from fastapi import FastAPI, Header, HTTPException
from image_registration.findit import Findit
from utils.paddleocr import OCR
from image_registration.exceptions import BaseError as CvError
from baseImage.exceptions import BaseError as ImageError
import binascii

from utils.request_item_model import base_item, best_result_response, paddleOCR_item
from utils import ParseImage, ResultModels, ResultErrorModels
from pydantic import BaseModel

from typing import Union, Dict
import time
app = FastAPI()
ocr = OCR()


@app.get('/')
def read_root():
    return {'Hello': "World"}


findit = Findit()


@app.post("/match/best/", response_model=best_result_response)
def tpl_best_result(item: base_item):
    try:
        im_source = ParseImage.b64decode_np(item.im_source)
        im_search = ParseImage.b64decode_np(item.im_search)
        result = findit.find_best_result(im_source=im_source, im_search=im_search, threshold=item.threshold,
                                         rgb=item.rgb)
    except (binascii.Error, ImageError):
        raise HTTPException(status_code=200, detail=ResultErrorModels.ImageError())
    except CvError:
        raise HTTPException(status_code=200, detail=ResultErrorModels.RecognizeError())

    if result:
        return ResultModels.find_best(result)


@app.post("/ocr/paddle/general_basic")
def paddleocr_general_basic(item: paddleOCR_item):
    """基础识别, 不包含检测位置, 只识别. det=False, res=True, cls=False"""
    try:
        img = ParseImage.b64decode_np(item.image)
        result = ocr.ocr(image=img, det=False, lang=item.lang)
    except (binascii.Error, ImageError):
        raise HTTPException(status_code=200, detail=ResultErrorModels.ImageError())

    if result:
        return ResultModels.ocr_general_basic(result)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8081)

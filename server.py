from fastapi import FastAPI, Header
from image_registration import MatchTemplate, CudaMatchTemplate, SIFT, RootSIFT, SURF, CUDA_SURF, findit, ORB, CUDA_ORB

from utils.request_item_model import base_item, best_result_response
from utils import ParseImage, ResultModels
from pydantic import BaseModel

from typing import Union, Dict
import time
app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': "World"}


tpl = CudaMatchTemplate()

# TODO: 错误处理(图片解码错误,find_best错误)


@app.post("/tpl/best/", response_model=best_result_response)
def tpl_best_result(item: base_item):
    im_source = ParseImage.b64decode_np(item.im_source)
    im_search = ParseImage.b64decode_np(item.im_search)
    result = tpl.find_best_result(im_source=im_source, im_search=im_search, threshold=item.threshold,
                                  rgb=item.rgb)
    if result:
        return ResultModels.find_best(result)


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8081)

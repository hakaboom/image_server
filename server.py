import base64
import cv2
from fastapi import FastAPI, Response, Header, status, File, UploadFile, Form
from fastapi.responses import JSONResponse, ORJSONResponse
from image_registration import MatchTemplate, CudaMatchTemplate, SIFT, RootSIFT, SURF, CUDA_SURF, findit, ORB, CUDA_ORB
from baseImage import IMAGE
from pydantic import BaseModel
import numpy as np

from typing import Optional, Union, List
import pickle
import time

from utils.request_item_model import base_item
from utils import ParseImage

app = FastAPI()


@app.get('/')
def read_root():
    return {'Hello': "World"}


tpl = CudaMatchTemplate()


@app.post("/tpl/best/", response_class=ORJSONResponse)
def tpl_best_result(item: base_item, image_format: str = Header(None, examples={
    'pickle-ndarray': {
        'summary': 'pickle-ndarray',
        "description": "python pickle序列化后的numpy数组",
    }
})):
    result = {}
    if image_format == 'pickle-ndarray':
        im_source = ParseImage.pickle_np(item.im_source)
        im_search = ParseImage.pickle_np(item.im_search)
    else:
        im_source = ParseImage.b64decode_np(item.im_source)
        im_search = ParseImage.b64decode_np(item.im_search)

    _result = tpl.find_best_result(im_source=im_source, im_search=im_search, threshold=item.threshold,
                                   rgb=item.rgb)
    if _result:
        result.update(_result)
    return result


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8081)

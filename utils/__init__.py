import base64
import pickle
from typing import Union, Optional, List

import cv2
import numpy as np

from baseImage import Rect


class ParseImage(object):
    @staticmethod
    def pickle_np(src: str) -> np.ndarray:
        """
        限定与python交互的格式，接受一个使用pickle序列化的ndarray数组

        Args:
            src: pickle序列化的ndarray数组

        Returns:
            np.ndarray
        """
        img_b64decode = base64.b64decode(src)
        img = pickle.loads(img_b64decode)
        return img

    @staticmethod
    def b64decode_np(src: str) -> np.ndarray:
        """
        接受一个b64encode且cv_encode后的字符串,转换为ndarray数组

        Args:
            src:

        Returns:
            np.ndarray
        """
        str_decode = base64.b64decode(src)
        nparray = np.frombuffer(str_decode, np.uint8)
        img = cv2.imdecode(nparray, cv2.IMREAD_COLOR)
        return img


class ResultModels(object):
    @staticmethod
    def find_best(res: dict) -> dict:
        rect: Rect = res.get('rect')
        confidence = res.get('confidence')

        return {
            'rect': {
                'x': rect.x,
                'y': rect.y,
                'width': rect.width,
                'height': rect.height,
            },
            'confidence': confidence,
        }

    @staticmethod
    def ocr_general_basic(res: list):
        return {
            'text': res[0][0],
            'confidence': res[0][1],
        }


class ResultErrorModels(object):
    @staticmethod
    def ImageError():
        return {
          "error_code": 100,
          "error_msg": "图片错误，请检查后重新尝试"
        }

    @staticmethod
    def RecognizeError():
        return {
          "error_code": 101,
          "error_msg": "识别错误，请再次请求"
        }

    @staticmethod
    def MissingParameters(params: Union[str, list]):
        return {
          "error_code": 102,
          "error_msg": f"请求参数缺失: {params}"
        }

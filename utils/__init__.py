import base64
import pickle

import cv2
import numpy as np


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

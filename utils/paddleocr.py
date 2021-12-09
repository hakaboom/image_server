# -*- coding: utf-8 -*-
import json
from paddleocr import PaddleOCR


class OCR(object):
    def __init__(self, use_gpu=False):
        self.use_gpu = use_gpu
        self.func = {}
        for lang in ['ch', 'en', 'japan']:
            self.create_ocr(lang, use_gpu=use_gpu)

    def create_ocr(self, lang, use_gpu=False):
        try:
            ocr = PaddleOCR(lang=lang, use_gpu=use_gpu or self.use_gpu, use_angle_cls=True, gpu_mem=200)
        except AssertionError:
            print('创建OCR实例失败: lang={}'.format(lang))
        else:
            self.func[lang] = ocr

    def ocr(self, image, lang='ch', det=True, rec=True):
        draw_ocr = self.func[lang]
        result = draw_ocr.ocr(image, det=det, rec=rec)
        return result

# -*- coding: utf-8 -*-
import requests
from baseImage import IMAGE
import json
import time
import base64
import numpy as np
import urllib.parse
import cv2
import pickle
request_url = "http://127.0.0.1:8081/tpl/best/"
#
for i in range(1):
    start_time = time.time()
    im_source: np.ndarray = IMAGE('test.png').imread()
    im_search: np.ndarray = IMAGE('test.png').imread()

    im_source_str = cv2.imencode('.png', im_source)[1].tobytes()
    im_search_str = cv2.imencode('.png', im_search)[1].tobytes()
    b64_source = base64.b64encode(im_search_str).decode()
    b64_search = base64.b64encode(im_search_str).decode()

    params = json.dumps(dict(
        im_source=b64_source,
        im_search=b64_search,
    ))

    response = requests.post(request_url, data=params)
    print(response.json())

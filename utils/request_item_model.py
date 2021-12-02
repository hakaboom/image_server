from pydantic import BaseModel
from typing import Union, Optional, Any
from fastapi import File, Form



class base_item(BaseModel):
    im_source: str
    im_search: str
    threshold: Union[int, float, None] = 0.8
    rgb: Optional[bool] = True


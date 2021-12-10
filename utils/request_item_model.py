from pydantic import BaseModel, Field
from typing import Union, Optional, Any
from fastapi import File, Form, Query


class base_item(BaseModel):
    im_source: str
    im_search: str
    threshold: Union[int, float, None] = Field(0.8, gt=0, le=1)
    rgb: Optional[bool] = True


class _Rect(BaseModel):
    x: Union[int, float] = Field(..., ge=0)
    y: Union[int, float] = Field(..., ge=0)
    width: Union[int, float] = Field(..., ge=0)
    height: Union[int, float] = Field(..., ge=0)


class best_result_response(BaseModel):
    rect: _Rect
    confidence: float = Field(..., ge=0, le=1)


class paddleOCR_item(BaseModel):
    img: Any
    lang: Optional[str] = 'ch'  # 默认识别语言


class general_basic_response(BaseModel):
    text: str
    confidence: float = Field(..., ge=0, le=1)

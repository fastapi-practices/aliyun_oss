#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from typing import Annotated

from fastapi import APIRouter, File, UploadFile

from backend.common.dataclasses import UploadUrl
from backend.common.response.response_schema import ResponseSchemaModel, response_base
from backend.common.security.jwt import DependsJwtAuth
from backend.plugin.aliyun_oss.utils.file_ops import oss_put_object
from backend.utils.file_ops import upload_file_verify

router = APIRouter()


@router.post('/image', summary='上传图片', dependencies=[DependsJwtAuth])
async def oss_image(file: Annotated[UploadFile, File()]) -> ResponseSchemaModel[UploadUrl]:
    upload_file_verify(file)
    url = await oss_put_object(file)
    return response_base.success(data={'url': url})


@router.post('/video', summary='上传视频', dependencies=[DependsJwtAuth])
async def oss_video(file: Annotated[UploadFile, File()]) -> ResponseSchemaModel[UploadUrl]:
    upload_file_verify(file)
    url = await oss_put_object(file)
    return response_base.success(data={'url': url})

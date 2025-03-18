#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import oss2

from asgiref.sync import sync_to_async
from fastapi import UploadFile

from backend.common.exception import errors
from backend.common.log import log
from backend.plugin.aliyun_oss.conf import oss_settings
from backend.utils.file_ops import build_filename


def get_oss_buket() -> oss2.Bucket:
    """获取阿里云 oss buket"""
    auth = oss2.Auth(oss_settings.OSS_ACCESS_KEY, oss_settings.OSS_SECRET_KEY)
    buket = oss2.Bucket(auth, oss_settings.OSS_ENDPOINT, oss_settings.OSS_BUCKET_NAME)
    return buket


@sync_to_async
def oss_put_object(file: UploadFile) -> str:
    """
    oss 简单上传（bytes）

    :param file:
    :return:
    """
    filename = build_filename(file)
    buket = get_oss_buket()
    try:
        res = buket.put_object(filename, file.file)
    except Exception as e:
        log.error(f'上传文件 {filename} 失败：{str(e)}')
        raise errors.RequestError(msg='上传文件失败')
    return res.resp.response.url

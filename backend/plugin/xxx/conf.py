#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

# from backend.core.path_conf import BasePath


class XxxSettings(BaseSettings):
    """xxx Settings"""

    # model_config = SettingsConfigDict(env_file=f'{BasePath}/.env', env_file_encoding='utf-8', extra='ignore')



@lru_cache
def get_xxx_settings() -> XxxSettings:
    """获取 xxx 配置"""
    return XxxSettings()


xxx_settings = get_xxx_settings()

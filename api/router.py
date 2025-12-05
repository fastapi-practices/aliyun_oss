from fastapi import APIRouter

from backend.core.conf import settings
from backend.plugin.aliyun_oss.api.v1.oss import router as oss_router

v1 = APIRouter(prefix=settings.FASTAPI_API_V1_PATH)

v1.include_router(oss_router, prefix='/oss', tags=['阿里云 OSS'])

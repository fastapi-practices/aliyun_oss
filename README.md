## 阿里云 OSS

1. 必须在环境变量文件 `.env` 中添加以下内容:

   ```dotenv
    # [ Plugin ] OSS
    OSS_ACCESS_KEY='阿里云 access key'
    OSS_SECRET_KEY='阿里云 secret key'
   ```

2. 在 core/conf.py 中添加以下内容:

   ```python
   ##################################################
   # [ Plugin ] OSS
   ##################################################
   # .env
   OSS_ACCESS_KEY: str
   OSS_SECRET_KEY: str
   
   # 基础配置
   OSS_BUCKET_NAME: str = 'fba-test'
   OSS_ENDPOINT: str = 'https://oss-cn-hangzhou.aliyuncs.com'
   ```



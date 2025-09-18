import os

import boto3
from dotenv import load_dotenv

load_dotenv()

s3 = boto3.client(
    "s3",
    endpoint_url=os.getenv("S3_ENDPOINT_URL"),
    aws_access_key_id=os.getenv("S3_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("S3_SECRET_KEY"),
)

bucket = os.getenv("S3_BUCKET")

# Пример загрузки
s3.upload_file("local_video.mp4", bucket, "videos/local_video.mp4")

# Пример получения ссылки
url = s3.generate_presigned_url(
    "get_object",
    Params={"Bucket": bucket, "Key": "videos/local_video.mp4"},
    ExpiresIn=3600,
)
print("Ссылка для скачивания:", url)

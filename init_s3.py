import os

import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()

S3_ENDPOINT_URL = os.getenv("S3_ENDPOINT_URL")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")
S3_BUCKET = os.getenv("S3_BUCKET")


def init_s3_bucket():
    """Проверяет наличие бакета и создаёт его, если не существует"""
    s3 = boto3.client(
        "s3",
        endpoint_url=S3_ENDPOINT_URL,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY,
    )

    try:
        buckets = [b["Name"] for b in s3.list_buckets()["Buckets"]]
        if S3_BUCKET in buckets:
            print(f"✅ Бакет '{S3_BUCKET}' уже существует")
        else:
            print(f"ℹ️  Бакет '{S3_BUCKET}' не найден, создаю...")
            s3.create_bucket(Bucket=S3_BUCKET)
            print(f"✅ Бакет '{S3_BUCKET}' создан")
    except ClientError as e:
        print(f"❌ Ошибка при работе с S3: {e}")
        raise


if __name__ == "__main__":
    init_s3_bucket()

import redis
import boto3
import json
from datetime import datetime, timezone
from config import Config

def main():
    Config.validate()

    redis_client = redis.Redis(
        host=Config.REDIS_HOST,
        port=Config.REDIS_PORT,
        decode_responses=True,
        socket_connect_timeout=5,
        socket_timeout=5
    )

    value = redis_client.get(Config.REDIS_KEY)
    if value is None:
        value = "No data found"

    payload = {
        "redis_key": Config.REDIS_KEY,
        "redis_value": value,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }

    s3_client = boto3.client("s3")
    s3_client.put_object(
        Bucket=Config.S3_BUCKET,
        Key=Config.S3_OBJECT_KEY,
        Body=json.dumps(payload, indent=2),
        ContentType="application/json"
    )
if __name__ == "__main__":
    main()


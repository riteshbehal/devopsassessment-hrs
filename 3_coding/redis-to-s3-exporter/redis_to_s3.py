import redis
import boto3
import json
from datetime import datetime, timezone

# ---------- CONFIG ----------
REDIS_HOST = "devops-assessment-redis.vrl0te.ng.0001.use1.cache.amazonaws.com"
REDIS_PORT = 6379
REDIS_KEY = "username"

S3_BUCKET = "amzn-s3datawebyear1"
S3_OBJECT_KEY = "data/task3-data.json"
# ----------------------------

# Connect to Redis
r = redis.Redis(
    host=REDIS_HOST,
    port=REDIS_PORT,
    decode_responses=True,
    socket_connect_timeout=5,
    socket_timeout=5
)

# Read data from Redis
value = r.get(REDIS_KEY)
if value is None:
    value = "No data found"

data = {
    "redis_key": REDIS_KEY,
    "redis_value": value,
    "timestamp": datetime.now(timezone.utc).isoformat()
}

# Upload to S3
s3 = boto3.client("s3")
s3.put_object(
    Bucket=S3_BUCKET,
    Key=S3_OBJECT_KEY,
    Body=json.dumps(data, indent=2),
    ContentType="application/json"
)

print("✅ Data successfully read from Redis and uploaded to S3")

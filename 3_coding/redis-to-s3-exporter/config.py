import os

class Config:
    # Redis configuration
    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))
    REDIS_KEY = os.getenv("REDIS_KEY", "username")

    # S3 configuration
    S3_BUCKET = os.getenv("S3_BUCKET")
    S3_OBJECT_KEY = os.getenv("S3_OBJECT_KEY", "data/task3-data.json")

    @staticmethod
    def validate():
        missing = []

        if not Config.REDIS_HOST:
            missing.append("REDIS_HOST")
        if not Config.S3_BUCKET:
            missing.append("S3_BUCKET")

        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}"
            )

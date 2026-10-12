
import os

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://hrudayai_user:local_dev_password@localhost:5432/hrudayai",
)
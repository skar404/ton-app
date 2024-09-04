import os
from pathlib import Path

from pydantic_settings import BaseSettings


class EnvConfig(
    BaseSettings,
    env_file=os.getenv("ENV_FILE", Path(__file__).parent.parent / ".env"),
):
    cache_time: int = 60


env = EnvConfig()

import enum
from functools import lru_cache
from pydantic_settings import BaseSettings

__all__ = [
    "get_settings",
    "BackendSettings",
    "RunningMode",
]


class RunningMode(enum.Enum):
    local = "local"
    docker = "docker"


class BackendSettings(BaseSettings):
    running_mode: RunningMode = RunningMode.local
    debug: bool = True


@lru_cache()
def get_settings() -> BackendSettings:
    return BackendSettings()
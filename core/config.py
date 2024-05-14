from pydantic_settings import BaseSettings


class ProjectSettings(BaseSettings):
    api_id: int
    api_hash: str

    class Config:
        env_file = ".env"


project_settings = ProjectSettings()

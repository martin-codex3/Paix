from pydantic_settings import BaseSettings, SettingsConfigDict


class AppConfig(BaseSettings):

    DATABASE_URL: str

    model_config = SettingsConfigDict(
        env_file=".env"
    )


# the object for the app config here
AppConfig = AppConfig()

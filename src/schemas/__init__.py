from pydantic import BaseSettings


class Settings(BaseSettings):
    # DATABASE_URL: PostgresDsn
    # PAGINATE_BY: PositiveInt = Field(default=5)

    class Config:
        # env_file = '.env'
        pass

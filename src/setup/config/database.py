from pydantic import BaseModel, PostgresDsn


class DatabaseSettings(BaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str

    @property
    def dsn(self) -> PostgresDsn:
        return PostgresDsn.build(
            scheme="postgresql+psycopg",
            username=self.user,
            password=self.password,
            host=self.host,
            port=self.port,
            path=self.database,
        )

from typing import Literal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()

def get_engine(db_type : Literal["sqlite", "mariadb"],
               db_name: str,
               user: str | None = None,
               password: str | None = None,
               host: str = "localhost",
               port: int = 3306):
    match db_type:
        case "sqlite":
            return create_engine(f"sqlite:///{db_name}", echo=True)
        case "mariadb":
            return create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{db_name}", echo=True)
        case _:
            raise ValueError(f"Unsupported database type : {db_type}")

def get_db(engine):
    Session = sessionmaker(bind=engine)
    return Session()
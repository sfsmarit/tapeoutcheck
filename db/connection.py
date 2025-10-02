from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.enums import DBType
import config 

from .models import Base


# Create engine
if config.DB_TYPE == DBType.MARIADB:
    engine = create_engine(f"mysql+pymysql://{config.USER}:{config.PASSWORD}@{config.HOST}:{config.PORT}/{config.DB_NAME}", echo=True)
elif config.DB_TYPE == DBType.SQLITE:
    engine = create_engine(f"sqlite:///{config.DB_NAME}", echo=True)
else:
    raise ValueError(f"Unsupported database type : {config.DB_TYPE}")

# Create tables
Base.metadata.create_all(engine)

def get_session():
    Session = sessionmaker(bind=engine)
    return Session()
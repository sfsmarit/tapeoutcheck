import re
from datetime import datetime

from sqlalchemy import Integer, String, Boolean, DateTime, Enum
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy.sql import func

from utils.enums import MaskType, FETech


Base = declarative_base()


class TapeoutData(Base):
    __tablename__ = 'tapeouts'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), default="")
    mask_type: Mapped[MaskType] = mapped_column(Enum(MaskType))
    fe_tech: Mapped[FETech] = mapped_column(Enum(FETech))
    designer: Mapped[str] = mapped_column(String(50), default="")
    skyfoundry_url: Mapped[str] = mapped_column(String(500), default="")
    sap_sheet_url: Mapped[str] = mapped_column(String(500), default="")
    
    def has_valid_name(self) -> bool:
        if not self.name:
            return False
        pattern = r"^[A-Z]{2}\d{3}-[A-Z]-[A-Z]{3}$"
        return bool(re.match(pattern, self.name))


class TaskData(Base):
    __tablename__ = 'tasks'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    tapeout: Mapped[str] = mapped_column(String(20), default="")
    task_id: Mapped[str] = mapped_column(String(64), default="")
    name: Mapped[str] = mapped_column(String(100), default="")
    status: Mapped[bool] = mapped_column(Boolean, default=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
from sqlalchemy import Column
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class Medication(ModelBase):
    __tablename__ = "medication"
    MedicationID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    Name = Column(pg.VARCHAR)
    Brand = Column(pg.VARCHAR)
    Description = Column(pg.VARCHAR, nullable=False) 
    
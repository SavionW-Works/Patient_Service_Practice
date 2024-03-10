from sqlalchemy import Column
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg

class Physician(ModelBase):
    __tablename__ = "physician"
    PhysicianID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    Firstname = Column(pg.VARCHAR)
    Lastname = Column(pg.VARCHAR)
    SSN = Column(pg.VARCHAR, nullable=False) 
    Title = Column(pg.VARCHAR)

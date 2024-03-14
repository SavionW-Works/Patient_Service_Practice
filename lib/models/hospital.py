from sqlalchemy import Column
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg 


class Hospital(ModelBase):
    __tablename__ = "hospital"
    HospitalID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    HospitalName = Column(pg.VARCHAR,nullable=False )
    Capacity = Column(pg.BIGINT,nullable=False )
    State = Column(pg.VARCHAR) 
    City = Column(pg.VARCHAR) 
    Zipcode = Column(pg.VARCHAR, nullable=False)

   

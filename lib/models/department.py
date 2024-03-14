from sqlalchemy import Column, ForeignKey
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg  
from lib.models.physician import Hospital 
from sqlalchemy.orm import mapped_column, relationship


class Department(ModelBase):
    __tablename__ = "department"
    DepartmentID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    DepartmentName = Column(pg.VARCHAR)
    HospitalID = mapped_column(pg.BIGINT,  ForeignKey(Hospital.HosptialID), nullable=False) #Exists in hospital


    # relationships
    hospital = relationship("Hospital", foreign_keys=[HospitalID]) #Reference hospital

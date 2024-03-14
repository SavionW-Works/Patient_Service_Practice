from sqlalchemy import Column, ForeignKey
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg  
from lib.models.physician import Department 
from sqlalchemy.orm import mapped_column, relationship


class Manager(ModelBase):
    __tablename__ = "manager"
    ManagerID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    
    Firstname = Column(pg.VARCHAR)
    Lastname = Column(pg.VARCHAR)
    SSN = Column(pg.VARCHAR, nullable=False) 
    DepartmentID = mapped_column(pg.BIGINT,  ForeignKey(Department.DepartmentID), nullable=False) #Exists in patient


    # relationships
    department = relationship("department", foreign_keys=[DepartmentID]) 

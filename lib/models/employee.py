from sqlalchemy import Column, ForeignKey
from lib.models.model_base import ModelBase
from lib.models.model_base import ModelBase
import sqlalchemy.dialects.postgresql as pg  
from lib.models.physician import Department, Manager 
from sqlalchemy.orm import mapped_column, relationship


class Employee(ModelBase):
    __tablename__ = "employee"
    EmployeeID = Column(
        pg.BIGINT,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    
    Firstname = Column(pg.VARCHAR)
    Lastname = Column(pg.VARCHAR)
    SSN = Column(pg.VARCHAR, nullable=False)  
    Title = Column(pg.VARCHAR)
    DepartmentID = mapped_column(pg.BIGINT,  ForeignKey(Department.DepartmentID), nullable=False) #Exists in department
    ManagerID = mapped_column(pg.BIGINT,  ForeignKey(Manager.DepartmentID), nullable=False) #Exists in manager


    # relationships
    department = relationship("department", foreign_keys=[DepartmentID]) 
    manager = relationship("manager", foreign_keys=[DepartmentID]) 

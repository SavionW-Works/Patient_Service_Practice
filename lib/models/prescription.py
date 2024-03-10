import datetime
import uuid
from sqlalchemy import Column, ForeignKey
from lib.models.model_base import ModelBase
from lib.models.physician import Physician 
from lib.models.medication import Medication
from sqlalchemy.orm import mapped_column, relationship
import sqlalchemy.dialects.postgresql as pg

class Prescription(ModelBase):
    __tablename__ = "prescription"
    PhysicianID = mapped_column(pg.BIGINT, ForeignKey(Physician.PhysicianID), nullable=False)
    PatientRecordNumber = Column(pg.BIGINT) 
    MedicationID = mapped_column(pg.BIGINT, ForeignKey(Medication.MedicationID), nullable=False)
    PrescribedOn = Column(pg.DATE, nullable=False)
    AppointmentID = Column(pg.BIGINT, nullable=False)
    Description = Column(pg.REAL, nullable=False) 
    
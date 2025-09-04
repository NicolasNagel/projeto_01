from sqlalchemy import Column, String, Float, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Machine(Base):
    __tablename__ = "machines"
    machine_id = Column(String, primary_key=True)
    machine_type = Column(String)
    installation_date = Column(Date)
    status = Column(String)

    maintenance = relationship("Maintenance", back_populates="machine")
    incidentes = relationship("Incident", back_populates="machine")

class Operator(Base):
    __tablename__ = "operator"
    operator_id = Column(String, primary_key=True)
    name = Column(String)
    shift = Column(String)
    experience_level = Column(String)

    maintenance = relationship("Maintenance", back_populates="operator")

class Maintenance(Base):
    __tablename__ = "maintenance"
    maintenance_id = Column(String, primary_key=True)
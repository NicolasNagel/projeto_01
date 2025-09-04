from pydantic import BaseModel, Field
from datetime import date

class MachineSchema(BaseModel):
    machine_id: str
    machine_type: str
    installation_date: date
    status: str

class OperatorSchema(BaseModel):
    operator_id: str
    name: str
    shift: str
    experience_level: str

class MaintenceSchema(BaseModel):
    maintence_id: str
    machine_id: str
    operator_id: str
    date: date
    maintence_type: str
    duration_hours: float = Field(gt=0)
    cost: float = Field(gt=0)

class IncidentSchema(BaseModel):
    incident_id: str
    machine_id: str
    date: date
    downtime_hours: float = Field(gt=0)
    description: str
from model.schema import MachineSchema, OperatorSchema, MaintenceSchema, IncidentSchema
from src.data import machines, operators, maintece, incidentes

for _, row in machines.iterrows():
    valid = MachineSchema(**row.to_dict())
    print(valid.model_dump())

for _, row in operators.iterrows():
    valid = OperatorSchema(**row.to_dict())
    print(valid.model_dump())

for _, row in maintece.iterrows():
    valid = MaintenceSchema(**row.to_dict())
    print(valid.model_dump())

for _, row in incidentes.iterrows():
    valid = IncidentSchema(**row.to_dict())
    print(valid.model_dump())
from model.schema import MachineSchema, OperatorSchema, MaintenceSchema, IncidentSchema
from src.data import machines, operators, maintece, incidents

MAPPING = {
    "machines": {
        "schema": MachineSchema,
        "orm": "...",
        "data": machines
    },
    "operators": {
        "schema": OperatorSchema,
        "orm": "...",
        "data": operators
    },
    "maintence": {
        "schema": MaintenceSchema,
        "orm": "...",
        "data": maintece
    },
    "incidents": {
        "schema": IncidentSchema,
        "orm": "...",
        "data": incidents
    }
}
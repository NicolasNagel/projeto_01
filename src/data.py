import pandas as pd
import random

from faker import Faker

fake = Faker()

# Parametros
MACHINES = 10
OPERATORS = 5
MAINTENCE = 50
INCIDENTS = 30

# Tabela de Máquinas 
machines = pd.DataFrame({
    "machine_id": [f"M{i+1}" for i in range(MACHINES)],
    "machine_type": [random.choice(["CNC", "Lathe", "Press", "Drill"]) for _ in range(MACHINES)],
    "installation_date": [fake.date_between(start_date="-5y", end_date="today") for _ in range(MACHINES)],
    "status": [random.choice(["Active", "Inactive", "Under Repair"]) for _ in range(MACHINES)]
})

# Tabela de Operadores
operators = pd.DataFrame({
    "operator_id": [f"O{i+1}" for i in range(OPERATORS)],
    "name": [fake.name() for _ in range(OPERATORS)],
    "shift": [random.choice(["Morning", "Evening", "Night"]) for _ in range(OPERATORS)],
    "experience_level": [random.choice(["Junior", "Mid", "Senior"]) for _ in range(OPERATORS)],
})

# Tabela de Manutenção
maintece = pd.DataFrame({
    "maintence_id":[f"MT{i+1}" for i in range(MAINTENCE)],
    "machine_id": [random.choice(machines["machine_id"]) for _ in range(MAINTENCE)],
    "operator_id": [random.choice(operators["operator_id"]) for _ in range(MAINTENCE)],
    "date": [fake.date_between(start_date="-1y", end_date="today") for _ in range(MAINTENCE)],
    "maintence_type": [random.choice(["Preventive", "Corrective"]) for _ in range(MAINTENCE)],
    "duration_hours": [round(random.uniform(1, 6), 2) for _ in range(MAINTENCE)],
    "cost": [round(random.uniform(100, 1000), 2) for _ in range(MAINTENCE)],
})

# Tabela de Incidentes
incidents = pd.DataFrame({
    "incident_id": [f"I{i+1}" for i in range(INCIDENTS)],
    "machine_id": [random.choice(machines["machine_id"]) for _ in range(INCIDENTS)],
    "date": [fake.date_between(start_date="-1y", end_date="today") for _ in range(INCIDENTS)],
    "downtime_hours": [round(random.uniform(1, 10), 2) for _ in range(INCIDENTS)],
    "description": [random.choice(["Overheating", "Mechanical Failure", "Sensor Error"]) for _ in range(INCIDENTS)],
})
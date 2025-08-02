import torch
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

from src.model import ElectricityCostRegressor

app = FastAPI()

class InputData(BaseModel):
    site_area: float
    water_consumption: float
    recycling_rate: float
    utilisation_rate: float
    air_qality_index: float
    issue_reolution_time: float
    resident_count: float
    structure_type_Commercial: float
    structure_type_Industrial: float
    structure_type_Mixed_use: float
    structure_type_Residential: float

input_dim = 11
model = ElectricityCostRegressor(input_dim=input_dim)
model.load_state_dict(torch.load("results/electricity_cost_regressor.pth"))
model.eval()

@app.post("/predict")
def predict(data: InputData):
    features = np.array([[data.site_area, data.water_consumption, data.recycling_rate,
                          data.utilisation_rate, data.air_qality_index, data.issue_reolution_time,
                          data.resident_count, data.structure_type_Commercial,
                          data.structure_type_Industrial, data.structure_type_Mixed_use,
                          data.structure_type_Residential]])
    features_tensor = torch.tensor(features, dtype=torch.float32)
    with torch.no_grad():
        prediction = model(features_tensor).item()
    return {"predicted_electricity_cost": prediction}
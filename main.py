from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd


app = FastAPI()

# classe pour la saisie de donneés en entrée

class InputData(BaseModel):
    #Définir les champs pour les données en entrée
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

   

# charger le model entrainé

with open ('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Endpoint pour la prédiction

@app.post('/')

async def predict(input_data: InputData):
    #Transformer les données en entrées en dataframe pandas

    #input_df = pd.DataFrame([input_data.dict().values()], columns=input_data.dict().keys())
    input_df = pd.DataFrame([input_data.dict()])
    # Effectuer la prediction
    prediction = model.predict(input_df)

    # retrouner la prediction
    return {"prediction": prediction[0]}

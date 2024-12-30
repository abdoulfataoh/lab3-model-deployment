import mlflow
from fastapi import APIRouter


import app.settings as settings
from app.utils import HeartAttackPredictionInput

router = APIRouter()
mlflow.set_tracking_uri(uri=settings.MLFLOW_TRACKING_URI)
loaded_model = mlflow.sklearn.load_model(model_uri=settings.MODEL_URI)



@router.get('/health')
def health():
    return {'status': 'ok'}


@router.post("/predict")
def predict(input_data: HeartAttackPredictionInput):
    input_features = [[
        input_data.age, input_data.sex, input_data.cp,
        input_data.trtbps, input_data.chol, input_data.fbs,
        input_data.restecg, input_data.thalachh, input_data.exng,
        input_data.oldpeak, input_data.slp, input_data.caa,
        input_data.thall
    ]]
    prediction = loaded_model.predict(input_features)
    return {'prediction': int(prediction[0])}

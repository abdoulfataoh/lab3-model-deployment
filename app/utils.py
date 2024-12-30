from pydantic import BaseModel


class HeartAttackPredictionInput(BaseModel):
    age: int
    sex: int
    cp: int
    trtbps: float
    chol: float
    fbs: int
    restecg: int
    thalachh: float
    exng: int
    oldpeak: float
    slp: int
    caa: int
    thall: int

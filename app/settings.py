from environs import Env

env = Env()
env.read_env()

# [MLFLOW]
MLFLOW_TRACKING_URI = env("MLFLOW_TRACKING_URI", default='')
MLFLOW_EXPERIMENT_NAME = env("MLFLOW_EXPERIMENT_NAME", default='')

# [MODEL]
MODEL_URI = env("MODEL_URI", default='')

### Lab3 - Deploy Heart-attack
In this lab, you'll auto retrieve model from MLflow registry server and deploy it in prod env.

#### Build heart-attack

```bash
docker build -t heart-attack .
```

#### Run heart-atteck
```bash
docker run -d -p 8001:8001 \
-e MLFLOW_TRACKING_URI=MLFLOW_TRACKING_URI \
-e MLFLOW_EXPERIMENT_NAME=MLFLOW_EXPERIMENT_NAME \
-e MODEL_URI=MODEL_URI heart-attack
```

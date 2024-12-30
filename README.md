### Lab3 - Deploy Heart-attack

#### Build heart-attack

```bash
docker build -t heart-attack .
```

#### Run heart-atteck
```bash
docker run -d -p 8001:8001 -e MLFLOW_TRACKING_URI=MLFLOW_TRACKING_URI -e MLFLOW_EXPERIMENT_NAME=MLFLOW_EXPERIMENT_NAME MODEL_URI=MODEL_URI heart-attack
```
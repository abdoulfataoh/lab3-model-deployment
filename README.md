### Lab3 - Deploy Heart-attack
In this lab, you'll auto retrieve model from MLflow registry server and deploy it in prod env.

#### 0. Clone this project

```bash
git clone https://github.com/abdoulfataoh/lab3-model-deployment.git
cd lab3-model-deployment
```

#### 1. Build heart-attack

```bash
docker build -t heart-attack .
```

#### 3. Run heart-atteck
```bash
docker run -d -p 8001:8001 \
-e MLFLOW_TRACKING_URI='MLFLOW_TRACKING_URI' \
-e MLFLOW_EXPERIMENT_NAME='MLFLOW_EXPERIMENT_NAME' \
-e MODEL_URI='MODEL_URI' heart-attack
```
> Replace 'MLFLOW_TRACKING_URI', 'MLFLOW_EXPERIMENT_NAME', and 'MODEL_URI' by the corrects values

#### 4. Check fastapi docs
```bash
http://127.0.0.1:8001/docs
```

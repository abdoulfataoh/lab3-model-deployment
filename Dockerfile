# Coding: utf-8

# [Base image]
FROM python:3.11

# [Meta data]
LABEL name="demo-deploy-ml"
LABEL authors="abdoulfataoh-from-citadel"

# [Wordir]
WORKDIR /src

# [Env variables]
ENV MLFLOW_TRACKING_URI=${MLFLOW_TRACKING_URI}
ENV MLFLOW_EXPERIMENT_NAME=${MLFLOW_EXPERIMENT_NAME}
ENV MODEL_URI=${MODEL_URI}

# [Source code]
ADD ./ /src

# [Expose port]
EXPOSE 8001

# [Install poetry]
RUN pip install -U pip
RUN pip install poetry

# [Install requiered modules]
RUN poetry config virtualenvs.in-project true
RUN poetry install

# [Enable venv]
ENV PATH="/src/.venv/bin:$PATH"

# [Start the app]
CMD [ "make", "run" ]

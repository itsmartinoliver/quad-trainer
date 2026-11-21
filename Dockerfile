FROM python:3.10

COPY pyproject.toml .
COPY rpo_continuous_action.py .
COPY envs ./envs
COPY utils ./utils

RUN pip install .

ENTRYPOINT ["python", "rpo_continuous_action.py"]
CMD ["--env-id", "quad_stable", "--track"]

FROM python:3.10

COPY pyproject.toml .
COPY ppo_continuous_action.py .
COPY env.py .
COPY utils ./utils
COPY cleanrl_utils ./cleanrl_utils

RUN pip install .

ENTRYPOINT ["python", "ppo_continuous_action.py"]
CMD ["--env-id", "Quad-v0", "--total-timesteps", "50000", "--seed", "1", "--save-model"]

FROM python:3.10

COPY pyproject.toml .
COPY ppo_continuous_action.py .
COPY env.py .
COPY utils ./utils
COPY cleanrl_utils ./cleanrl_utils

RUN pip install .

ENTRYPOINT ["python", "train.py"]
CMD ["ppo", "Quad_v0", "50000", "1", "-s", "-c"]

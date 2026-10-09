# Quad Trainer

This project is built on CleanRL and trains a model to fly quadcopters.

### Setting Up
`cd quad-trainer`  
Create virtual environment with `python3.10 -m venv venv`  
Activate with `source venv/bin/activate`  
Install dependencies with `pip install .`

### Training
Run `python ppo_continuous_action.py --env-id Quad-v0 --total-timesteps 50000 --seed 1 --save-model --capture-video`
and `tensorboard --logdir runs`
to train and view results.

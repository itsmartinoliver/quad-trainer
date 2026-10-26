# Quad Trainer

This project is built on CleanRL and trains a model to fly quadcopters.

### Setting Up
`cd quad-trainer`  
Create virtual environment with `python3.10 -m venv venv`  
Activate with `source venv/bin/activate`  
Install dependencies with `pip install .`

### Training
Run `python train.py ppo Quad_v0 50000 1` to train
and `tensorboard --logdir runs` to view results.

### My Notes
Building with Docker: `docker buildx build -t itsmartinoliver/quad-trainer:latest --platform linux/amd64,linux/arm64 .` (in quad-trainer directory)  
Upload to Docker Hub with `docker push itsmartinoliver/quad-trainer:latest`

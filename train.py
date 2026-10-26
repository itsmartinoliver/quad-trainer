import subprocess
import argparse

algorithms={"ppo": "ppo_continuous_action.py"}

parser = argparse.ArgumentParser("train.py")
parser.add_argument("algorithm", help="Algorithm to be used for training", type=str)
parser.add_argument("environment", help="Environment to be trained on", type=str)
parser.add_argument("timesteps", help="Number of total timesteps", type=int)
parser.add_argument("seed", help="Seed for training algorithm", type=int)
args = parser.parse_args()

# TODO: Add --save-model, --capture-video, and options for gcloud storage
subprocess.run([
    "python", algorithms[args.algorithm],
    "--env-id", args.environment,
    "--total-timesteps", str(args.timesteps),
    "--seed", str(args.seed)
    ])

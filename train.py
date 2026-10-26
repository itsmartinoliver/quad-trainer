import subprocess
import argparse

algorithms={"ppo": "ppo_continuous_action.py"}

parser = argparse.ArgumentParser("train.py")

# Positional arguments
parser.add_argument("algorithm", help="Algorithm to be used for training", type=str)
parser.add_argument("environment", help="Environment to be trained on", type=str)
parser.add_argument("timesteps", help="Number of total timesteps", type=int)
parser.add_argument("seed", help="Seed for training algorithm", type=int)

# Optional arguments
parser.add_argument("-s", "--save_model", action="store_true", help="Save the model after training")
parser.add_argument("-c", "--capture_video", action="store_true", help="Render clips of training process")

args = parser.parse_args()

command=[
    "python", algorithms[args.algorithm],
    "--env-id", args.environment,
    "--total-timesteps", str(args.timesteps),
    "--seed", str(args.seed)
    ]

if (args.save_model): command.append("--save-model")
if (args.capture_video): command.append("--capture-video")

subprocess.run(command)

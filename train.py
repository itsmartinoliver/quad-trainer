import subprocess
import argparse

algorithms = {"ppo": "ppo_continuous_action.py"}

parser = argparse.ArgumentParser("train.py")

# Positional arguments
parser.add_argument("algorithm", help="Algorithm to be used for training", type=str)
parser.add_argument("environment", help="Environment to be trained on", type=str)
parser.add_argument("timesteps", help="Number of total timesteps", type=int)
parser.add_argument("seed", help="Seed for training algorithm", type=int)

# Optional arguments
parser.add_argument("-s", "--save_model", action="store_true", help="Save the model after training")
parser.add_argument("-c", "--capture_video", action="store_true", help="Render clips of training process")
parser.add_argument("-b", "--bucket", type=str, help="Upload results to Google Cloud bucket")

args = parser.parse_args()

command = [
    "python", algorithms[args.algorithm],
    "--env-id", args.environment,
    "--total-timesteps", str(args.timesteps),
    "--seed", str(args.seed)
    ]

if (args.save_model): command.append("--save-model")
if (args.capture_video): command.append("--capture-video")

subprocess.run(command)

# After training, upload to gcloud storage bucket;
if (args.bucket):
    print(f"Uploading runs to Google Cloud bucket {args.bucket}...")
    subprocess.run(["python", "upload_folder.py", "runs", args.bucket])
    print(f"Uploading videos to Google Cloud bucket {args.bucket}...")
    subprocess.run(["python", "upload_folder.py", "videos", args.bucket])

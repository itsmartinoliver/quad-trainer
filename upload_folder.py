from pathlib import Path
import argparse
from google.cloud import storage

def upload_folder(folder: Path, bucket_name: str, prefix: str = "") -> None:
    folder = folder.expanduser().resolve()

    if not folder.is_dir():
        raise NotADirectoryError(f"Not a folder: {folder}")

    client = storage.Client()
    bucket = client.bucket(bucket_name)

    files = [path for path in folder.rglob("*") if path.is_file()]

    for path in files:
        # Preserve the folder structure relative to the selected root.
        object_name = (Path(prefix) / path.relative_to(folder)).as_posix()
        bucket.blob(object_name).upload_from_filename(str(path))
        print(f"Uploaded {path} → gs://{bucket_name}/{object_name}")

    print(f"Done: uploaded {len(files)} file(s).")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Recursively upload a folder to Google Cloud Storage."
    )
    parser.add_argument("folder", help="Local folder to upload")
    parser.add_argument("bucket", help="Destination bucket name")
    parser.add_argument(
        "--prefix",
        default="",
        help="Optional destination path inside the bucket, e.g. backups/2026",
    )
    args = parser.parse_args()

    upload_folder(Path(args.folder), args.bucket, args.prefix)

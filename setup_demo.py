import ssl
import certifi
import urllib.request

url = "https://github.com/marquisedemaree/RAT/releases/download/v1.0/data.zip"
out = "https://github.com/marquisedemaree/RAT/releases/download/v1.0/models.zip"

ssl_context = ssl.create_default_context(cafile=certifi.where())

urllib.request.urlretrieve(url, out)

import os
import ssl
import certifi
import urllib.request
import zipfile
from pathlib import Path


# CONFIG
MODELS_URL = "https://github.com/marquisedemaree/RAT/releases/download/v1.0/models.zip"
DATA_URL = "https://github.com/marquisedemaree/RAT/releases/download/v1.0/data.zip"
MODELS_ZIP = "models.zip"
DATA_ZIP = "data.zip"


def download_file(url, output_path):
    print(f"⬇️  Downloading {url}...")

    ssl_context = ssl.create_default_context(cafile=certifi.where())

    with urllib.request.urlopen(url, context=ssl_context) as response:
        with open(output_path, "wb") as f:
            f.write(response.read())

    print(f"✅ Saved to {output_path}")


def unzip_file(zip_path, extract_to="."):
    print(f"📦 Extracting {zip_path}...")

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

    print(f"✅ Extracted {zip_path}")


def validate_structure():
    print("🔍 Validating folder structure...")

    expected_paths = [
        Path("models/rsna_model.pth"),
        Path("data/demo_scans"),
        Path("data/demo_labels.csv"),
    ]

    missing = [str(p) for p in expected_paths if not p.exists()]

    if missing:
        print("❌ Setup incomplete. Missing:")
        for m in missing:
            print(f"   - {m}")
        return False

    print("✅ Folder structure is correct")
    return True


def main():
    # Create base directories
    Path("models").mkdir(exist_ok=True)
    Path("data").mkdir(exist_ok=True)

    # Download files
    download_file(MODELS_URL, MODELS_ZIP)
    download_file(DATA_URL, DATA_ZIP)

    # Extract
    unzip_file(MODELS_ZIP)
    unzip_file(DATA_ZIP)

    # Remove zip files
    os.remove(MODELS_ZIP)
    os.remove(DATA_ZIP)
    print("🧹 Cleaned up zip files")

    # Validate
    validate_structure()


if __name__ == "__main__":
    main()

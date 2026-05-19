from pathlib import Path

SUPPORTED_EXTENSIONS = [".csv", ".xlsx", ".json"]

def validate_file(path: str):
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    if file_path.suffix not in SUPPORTED_EXTENSIONS:
        raise ValueError(f"Unsupported file type: {file_path.suffix}")

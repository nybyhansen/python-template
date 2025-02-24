import subprocess
import sys


def is_uv_installed() -> bool:
    try:
        subprocess.run(["uv", "--version"], capture_output=True, check=True)
        return True

    except Exception:
        return False


def is_taskfile_installed() -> bool:
    try:
        subprocess.run(["task", "--version"], capture_output=True, check=True)
        return True

    except Exception:
        return False


if __name__ == "__main__":
    if not is_uv_installed():
        print("error: uv is not installed.")
        sys.exit(1)

    if not is_taskfile_installed():
        print("error: taskfile is not installed.")
        sys.exit(1)

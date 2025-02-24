import subprocess
import sys


def clone_remote_repo() -> bool:

    if not {{cookiecutter.init_git}}:  # type: ignore
        return True

    remote_repo_url = "{{ cookiecutter.remote_repo_url }}"

    try:
        subprocess.run(["git", "init"], capture_output=True, check=True)
        if remote_repo_url:
            subprocess.run(
                ["git", "remote", "add", "origin", f"{remote_repo_url}"],
                capture_output=True,
                check=True,
            )
        return True

    except Exception:
        return False


def init_project_environment() -> bool:
    try:
        subprocess.run(["task", "init"], capture_output=True, check=True)
        return True

    except Exception:
        return False


if __name__ == "__main__":
    clone_repo_response = clone_remote_repo()
    if not clone_repo_response:
        sys.exit(1)

    init_installed = init_project_environment()
    if not init_installed:
        print("error: could not initilize project environment")
        sys.exit(1)

import pytest
from cookiecutter.main import cookiecutter


@pytest.fixture(scope="function")
def project_base(tmp_path) -> None:
    return cookiecutter(
        template=".",
        output_dir=tmp_path,
        keep_project_on_failure=False,
        no_input=True,
        extra_context={
            "name": "test_project",
            "description": "test project",
            "init_git": False,
            "remote_repo_url": "",
        },
    )


@pytest.fixture(scope="function")
def project_base_remote_git(tmp_path) -> None:
    return cookiecutter(
        template=".",
        output_dir=tmp_path,
        keep_project_on_failure=False,
        no_input=True,
        extra_context={
            "name": "test_project",
            "description": "test project",
            "init_git": True,
            "remote_repo_url": "https://github.com/innersource-nn/python-templates-test.git",
        },
    )

def test_that_project_can_initiate(project_base, tmp_path):
    files = [_.name for _ in tmp_path.iterdir()]
    assert "test_project" in files


def test_that_project_can_initiate_with_remote_git(project_base_remote_git, tmp_path):
    files = [_.name for _ in tmp_path.iterdir()]
    assert "test_project" in files

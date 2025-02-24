<h1 style="text-align:center;">PYTHON TEMPLATE</h1>

<p align="center"><img src="doc/template-logo.png" alt="drawing" width="250">

This repository contains a **generic python template** to help you kickstart your new project quickly and with appropriate quality measures. This means that the template comes with no opinions on how you should structure your project or what kind of application you should create. The template has a very strict configuration for automated quality checks (pre-commit, ruff, black etc.), and so, do expect to write your code with type annotations, consistent use of docstrings and no dead code ;-)

## Use this template

If you want to use this template, first make sure you have [cookiecutter](https://cookiecutter.readthedocs.io/en/2.0.2/installation.html) installed as well as these dependencies:

- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- [Taskfile](https://taskfile.dev/installation/)

Now, enter the command in your terminal:

```bash
cookiecutter https://github.com/nybyhansen/python-template
```

You will be prompted to configure your project (see parameters below) and the template will be applied. Navigate into new project folder and test that everything works by running the test suite:

```bash
task test
```

Please leave a star on this repository if you use the template. This will give us an indication of its use - thanks!

### Input parameters

| Parameter       | Description                                       | Default |
| :-------------- | :------------------------------------------------ | :-----: |
| name            | name of the project                               |    -    |
| description     | short description of the project                  |    -    |
| init_git        | if git should be initialized                      |  false  |
| remote_repo_url | url for remote repository, i.e. Github (optional) |    -    |

## Contribute to the template

Contributions to the template are very welcome!

**Please create an issue** about the change you would like to see - no matter if you intend to implement it yourself or pass the idea on to someone else.

### Getting started

After cloning the repository, make sure that you have `uv` and `Taskfile` installed as described earlier. Now, you only have to run the following command in your terminal:

```bash
task init
```

Enjoy your coding!

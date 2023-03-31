import os
import subprocess

include_analysis_directories = bool("{{cookiecutter.analysis}}" == "y")

if include_analysis_directories:
    os.makedirs(
        os.path.join(
            os.getcwd(),
            "src",
        )
    )
    os.makedirs(
        os.path.join(
            os.getcwd(),
            "data",
        )
    )
    os.makedirs(
        os.path.join(
            os.getcwd(),
            "notebook",
        )
    )

print("Installing the dependencies ...")
subprocess.call(["make", "install"])

print("Initializing a git repo ...")
subprocess.call(["git", "init"])
subprocess.call(["git", "add", "*"])
subprocess.call(["git", "commit", "-m", "Initial commit"])

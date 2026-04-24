import subprocess


def initialize_repo(repo_name, branch_name):
    # then let's initialize a repo (an empty one or existing one)
    gitRepo = subprocess.run(["git", "init"], capture_output=True, text=True)
    print(gitRepo)


# know the difference between local and remote workflows areas

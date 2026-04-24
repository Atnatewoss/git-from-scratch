import subprocess


def git_workflows(workflow_tree, staged, committed, branch_name):
    # starting with the local workflow area
    # there are three working areas in git
    # 1. the working tree (which consists of untracked files, if not commited before)
    # demo data:
    #   1.1 create a file called my_first_file.py `through running [ni my_first_file.py] in the terminal`
    #   1.2 write this into it `This is the content of my first file.`

    # we have a check here if the change we made is wrong or we want to undo it before it's staged, we can do so using the command:
    # reverse_options = ["checkout", "restore"]
    checkoutResult = subprocess.run(
        ["git", "checkout", "filename"],
        capture_output=True,
        text=True,
    )
    print(checkoutResult)
    # If there's no issue, then we can stage it if it's correct.

    # 2. the staging area (to have git recognize our change/s and start tracking it we need to add it to the staging area)
    stagingResult = subprocess.run(
        ["git", "add", "file-names (in our case the my_first_file.py)"],
        capture_output=True,
        text=True,
    )
    print(stagingResult)
    # On the topic of checking out: (all this checkout is before the change is staged though, what do we do if we stage something we don't want to or didn't intend to)
    # we can unstage our changes by using the git ​reset command.

    # 3. the commit change (now that git is tracking our changes and the repo is initialized and the changes we make can be identified back to us because it's configured, now have all the changes into one consistent copy showing )
    commitResult = subprocess.run(
        ["git", "commit", "-m", "this is my first commit"],
        capture_output=True,
        text=True,
    )
    print(commitResult)


# now let's make a change to our file by adding a second line
# add a second line in my_first_file.py, "This is the second content of my first file" and then stage and commit, like we did earlier.
# 1. running `subprocess.run(["git", "add", "my_first_file.py"], text=True)` -> (adding the untracked to the stage)
# 2. run `subprocess.run(["git", "commit", "-m", "add a second line"], text=True)`

# any time you want to check the tracked and untracked changes you can using `git status`
# and if you want to see your commit history, you can also do that by running `git log`

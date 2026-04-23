import subprocess

# Pre-requisite: make sure you have git installed
# check by opening your terminal and typing `git --version`

list_of_commands = [
    # list all of the commmands used in the tools here, to track them as a check list
]

list_of_branches = ["main"]


def manage_branch_workflow():
    default_branch = "main"
    allowed_actions = [
        "create branch",
        "change branch",
        "delete branch",
        "merge branch",
    ]

    def create_branch():
        pass

    def change_branch():
        pass

    def delete_branch():
        pass

    def merge_branch():
        types_of_merges = ["fast forward", "three way merge"]
        # three way merge: could happen if we create a commit on the main branch after creating another branch
        # if the changes were made in different files, the git is good to go.
        # but if they were made in the same file, git will take both of the changes and put them in a result.
        # but instead if the changes were made on the same part in the same file, git won't know how to merge those changes, and the attempt will result in a merge conflict
        pass


def config_git_user(user_email, user_name):
    # first let's set up our account into git config to let it know who is making the changes
    # ask the user's email, and username and then pass it into this
    git_user_email = subprocess.run(
        ["git", "config", "--global", "user.email", user_email],
        capture_output=True,
        text=True,
    )
    git_user_name = subprocess.run(
        ["git", "config", "--global", "user.name", user_name],
        capture_output=True,
        text=True,
    )
    git_account = {git_user_email, git_user_name}
    print(git_account)


def initialize_repo(repo_name, branch_name="main"):
    # then let's initialize a repo (an empty one or existing one)
    gitRepo = subprocess.run(["git", "init"], capture_output=True, text=True)
    print(gitRepo)


# know the difference between local and remote workflows areas


def workflows(workflow_tree, staged, committed, branch_name="main"):
    # starting with the local workflow area
    # there are three working areas in git
    # 1. the working tree (which consists of untracked files, if not commited before)
    # demo data:
    #   1.1 create a file called my_first_file.py `through running [ni my_first_file.py] in the terminal`
    #   1.2 write this into it `This is the content of my first file.`

    # we have a check here if the change we made is wrong or we want to undo it before it's staged, we can do so using the command:
    reverse_options = ["checkout", "restore"]
    checkoutResult = subprocess.run(
        ["git", "checkout or restore (from reverse_options)", "filename"],
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


def diff(branch_name="main"):
    # Now first check the changes between files (using diff)'
    diffChanges = subprocess.run(
        ["git", "diff", "file_name"], capture_output=True, text=True
    )
    print(diffChanges)


# Now that's some of the basics of git'.


# for a tracked file (a file that's been commited before we can skip the staging stage if we just want to commit all of it)
# but this won't work for a new created file since that's untracked, and this will only work for a file that's been commited before
# to do that we add the `a-flag` when commiting, 'subprocess.run(["git", "commit", "-a", "-m", "this is the change where i skipped staging"], text=True)'

# What if we want to revert it after we commited it, then we'd use the `subprocess.run(["git", "revert", "HEAD (the latest commit)"], text=True)

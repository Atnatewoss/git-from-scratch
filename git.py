import subprocess

# Pre-requisite: make sure you have git installed

# first let's initialize a repo (an empty one or existing one)
gitRepo = subprocess.run(["git", "init"], capture_output=True, text=True)
print(gitRepo)

# set up our account into git config to let it know who is making the changes
# ask the user's email, and username and then pass it into this
gitAccount = subprocess.run(
    ["git", "config", "--global", "user.email", "your-email"],
    capture_output=True,
    text=True,
)
print(gitAccount)

# know the difference between local and remote workflows areas

# starting with the local workflow area
# there are three working areas in git
# 1. the working tree (which consists of untracked files, if not commited before)
# demo data:
#   1.1 create a file called my_first_file.py `through running [ni my_first_file.py] in the terminal`
#   1.2 write this into it `This is the content of my first file.`

# 2. the staging area (to have git recognize our change/s and start tracking it we need to add it to the staging area)
stagingResult = subprocess.run(
    ["git", "add", "file-names (in our case the my_first_file.py)"],
    capture_output=True,
    text=True,
)
print(stagingResult)

# 3. the commit change (now that git is tracking our changes and the repo is initialized and the changes we make can be identified back to us because it's configured, now have all the changes into one consistent copy showing )
commitResult = subprocess.run(
    ["git", "commit", "-m", "this is my first commit"], capture_output=True, text=True
)
print(commitResult)

# now let's make a change to our file by adding a second line
# add a second line in my_first_file.py, "This is the second content of my first file" and then stash and commit, like we did earlier.
# 1. running `subprocess.run(["git", "add", "my_first_file.py"], text=True)` -> (adding the untracked to the stash)
# 2. run `subprocess.run(["git", "commit", "-m", "add a second line"], text=True)`

# any time you want to check the tracked and untracked changes you can using `git status`
# and if you want to see your commit history, you can also do that by running `git log`

# Now first check the changes between files (using diff)'
diffChanges = subprocess.run(
    ["git", "diff", "file_name"], capture_output=True, text=True
)
print(diffChanges)

# Now that's some of the basics of git'.


# for a tracked file (a file that's been commited before we can skip the stashing stage if we just want to commit all of it)
# but this won't work for a new created file since that's untracked, and this will only work for a file that's been commited before
# to do that we add the `a-flag` when commiting, 'subprocess.run(["git", "commit", "-a", "-m", "this is the change where i skipped stashing"], text=True)'

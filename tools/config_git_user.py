import subprocess


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

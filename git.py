from git_tools import config_git_user, diff, initialize_repo, workflows


class Git:
    workflow_tree = True
    staged = True
    committed = True

    # user config info
    user_email = "user_email"
    user_name = "user_name"

    # repo name
    repo_name = "new repo"

    # branch name
    branch_name = "main"

    config_git_user = config_git_user(user_email, user_name)
    initialize_repo = initialize_repo(repo_name, branch_name="main")
    workflows = workflows(
        workflow_tree=True, staged=True, committed=True, branch_name="main"
    )
    diff = diff(branch_name="main")
    # branches = branches()

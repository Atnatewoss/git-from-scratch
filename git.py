from git_tools.py import branches, config_git_user, diff, initialize_repo, workflows


class Git:
    workflow_tree = True
    staged = True
    committed = True

    # user config info
    user_email = "user_email"
    user_name = "user_name"

    # repo name
    repo_name = "new repo"

    config_git_user = config_git_user(user_email, user_name)
    initialize_repo = initialize_repo(repo_name)
    workflows = workflows(workflow_tree=True, staged=True, committed=True)
    diff = diff()
    branches = branches()

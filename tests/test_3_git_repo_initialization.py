from git_tools import initialize_repo


class Git:
    ### --- SETUP INPUTS --- ###

    # branch workflow setup
    default_branch = "main"
    list_of_branches = [default_branch]
    current_branch = default_branch

    # new branch
    new_branch = "new branch"

    if not new_branch:
        current_branch = default_branch

    current_branch = new_branch

    # C) repo name
    repo_name = "matts_robot_arm_script"

    # ### --- EXECUTE FUNCTION TOOLS --- ###
    initialize_repo = initialize_repo(repo_name, branch_name=current_branch)

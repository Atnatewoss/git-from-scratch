from git_tools import diff


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

    # diff setup
    old_file = "old file.py, for now"
    new_file = "new file.py, for now"

    # ### --- EXECUTE FUNCTION TOOLS --- ###
    diff = diff(old_file, new_file, branch_name=current_branch)

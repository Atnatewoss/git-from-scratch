from tools import manage_branch_workflow


class Git:
    ### --- SETUP INPUTS --- ###

    # branch workflow setup
    default_branch = "main"
    list_of_branches = [default_branch]
    current_branch = default_branch

    # new branch
    new_branch = "my branch"

    if not new_branch:
        current_branch = default_branch

    current_branch = new_branch

    # ### --- EXECUTE FUNCTION TOOLS --- ###
    # # what tasks we would like git to perform
    # create, delete, change, merge
    action = "create"
    manage_branch_workflow = manage_branch_workflow(
        default_branch, list_of_branches, current_branch, new_branch, action
    )

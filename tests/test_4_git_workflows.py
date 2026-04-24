from tools import git_workflows


class Git:
    ### --- SETUP INPUTS --- ###
    # A) workflow process management
    workflow_tree = True
    staged = True
    committed = True

    # branch workflow setup
    default_branch = "main"
    list_of_branches = [default_branch]
    current_branch = default_branch

    # new branch
    new_branch = "new branch"

    if not new_branch:
        current_branch = default_branch

    current_branch = new_branch

    # ### --- EXECUTE FUNCTION TOOLS --- ###
    git_workflows = git_workflows(
        workflow_tree=workflow_tree,
        staged=staged,
        committed=committed,
        branch_name=current_branch,
    )

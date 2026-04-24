from git_config import (
    action,
    committed,
    current_branch,
    default_branch,
    list_of_branches,
    new_branch,
    new_file,
    old_file,
    repo_name,
    staged,
    user_email,
    user_name,
    workflow_tree,
)
from git_tools import (
    config_git_user,
    diff,
    git_workflows,
    initialize_repo,
    manage_branch_workflow,
)


class Git:
    ### --- EXECUTE FUNCTION TOOLS --- ###
    manage_branch_workflow = manage_branch_workflow(
        default_branch, list_of_branches, current_branch, new_branch, action
    )
    config_git_user = config_git_user(user_email, user_name)
    initialize_repo = initialize_repo(repo_name, branch_name=current_branch)
    git_workflows = git_workflows(
        workflow_tree=workflow_tree,
        staged=staged,
        committed=committed,
        branch_name=current_branch,
    )
    diff = diff(old_file, new_file, branch_name=current_branch)

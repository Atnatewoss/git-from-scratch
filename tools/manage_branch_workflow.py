def manage_branch_workflow(
    default_branch, list_of_branches, current_branch, new_branch, action
):

    allowed_actions = [
        "create branch",  ## from the parameter passed in, needs a branch_name [parameter]
        "delete branch",  ## from the list_of_branches, needs a branch_name [parameter]
        "change branch",  ## from the list_of_branches, needs a branch_name [parameter]
        "merge branch",  ## from the list_of_branches, needs the current_branch, and a branch_name [parameter]
    ]

    # triggered when a branch_name is passed and action is create
    def create_branch(new_branch):
        list_of_branches.append(new_branch)
        return new_branch

    # triggered when a branch_name is passed and action is delete
    def delete_branch(new_branch):
        branch_to_be_deleted = new_branch
        list_of_branches.remove(new_branch)
        return branch_to_be_deleted

    # triggered when a branch_name is passed and action is change
    def change_branch(new_branch):
        current_branch = new_branch
        return current_branch

    def merge_branch():
        merge_conflict = False
        types_of_merges = ["fast forward", "three way merge"]
        # three way merge: could happen if we create a commit on the main branch after creating another branch
        # if the changes were made in different files, the git is good to go.
        # but if they were made in the same file, git will take both of the changes and put them in a result.
        # but instead if the changes were made on the same part in the same file, git won't know how to merge those changes, and the attempt will result in a merge conflict
        pass

        if merge_conflict:
            pass

    allowed_actions_flag = True  ## the flag that controls access to perform the allowed_actions, by first checking if the inputs/parameters they need to perform their actions is provided

    if (
        not new_branch or not new_branch.strip()
    ):  ## Catches None, empty string "", and empty collections || .strip() Catches "   " as empty
        allowed_actions_flag = False

    if allowed_actions_flag:
        # call the functions, by first perfoming the mapping from the action to the functions.
        function_mapping = {
            "create": create_branch,
            "delete": delete_branch,
            "change": change_branch,
            "merge": merge_branch,
        }

        action_func = action.lower()
        if action in function_mapping:
            function_mapping[action_func](new_branch)
        else:
            response = "This action is not supported! Please try one of the following: create, delete, change, merge"
            print(response)
            return response

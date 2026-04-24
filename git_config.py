### --- SETUP INPUTS --- ###
# A) workflow process management
workflow_tree = True
staged = True
committed = True

# branch workflow setup
default_branch = "main"
list_of_branches = [default_branch]

# new branch
new_branch = "new branch"

if not new_branch:
    current_branch = default_branch

current_branch = new_branch

# diff setup
old_file = "old file.py, for now"
new_file = "new file.py, for now"

# B) user config info
user_email = "user_email"
user_name = "user_name"

# C) repo name
repo_name = "new repo"

# D) list all of the commmands used in the tools here, to track them as a check list
list_of_commands = []

### --- EXECUTE FUNCTION TOOLS --- ###
# what tasks we would like git to perform
# create, delete, change, merge
action = ""

import subprocess


def diff(old_file, new_file, branch_name):
    # demo check between the two file
    print(old_file, new_file)
    # Now first check the changes between files (using diff)'
    diffChanges = subprocess.run(
        ["git", "diff", "file_name"], capture_output=True, text=True
    )
    print(diffChanges)
    return diffChanges


# Now that's some of the basics of git'.


# for a tracked file (a file that's been commited before we can skip the staging stage if we just want to commit all of it)
# but this won't work for a new created file since that's untracked, and this will only work for a file that's been commited before
# to do that we add the `a-flag` when commiting, 'subprocess.run(["git", "commit", "-a", "-m", "this is the change where i skipped staging"], text=True)'

# What if we want to revert it after we commited it, then we'd use the `subprocess.run(["git", "revert", "HEAD (the latest commit)"], text=True)

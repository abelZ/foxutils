import os


# list files or folders under @path
# @path the path to list
# @postfixs the file post fixs filter, exp ['.mp4', '.ts']
# @recursive if the list should execute recursive
# @needFolder if the function should return files or folders
def listfiles(path, postfixs=[], recursive=True, needFolder=False):
    filtered = []
    try:
        for entry in os.listdir(path):
            if entry[0] == '.':
                continue

            full_path = os.path.join(path, entry)
            if needFolder:
                if os.path.isdir(full_path):
                    filtered.append(full_path)
                    if recursive:
                        filtered += listfiles(full_path, postfixs, recursive, needFolder)
            else:
                if os.path.isfile(full_path):
                    if not postfixs or os.path.splitext(full_path)[-1] in postfixs:
                        filtered.append(full_path)
                else:
                    if recursive:
                        filtered += listfiles(full_path, postfixs)
    except Exception as e:
        print(e)

    return filtered

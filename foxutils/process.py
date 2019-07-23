import psutil

# return if @pid exist and process name match the @name
def pid_match_name(pid, name):
    if psutil.pid_exists(pid):
        process = psutil.Process(pid)
        with process.oneshot():
            if process.name() == name:
                return True
    return False

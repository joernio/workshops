import subprocess

def ls_files_directory(directory):
    """
    Runs 'ls' command with '-1' option to print one file per line.
    Returns a list of all files in the specified directory.
    """
    output = subprocess.check_output(['ls', '-1', directory]).decode('utf-8')
    return [line.strip() for line in output.splitlines()]

def ls_files_directory_popen(directory):
    """
    Uses Popen to run 'ls' command and capture its output.
    Returns a list of all files in the specified directory.
    """
    with subprocess.Popen(['ls', '-1', directory], stdout=subprocess.PIPE) as p:
        output = p.stdout.read().decode('utf-8')
    return [line.strip() for line in output.splitlines()]

def ls_files_directory_check_call(directory):
    """
    Uses check_call to run 'ls' command and capture its output.
    Returns a list of all files in the specified directory.
    """
    output = subprocess.check_output(['ls', '-1', directory]).decode('utf-8')
    return [line.strip() for line in output.splitlines()]

def ls_files_directory_communicate(directory):
    """
    Uses communicate method to run 'ls' command and capture its output.
    Returns a list of all files in the specified directory.
    """
    with subprocess.Popen(['ls', '-1', directory], stdout=subprocess.PIPE) as p:
        output, _ = p.communicate()
    return [line.strip() for line in output.decode('utf-8').splitlines()]

def ls_files_directory_check_output(directory):
    """
    Uses check_output to run 'ls' command and capture its output.
    Returns a list of all files in the specified directory.
    """
    output = subprocess.check_output(['ls', '-1', directory]).decode('utf-8')
    return [line.strip() for line in output.splitlines()]



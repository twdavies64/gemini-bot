import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(abs_working_dir, file_path))
        if os.path.commonpath([abs_working_dir, target_file]) != abs_working_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", target_file]
        if args:
            command.extend(args)
        comproc = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=abs_working_dir)
        output = []
        if comproc.returncode != 0:
            output.append(f'Process exited with code {comproc.returncode}')
        if not comproc.stdout and not comproc.stderr:
            output.append(f'No output produced')
        if comproc.stdout: 
            output.append(f'STDOUT: {comproc.stdout}')
        if comproc.stderr:
            output.append(f'STDERR: {comproc.stderr}')
        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"
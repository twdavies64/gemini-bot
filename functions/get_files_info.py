import os


def get_files_info(working_directory, directory="."):
    try:
        abs_working_dir = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_working_dir, directory))
        if os.path.commonpath([abs_working_dir, target_dir]) != abs_working_dir:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        content = os.listdir(target_dir)
        result = []
        for i in content:
            size = os.path.getsize(os.path.join(target_dir, i))
            is_dir = os.path.isdir(os.path.join(target_dir, i))
            result.append(f"- {i}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(result)

    except Exception as e:
        return f"Error: {e}"

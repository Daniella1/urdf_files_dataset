from pathlib import Path

def _get_files_with(dir, files):
    list_of_file_paths = []

    # Check that path exists
    if not Path(dir).exists():
        print(f"Warning, the path {dir} doesn't exist.")
        return list_of_file_paths

    for path in Path(dir).rglob(files):
        list_of_file_paths.append(path)

    if len(list_of_file_paths) == 0:
        print(f"Warning, no files found when searching for {files} in {dir}.")
    return list_of_file_paths
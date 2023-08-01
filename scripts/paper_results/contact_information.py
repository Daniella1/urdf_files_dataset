from helper_functions import _get_files_with

dir = "urdf_files"
urdf_files = _get_files_with(dir,"*.urdf")

words_to_count = {'author': 0,'@': 0,'.com': 0}

for urdf_file in urdf_files:
    with open(urdf_file) as f:
        urdf = f.read()
    for word in words_to_count:
        if word in urdf:
            words_to_count[word] += 1

print(words_to_count)


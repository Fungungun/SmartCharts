import os
from pathlib import Path



def search_all_files(directory):
    dirpath = Path(directory)
    assert(dirpath.is_dir())

    file_list = []

    for x in dirpath.iterdir():
        if x.is_file() and x.suffix == ".pyc":
            file_list.append(x)
            # pass
        elif x.is_dir():
            file_list.extend(search_all_files(x))
    
    return file_list


decompiled_lib_folder = Path("C:\\Users\\chenghuanliu\\Desktop\\Projects\\SmartCharts\\smart_chart_d")
all_pyc_files = search_all_files(decompiled_lib_folder)

import lzma, base64

for filepath in all_pyc_files:
    d_filepath = str(filepath.parent) + "/" + filepath.name.split(".")[0] + "_d.py"
    py_filepath = str(filepath.parent) + "/" + filepath.name.split(".")[0] + ".py"

    os_command = f"uncompyle6 -o {d_filepath} {filepath}"
    os.system(os_command)

    fr = open(d_filepath, "r")
    fw = open(py_filepath, "w")

    for line in fr:
        if line.startswith("exec"):
            line = line.split("(")
            compressed_content = line[3].strip(")")[2:-1].encode('ascii')
            # print(compressed_content)
            decompressed_content = lzma.decompress(base64.b64decode(compressed_content))
            print(decompressed_content)
            
            exit(0)
    



    

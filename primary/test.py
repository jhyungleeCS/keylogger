


def savefile(keylog):
    file_name = "keylog.txt"
    count = 0
    while os.path.exists(file_name):
        count += 1
        file_name = f"keylog{count}.txt"
    
    file_path_keylog = os.path.join(os.path.expanduser("~/Desktop"), file_name)


    # Open the file for writing
    with open(file_path_keylog, "w") as f:
        # Write each element of the list to a new line in the file
        for item in keylog:
            f.write(str(item)+ ", ")
    
    keylog_str = [str(item) for item in keylog]
    

    print("File saved to", file_path_keylog)
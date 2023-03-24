from loggermain import keylogger
import os 

def savefile(keylog):
    count = 0
    file_name = "keylog.txt"
    while os.path.exists(file_name):
        count += 1
        file_name = f"keylog{count}.txt"
    file_path_keylog = os.path.join(os.path.expanduser("~/Desktop"), file_name)
    with open(file_path_keylog, "w") as f:
        for item in keylog:
            f.write(str(item) + ", ")
    print("File saved to", file_path_keylog)



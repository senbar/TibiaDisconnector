import subprocess
import time
import keyboard
import sys


def disconnect ():
    pgrep= subprocess.run("pgrep Tibia", shell=True, stdout= subprocess.PIPE)
    tibiaId= int(pgrep.stdout)

    p = subprocess.Popen(' sudo gdb -p ' + str(tibiaId)+ ' --eval-command="call close(5u)"'
                            , stdin=subprocess.PIPE, shell=True)

    time.sleep(5)
    p.kill()
    return(0)

def listen (hotkey = "ctrl + F"):
    print("Listening on hotkey ", hotkey)

    keyboard.add_hotkey(hotkey, disconnect)
    keyboard.add_hotkey('ctrl + escape', lambda: sys.exit(0))

    keyboard.wait('esc')


if __name__ == '__main__':
    hotkey= str(input('Give hotkey for disconnecting: '))

    if hotkey:
        listen(hotkey)
    else:
        listen()


import subprocess
import time
def disconnect ():
    pgrep= subprocess.run("pgrep Tibia", shell=True, stdout= subprocess.PIPE)
    tibiaId= int(pgrep.stdout)

    p = subprocess.Popen(' sudo gdb -p ' + str(tibiaId)+ ' --eval-command="call close(5u)"'
                            , stdin=subprocess.PIPE, shell=True)

    time.sleep(5)
    p.kill()
    return(0)


if __name__ == '__main__':
    disconnect()


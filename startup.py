import os
from getpass import getuser

STARTUP_PATH = os.path.abspath(rf'C:\Users\{ getuser() }\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')
    
def add_to_startup(file=None):

    if file is None:
        return None
    elif not os.path.isabs(file):
        file = os.path.abspath(file)

    batch_file, _ = os.path.splitext(os.path.basename(file))
    batch_file += '.bat'

    batch_file = os.path.join(STARTUP_PATH, batch_file)

    with open(batch_file, 'w') as bat:
        bat.write(f'@echo off\npython { file } %*\npause')


def remove_from_startup(file):

    if not os.path.isabs(file):
        file = os.path.abspath(file)

    batch_file, _ = os.path.splitext(os.path.basename(file))
    batch_file += '.bat'

    batch_file = os.path.join(STARTUP_PATH, batch_file)

    if os.path.exists(batch_file):
        os.remove(batch_file)



if __name__ == '__main__':
    add_to_startup(__file__)
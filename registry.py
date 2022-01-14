import winreg

from logger import log
import settings

REG_PATH = r'Control Panel\Desktop'

def set_reg(name, value):

    logger = log(name=__name__, filename=settings.LOGS)

    try:
        winreg.CreateKey(winreg.HKEY_CURRENT_USER, REG_PATH)
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0, 
                                       winreg.KEY_WRITE)
        winreg.SetValueEx(registry_key, name, 0, winreg.REG_SZ, value)
        winreg.CloseKey(registry_key)
        logger.debug(f'Set Registry : { name } : { value }')
        return True
    except WindowsError:
        logger.error(f'Failed to set Registry : { name } : { value }')
        return False

def get_reg(name):

    logger = log(name=__name__, filename=settings.LOGS)

    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, REG_PATH, 0,
                                       winreg.KEY_READ)
        value, _ = winreg.QueryValueEx(registry_key, name)
        winreg.CloseKey(registry_key)
        logger.debug(f'Get Registry : { name } : { value }')
        return value
    except WindowsError:
        logger.error(f'Failed to get Registry : { name }')
        return None


if __name__ == '__main__':
    print(get_reg('WallPaper'))
    set_reg('WallPaper', r"C:\Users\sidhu\Pictures\PyWallpapers\Wallpapers\0b7b6681ff82b03adcc7b8bcc05b655e.jpg")        
    print(get_reg('WallPaper'))

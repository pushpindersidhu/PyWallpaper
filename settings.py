import os
from getpass import getuser

from registry import REG_PATH

# settings

USER = getuser()

RUN_AT_STARTUP = False

DEFAULT_TIME = 60

PAGE = 1

REG_PATH = r'Computer\HKEY_CURRENT_USER\Control Panel\Desktop'

REG_NAME = 'WallPaper'

# system paths

CACHED_WALLPAPER = os.path.abspath(rf'C:\Users\{ USER }\AppData\Roaming\Microsoft\Windows\Themes\CachedFiles')

STARTUP_PATH = os.path.abspath(rf'C:\Users\{ USER }\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup')

DOWNLOADS = os.path.abspath(rf'C:\Users\{ USER }\Downloads')

# paths

PY_WALLPAPERS_PATH = os.path.abspath(rf'C:\Users\{ USER }\Pictures\PyWallpapers')

WALLPAPERS_PATH = os.path.join(PY_WALLPAPERS_PATH, 'Wallpapers')

LOGS_PATH = os.path.join(PY_WALLPAPERS_PATH, 'logs')

PATHS = [PY_WALLPAPERS_PATH, WALLPAPERS_PATH, LOGS_PATH]

CONFIG = os.path.join(PY_WALLPAPERS_PATH, 'config.json')

LOGS = os.path.join(LOGS_PATH, 'logs.log')

SETUP_LOG = os.path.join(LOGS_PATH, 'setup.log')
SCRAPER_LOG = os.path.join(LOGS_PATH, 'scraper.log')
CONFIG_LOG = os.path.join(LOGS_PATH, 'config.log')

# websites

WEBSITES = {'windows_spotlight' : 'https://windows10spotlight.com/'}

HTML_PARSER = 'lxml'

DOWNLOAD_URL = 'https://windows10spotlight.com/wp-content/uploads/'

MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


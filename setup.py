import os
from config import Config
from logger import log
import settings
from startup import add_to_startup


for path in settings.PATHS:
    if not os.path.exists(path):
        os.mkdir(path)


logger = log(name=__name__, filename=settings.LOGS)

if settings.RUN_AT_STARTUP:
    try:
        add_to_startup(os.path.abspath('main.py'))
        logger.info('File added to startup.')
    except:
        logger.error('Failed to add to startup.')


config = Config()

config.set('setup', True)

if config.get('page') is None:
    config.set('page', settings.PAGE)

if config.get('time') is None:
    config.set('time', settings.DEFAULT_TIME)


wallpapers = []
for wallpaper in os.listdir(settings.WALLPAPERS_PATH):
    if os.path.splitext(wallpaper)[1] in ['.jpg', '.png']:
        wallpapers.append(wallpaper)
        logger.info(f'{ wallpaper } found.')
    else:
        logger.warning(f'{ wallpaper } is not a wallpaper.')


config.set('wallpapers', wallpapers)

config.save()

logger.info('Setup finished.')

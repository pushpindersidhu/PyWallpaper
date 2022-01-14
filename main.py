from config import Config
from logger import log
from scrape import Scraper
from wallpaper import Wallpaper
from connection import isConnected
import settings
import time


if __name__ == '__main__':

    logger = log(name=__name__, filename=settings.LOGS)

    config = Config()
    
    setup = config.get('setup')
    if setup is None:
        import setup
        config.refresh()

    page = config.get('page')
    sleep_time = config.get('time')
    logger.debug(f'page : { page }')

    scraper = Scraper(page)
    scraper.scrape()

    wallpaper = Wallpaper()

    while True:
        if isConnected():
            data = scraper.get_wallpaper_data()
            if data is None:
                filename = wallpaper.get_random_wallpaper()
            else:
                url = wallpaper.create_url(data)
            filename = wallpaper.download_wallpaper(url, data)
        else:
            filename = wallpaper.get_random_wallpaper()
        
        if filename is not None:
            wallpaper.set_wallpaper(filename)

        # time.sleep(1)

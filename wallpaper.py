import ctypes
import os
from config import Config
from download import download
from logger import log
import settings
import random
from registry import set_reg


SPI_SETDESKWALLPAPER = 20

class Wallpaper:

    def __init__(self) -> None:
        self.logger = log(name=__name__, filename=settings.LOGS)


    def set_wallpaper(self, wallpaper):
        wallpaper = os.path.join(settings.WALLPAPERS_PATH, wallpaper)
        if wallpaper is not None:
            self.logger.info(f'Wallpaper Set : { wallpaper }')
            ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, wallpaper, 0)
            set_reg(settings.REG_NAME, wallpaper)
        else:
            self.logger.warning(f'Failed to set Wallpaper : { wallpaper }')


    def create_url(self, wallpaper_data):
        if wallpaper_data is not None:
            url = f'{ settings.DOWNLOAD_URL }{ wallpaper_data.get("year") }/{ wallpaper_data.get("month") }/{ wallpaper_data.get("id") }.jpg'
            self.logger.debug(f'Url of wallpaper : { url }')
            return url
        else:
            self.logger.warning('Wallpaper data is None.')
            return None


    def download_wallpaper(self, url, data):
        filename = f"{ data.get('id') }.jpg"
        config = Config()
        if filename in config.get('wallpapers'):
            self.logger.info(f'{ filename } already exists.')
            return filename
        else:
            self.logger.info(f'Requesting { filename }')
            filename = download(url=url, filename=filename, save_to=settings.WALLPAPERS_PATH)
            return filename

    
    def get_random_wallpaper(self):
        config = Config()
        wallpapers = config.get('wallpapers')
        try:
            wallpaper = random.choice(wallpapers)
            self.logger.debug(f'Random Wallpaper : { wallpaper }')
        except IndexError:
            wallpaper = None
            self.logger.info(f'No wallpapers found.')
        return wallpaper
    

    def change_wallpaper_in_reg(self, path):
        reg_key = '"reg add "HKEY_CURRENT_USERControl PanelDesktop" /v Wallpaper /t REG_SZ     /f /d "'+path
        os.system(reg_key)
        os.system('RUNDLL32.EXE user32.dll', 'UpdatePerUserSystemParameters')
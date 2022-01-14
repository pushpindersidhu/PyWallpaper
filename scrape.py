from bs4 import BeautifulSoup
import requests
import settings
import logging
from config import Config
from logger import log

class Scraper:

    def __init__(self, page=1) -> None:
        
        self.page = page
        self.url = f'{ settings.WEBSITES.get("windows_spotlight") }page/{ page }'
        self.wallpaper_id_iter = iter([])

        self.logger = log(name=__name__, filename=settings.LOGS)


    def update(self, page):
        self.page = page
        self.url = f'{ settings.WEBSITES.get("windows_spotlight") }page/{ page }'
        self.logger.info(f'(page, url) : ({ page }, {self.url})')


    def get_source(self):
        try:
            self.logger.info(f'{ self.url }')
            with requests.get(self.url) as req:
                self.logger.info(f'{ self.url } response status code : { req.status_code }')
                return req.text
        except:
            self.logger.error(f'Failed to get { self.url }')
            return None
    
    def scrape(self):
        source = self.get_source()
        if source is None:
            self.logger.warning('Source is None.')
            return None
        soup = BeautifulSoup(source, settings.HTML_PARSER)
        self.logger.info(f'Scraping the source of page { self.page }.')
        id_matches = soup.find_all('img', class_='thumbnail wp-post-image')
        date_matches = soup.find_all('span', class_='date')
        self.logger.debug(f'Match Found (ids, dates) : { len(id_matches) }, { len(date_matches) }')
        wallpaper_ids = [wallpaper_id.get('alt') for wallpaper_id in id_matches]
        dates_posted = [date_posted.text.split('-') for date_posted in date_matches]

        wallpaper_data_list = []

        for index, id in enumerate(wallpaper_ids):
            wallpaper_data = {}
            wallpaper_data['id'] = id
            month = settings.MONTHS.index(dates_posted[index][1]) + 1
            wallpaper_data['month'] = str(month) if len(str(month)) > 1 else ('0' + str(month))
            wallpaper_data['year'] = dates_posted[index][2]
            wallpaper_data_list.append(wallpaper_data)

        for wallpaper_data in wallpaper_data_list:
            self.logger.debug(f'Scraped data item : { wallpaper_data }')

        self.wallpaper_id_iter = iter(wallpaper_data_list)
        soup.clear()
        del wallpaper_ids, source, wallpaper_data_list
    
    def get_wallpaper_data(self):
        try:
            wallpaper_data = next(self.wallpaper_id_iter)
            self.logger.debug(f'Returned Wallpaper data : { wallpaper_data }')
            return wallpaper_data
        except StopIteration:
            self.logger.warning(f'No next value in iterator.')
            config = Config()
            self.update(self.page + 1)
            config.set('page', self.page)
            config.save()
            self.scrape()
            wallpaper_data = next(self.wallpaper_id_iter)
            return wallpaper_data
        

if __name__ == '__main__':
    scraper = Scraper()
    scraper.scrape()
    for i in range(10):
        scraper.get_wallpaper_data()

import requests
import uuid
import os
from getpass import getuser
from logger import log
import settings

def download(url, filename=None, save_to=None):

    logger = log(name=__name__, filename=settings.LOGS)

    DOWNLOADS = os.path.abspath(rf'C:\Users\{ getuser() }\Downloads')
    
    try:
        with requests.get(url, stream=True) as req:

            logger.info(f'Downloading { filename }...')

            if filename is None:
                filename = str(uuid.uuid4().hex) + '.jpg'

            if save_to is None:
                save_to = DOWNLOADS
            
            downloaded = 0
            with open(os.path.join(save_to, filename), 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += 8192

            downloaded /= 1048576
            logger.info(f'{ filename } downloaded ({ downloaded }MB).')
            logger.info(f'{ filename } saved to { save_to }.')

            return filename

    except Exception as e:
        logger.info(f'Download failed ({ filename }).')
        return None



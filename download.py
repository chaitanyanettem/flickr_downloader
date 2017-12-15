import requests
from celery import Celery
import logging
from configobj import ConfigObj
import uuid
config = ConfigObj('config.ini')

app = Celery('download', backend='redis://localhost', broker='redis://localhost')


@app.task()
def kubric(url, filename):
    image = requests.get(url+"=s800", stream=True)
    with open(filename, 'wb') as _file:
        for chunk in image:
            _file.write(chunk)


@app.task(rate_limit='800/h')
def flickr(page=1, per_page=500, search_term="india"):
    final_url = config['flickr']['url'].format(sort="interestingness-desc",
                                               content_type=6,extras="url_o",
                                               per_page=per_page,
                                               page=page,
                                               text=search_term,
                                               method="flickr.photos.search",
                                               api_key=config['flickr']['key'],
                                               format="json",
                                               privacy_filter=1)
    logging.info("Images from flickr page %s ", page)
    response = requests.get(final_url)
    images = [{'source_url': x.get('url_o'),
               'id': x.get('id')} for x in response.json()['photos']['photo']]
    if response.json()['photos']['pages'] > page and page < 5:
        flickr.delay(page=page+1, per_page=500, search_term=search_term)
    get_asset_files.delay(images, search_term)


@app.task()
def get_asset_files(assets, search_term):
    for image in assets:
        url = image["source_url"]
        if url:
            logging.info(url)
            ifile = requests.get(image['source_url'], stream=True)
            with open("download/" + search_term + "/" + str(str(uuid.uuid4()) + image['id']), 'wb') as _file:
                for chunk in ifile:
                    _file.write(chunk)
        else:
            logging.error("no url. Continuing")


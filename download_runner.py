import download
import os
import logging
from configobj import ConfigObj
config = ConfigObj('config.ini')


def start_flickr(phrases):
    if not config['flickr']['path'].endswith('/'):
        logging.error("make sure path ends with '/'")
    if not os.path.exists(config['flickr']['path']):
        os.makedirs(config['flickr']['path'])
    for phrase in phrases:
        if not os.path.exists(config['flickr']['path'] + phrase):
            os.makedirs(config['flickr']['path'] + phrase)
        download.flickr.delay(1, 500, phrase)


def get_phrases():
    phrases = []
    with open("phrase_list.txt") as phrase_list:
        for phrase in phrase_list:
                phrases.append(phrase.strip())
    return phrases


if __name__ == "__main__":
    start_flickr(get_phrases())

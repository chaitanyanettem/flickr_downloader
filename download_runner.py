import download
import os


def start_flickr(phrases):
    for phrase in phrases:
        if not os.path.exists(phrase):
            os.makedirs(phrase)
        download.flickr.delay(1, 500, phrase)


def get_phrases():
    phrases = []
    with open("phrase_list.txt") as phrase_list:
        for phrase in phrase_list:
                phrases.append(phrase.strip())
    return phrases


if __name__ == "__main__":
    start_flickr(get_phrases())

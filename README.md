This is an implementation of an image downloader which uses Flickr's API and Celery to download images in parallel.

## Installation

##### Packages

- Install the python requirements: `pip install -r requirements.txt`
- Install redis (which acts as Celery's broker and backend): `sudo apt install redis-server`

##### Create `config.ini`

Create a file called config.ini and add the following to it:

```ini
[flickr]
url = 'https://api.flickr.com/services/rest?sort={sort}&parse_tags=1&content_type={content_type}&extras={extras}&per_page={per_page}&page={page}&text={text}&method={method}&api_key={api_key}&format={format}&nojsoncallback=1&privacy_filter={privacy_filter}'
key = ''
```

You have to generate a Flickr API Key and place it in this file.

## Usage

`phrase_list.txt` is the list of phrases for which images will be downloaded. Each phrase must be placed on a new line. It is pre-populated with dummy values.

##### Running the downloader

- To start the celery workers run - `celery worker -A download -l INFO --concurrency 4`. This will start 4 parallel worker threads which will wait for download tasks to start.
- In another terminal, start issuing tasks to the worker threads with `python download_runner.py`

That's it :)

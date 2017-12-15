### Installation

- Install the python requirements: `pip install -r requirements.txt`
- Install redis: `sudo apt install redis-server`

### Usage

- You have to generate a Flickr API Key and place it in `config.ini`.
- Take a look at `phrase_list.txt`. This is the list of phrases for which images will be downloaded. Each phrase must be placed in a new line.

Noe, from one terminal in order to start the celery workers up run - 

`celery worker -A download -l INFO --concurrency 4`

After you've done this, in another terminal, start issuing tasks to the worker threads with

`python download_runner.py`

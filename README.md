# Overview

I like all types music, and lately I've been enjoying using mixcloud to find new music. This little webapp searches your last.fm account to get your top artists, then searches the mixcloud.com api for mixes related to those top artists. 

You can also do an artist search, which will find mixes for that artist, and also offer up related artists using last.fm.

# installation notes

**Note** *You'll need [Redis](http://redis.io/) to run this app. Redis is used to cache API requests.

After cloning the repo and `cd`ing into the main directory:

1. Get virtualenv
2. Install [Redis](http://redis.io/).
3. Make virtual environment

        mkdir env && virtualenv env
        
4. In env, install pip requirements

        pip install -r requirements.txt

5. Last.fm requires an api key for some reason. Set the following
environment variable up:

        export last_fm_api_key=<your api key>

6. Set up the development app with:

        python setup.py develop

7. Run the app.

        pserve development.ini


# running locally

    pserve development.ini

# updating app after changing configurations

    python setup.py develop
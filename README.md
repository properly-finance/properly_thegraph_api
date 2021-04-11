properly api service
====================

Server for realization aggregation function that absent in the graph operators

```
https://whispering-beyond-26434.herokuapp.com
```


Technology
----------

* Docker
* Python 3.9
* Flask
* Gunicorn
* pytest
* Heroku


Common features
----------------

* Docker (and docker-compose) containerized
* Automated control start and down through 'make'
* Flask  - Simple and fast popular framework
* ipdb for trace when debugging in dev mode
* Gunicorn starting script for production



### Install Docker

https://docs.docker.com/installation/

### Install Docker Compose

http://docs.docker.com/compose/install/

### Install the app's


```bash
make compose build
```

then

```bash
make compose bootstrap
```

then go to shell to run test

```bash
make compose shell test
workon thegraph_api
pytest -v tests

```

### Deploy 


```bash
heroku login --interactive
git push heroku master

```

And thats is all!! :)
FROM python:3.9-slim-buster
MAINTAINER Den Elston "elstton@yahoo.com"

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    g++ \
    libpq-dev \
    git \
&& pip install virtualenvwrapper poetry \
&& rm -rf /var/lib/apt/lists/*

RUN touch ~/.bashrc \
&& echo " " >> ~/.bashrc \
&& echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
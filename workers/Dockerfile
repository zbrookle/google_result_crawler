FROM python:3.7

ENV CHROME_VERSION=88.0.4324.96-1
ENV PIP_CHROME_VERSION=88.0.4324.96

RUN apt-get update 
RUN apt-get install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils

#download and install chrome
# In case of update, check for available versions here: https://www.ubuntuupdates.org/package/google_chrome/stable/main/base/google-chrome-stable
RUN wget http://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_${CHROME_VERSION}_amd64.deb
RUN dpkg -i google-chrome-stable_${CHROME_VERSION}_amd64.deb; apt-get -fy install

RUN pip install celery \
    sqlalchemy \
    psycopg2-binary \
    requests \
    beautifulsoup4 \
    selenium==3.141.0 \
    chromedriver-binary==${PIP_CHROME_VERSION} \
    kazoo

COPY project project

# ENTRYPOINT ["/project/entrypoint.sh"]
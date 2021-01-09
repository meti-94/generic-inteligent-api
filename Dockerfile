# invoke appropriate docker image
FROM huggingface/transformers-cpu
# install necessary utils
RUN apt update && \
 apt install -y vim && \
 apt-get install -y python3-pip && \
 apt install gcc && \
 pip3 install uwsgi 
# copy site files
copy ./web_service /site
# setup django env 
RUN pip3 install -r /site/requirements.txt
# place uwsgi config file
copy ./uwsgi.ini /etc/uwsgi/development.ini
copy ./RUN.sh /RUN.sh
RUN chmod +x /RUN.sh

WORKDIR /site

CMD [ "/RUN.sh" ]

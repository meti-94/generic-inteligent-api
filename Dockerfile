FROM huggingface/transformers-cpu
RUN apt update && \
 apt install -y vim && \
 apt-get install -y python3-pip && \
 apt install gcc && \
 pip3 install uwsgi 
copy ./web_service /site
RUN pip3 install -r /site/requirements.txt
copy ./uwsgi.ini /etc/uwsgi/development.ini
copy ./RUN.sh /RUN.sh
RUN chmod +x /RUN.sh

WORKDIR /site

CMD [ "/RUN.sh" ]

FROM python:3.6

ADD LogsGenerator.py /home/
ADD entrypoint.sh /home/entrypoint.sh
#ADD requirements.txt /home/requirements.txt

#RUN pip3 install -r /home/requirements.txt

RUN chmod +x /home/entrypoint.sh

ENTRYPOINT ["python", "/home/LogsGenerator.py"]
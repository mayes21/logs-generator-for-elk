## LOGS GENERATOR 4 ELK

Python script to generate logs for ELK (Elasticsearch - Logstash - Kibana) stack testing purpose.

To launch the script :
```
python LogsGenerator.py -p [logs_path]
```
_works fine with python versions 2.7 and 3.6_

To download logstash docker image (_version : 7.0.0_) :
```
docker pull docker.elastic.co/logstash/logstash:7.0.0
```

To launch logstash and install `logstash-output-stdout` plugin on docker
```
docker run --name logstash --rm -it -v ~/perso/dev/logs-generator-for-elk/elk/logstash/config/logstash.yml:/usr/share/logstash/config/logstash.yml -v ~/perso/dev/logs-generator-for-elk/elk/logstash/pipeline:/usr/share/logstash/pipeline -v ~/Bureau/logFile.log:/home/logFile.log docker.elastic.co/logstash/logstash:7.0.0 sh -c "logstash-plugin install --no-verify logstash-output-stdout; /usr/local/bin/docker-entrypoint
```
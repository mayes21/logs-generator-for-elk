## LOGS GENERATOR 4 ELK

Python script to generate logs for ELK (Elasticsearch - Logstash - Kibana) stack testing purpose.

> To launch the script :
```
python LogsGenerator.py -p [logs_path]
```
_works fine with python versions 2.7 and 3.6._

> To download logstash docker image (_version : 7.0.0_) :
```
docker pull docker.elastic.co/logstash/logstash:7.0.0
```

> To launch logstash and install `logstash-output-stdout` plugin on docker :
```
docker run --name logstash --rm -it -v ~/perso/dev/logs-generator-for-elk/elk/logstash/config/logstash.yml:/usr/share/logstash/config/logstash.yml -v ~/perso/dev/logs-generator-for-elk/elk/logstash/pipeline:/usr/share/logstash/pipeline -v ~/Bureau/logFile.log:/home/logFile.log docker.elastic.co/logstash/logstash:7.0.0 sh -c "logstash-plugin install --no-verify logstash-output-stdout; /usr/local/bin/docker-entrypoint
```

> Logstash output on stdout after applying the _grok filter_** :
```json
...
{
    "@timestamp" => 2019-04-17T09:27:50.247Z,
      "datetime" => "17-04-2019 11:04:20",
          "host" => "2ca5284f00b0",
          "path" => "/home/logFile.log",
      "loglevel" => "INFO",
       "message" => "Logging INFO Message",
      "@version" => "1"
}
...

```

> **The filter :
```
{ "message" => "%{DATESTAMP:datetime} %{LOGLEVEL:loglevel}%{SPACE}:%{SPACE}%{GREEDYDATA:message}" }
```

This is an example of how to use [RedisTimeSeries](https://oss.redislabs.com/redistimeseries/) and the integration with Prometheus and Grafana.

## Running the example

Start docker compose to start Redis, Prometheus and Grafana.
```bash
docker-compose up
```

Then setup virtual environment and run

```bash
python -m venv virtualenv
source virtualenv/bin/activate
pip install -r requirements.txt
python ProduceMessages.py
```

You can read more about this code in my blog https://ohad-israeli.github.io/time-series/
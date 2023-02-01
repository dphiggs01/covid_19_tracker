#!/usr/bin/env bash
PORT=9000
NUM_WORKERS=3
TIMEOUT=120
PIDFILE="gunicorn.pid"

if [ -d "/home/ubuntu/Applications/python_envs" ]; then
    source /home/ubuntu/Applications/python_envs/bin/activate
    PORT=80
fi


exec gunicorn covid19_app:app \
--workers $NUM_WORKERS \
--worker-class gevent \
--timeout $TIMEOUT \
--log-level=debug \
--reload-extra-file ./templates/index.html \
--reload-extra-file ./templates/date.html \
--reload-extra-file ./templates/covid19_state_county_zoom.html \
--reload-extra-file ./templates/covid19_state_table.html \
--reload-extra-file ./templates/covid19_state_county_table.html \
--bind=0.0.0.0:$PORT \
--pid=$PIDFILE

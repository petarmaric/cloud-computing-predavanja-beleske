#!/bin/bash -eu

NUM_CPUS=`nproc`
NUM_WORKERS=$((2 * $NUM_CPUS + 1))

gunicorn webapp.wsgi --workers=$NUM_WORKERS --bind 0.0.0.0:8000

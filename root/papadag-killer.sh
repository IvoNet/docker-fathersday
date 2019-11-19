#!/usr/bin/env bash

while true
do
    sleep 6
    PID=$(ps -ef|grep -v grep|grep python3|awk '{print $2}'|head)
    if [ ! -z ${PID} ]; then
        kill -9 $PID
    fi
done

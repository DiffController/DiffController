#!/bin/bash

# run_ryu.sh

# start docker
START_RYU_CONTAINER_CMD="sudo docker start 893cb3f47c7e"

# attach docker
ATTACH_RYU_CONTAINER_CMD="sudo docker attach 893cb3f47c7e"

# stop docker
STOP_RYU_CONTAINER_CMD="sudo docker stop 893cb3f47c7e"

function find_ip(){
    echo "ifconfig"
}

# trap for close ryu & docker
trap 'onCtrlC' INT
function onCtrlC () {
    echo 'Ctrl+C is captured'
    eval $STOP_RYU_CONTAINER_CMD
}

# run ryu controller
RUN_RYU_CMD="`find_ip` & ryu-manager ofctl_rest.py test.py rest_topology.py rest_conf_switch.py --verbose --observe-links "

# run container & exec ubuntu sh  
RUN_RYU_CONTROLLER="sudo docker exec -u root  -w /home/ryu/ryu/app -i ryu bash -c '$RUN_RYU_CMD'"

eval $START_RYU_CONTAINER_CMD

eval $RUN_RYU_CONTROLLER





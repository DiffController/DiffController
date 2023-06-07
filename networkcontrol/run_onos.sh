#!/bin/bash

function find_ip(){
    echo "ifconfig"
}

# trap for close ryu & docker
trap 'onCtrlC' INT
function onCtrlC () {
    echo 'Ctrl+C is captured'
    eval $STOP_ONOS_CONTAINER_CMD
}

# # start docker
START_ONOS_CONTAINER_CMD="sudo docker start 9b326c69d17f"

# # attach docker
ATTACH_ONOS_CONTAINER_CMD="sudo docker attach 9b326c69d17f"

# # stop docker
STOP_ONOS_CONTAINER_CMD="sudo docker stop 9b326c69d17f"

# run container & exec ubuntu sh  
RUN_ONOS_CONTROLLER="sudo docker exec -u root -i onos /bin/bash"

eval $START_ONOS_CONTAINER_CMD

eval $ATTACH_ONOS_CONTAINER_CMD
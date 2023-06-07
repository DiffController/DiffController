#!/bin/bash

# start docker
START_ODL_CONTAINER_CMD="sudo docker start b38a3763bb56"

# attach docker
ATTACH_ODL_CONTAINER_CMD="sudo docker attach b38a3763bb56"

# stop docker
STOP_ODL_CONTAINER_CMD="sudo docker stop b38a3763bb56"

# trap for close floodlight & docker
trap 'onCtrlC' INT
function onCtrlC () {
    echo "Waiting for OpenDaylight process to end"
    eval "sudo sleep 5"
    echo 'Ctrl+C is captured'
    eval $STOP_ODL_CONTAINER_CMD
}

# run OpenDaylight controller
RUN_ODL_CMD="ifconfig & ./karaf"

# run container & exec ubuntu sh  
RUN_ODL_CONTROLLER="sudo docker exec -u root -w /home/distribution-karaf-0.6.2-Carbon/bin -i odl_carbon bash -c '$RUN_ODL_CMD'"

eval $START_ODL_CONTAINER_CMD
eval $RUN_ODL_CONTROLLER

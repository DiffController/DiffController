#!/bin/bash

# start docker
START_FL_CONTAINER_CMD="sudo docker start aa8c183b92dc"

# attach docker
ATTACH_FL_CONTAINER_CMD="sudo docker attach aa8c183b92dc"

# stop docker
STOP_FL_CONTAINER_CMD="sudo docker stop aa8c183b92dc"

# trap for close floodlight & docker
trap 'onCtrlC' INT
function onCtrlC () {
    echo 'Ctrl+C is captured'
    eval $STOP_FL_CONTAINER_CMD
}

# run floodlight controller
RUN_FL_CMD="ifconfig & java -jar target/floodlight.jar"

# run container & exec ubuntu sh  
RUN_FL_CONTROLLER="sudo docker exec -w /home/floodlight-master -u root -i floodlight_node1 bash -c '$RUN_FL_CMD'"

eval $START_FL_CONTAINER_CMD
eval $RUN_FL_CONTROLLER

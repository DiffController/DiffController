# Controller Docker Startup

After finishing the docker build for the corresponding controller according to /DiffController/build, you can use the shell here to start the different controllers.

For example, you can use the following command to start the Ryu controller:
```
sudo ./run_ryu.sh
```

The other controllers are similar, as follows:
```
sudo ./run_floodlight.sh
sudo ./run_onos.sh
sudo ./run_odl.sh
```

The **CONTAINER ID** and **NAMES** used in shell needs to modified.

Start the controllers in the following oreder:
```python
 Ryu --> Floodlight --> ONOS --> OpenDaylight
```

## For OpenDaylight Controller
If we want to use OpenDaylight with REST APIs and OpenFlow, We need to install some features as follows in the OpenDaylight shell:
```
feature:install odl-restconf
feature:install odl-l2switch-switch-all
feature:install odl-openflowplugin-flow-services-ui  
feature:install odl-mdsal-apidocs
feature:install odl-dluxapps-applications
```
Please note that incorrect order of feature installation may result in OpenDaylight not running.

# Controller Docker Shutdown

For running Controllers, only needs to use **Ctrl + C** to exit Controllers.


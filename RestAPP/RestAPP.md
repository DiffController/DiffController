# REST APP implementation

We implement this module mainly based on the northbound interface APIs provided by different controllers.

For Ryu controller: [Ryu API Reference](https://ryu.readthedocs.io/en/latest/app/ofctl_rest.html)

For Floodlight controller: [Floodlight API Reference](https://floodlight.atlassian.net/wiki/spaces/floodlightcontroller/pages/1343539/Floodlight+REST+API)


For the ONOS controller, you first need to start the controller. You can see all the REST APIs in the following URL:
```
http://{controller ip}:{controller port}/onos/v1/docs/
ONOS default Username: onos
ONOS default Password: rocks
```

OpenDaylight controller also has a web page similar to ONOS, first you must also start OpenDaylight controller, then you can see that the OpenDaylight controller supports REST APIs in the following web page:

```
 http://{controller ip}:{controller port}/apidoc/explorer/index.html
 OpenDaylight default Username: admin
 OpenDaylight default Password: admin
```

## Info Collected
For each controller, **DiffController** collect the following information before and after strategy execution through REST APIs:
```
1.switch list in topology
2.switch port list
3.hosts in topology
4.links between swithes in topology
5.flow tables in all switches
6.group table in all switches
7.meter table in all switches
```


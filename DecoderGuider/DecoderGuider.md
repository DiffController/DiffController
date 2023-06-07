# Decoder Guider Implementation

Decoder of different controllers can be found in the following pages.

For Ryu controller: [Ryu OpenFlow Protocol Parser](https://github.com/faucetsdn/ryu/tree/master/ryu/ofproto)

For Floodlight controller: [Floodlight OpenFlowJ](https://mvnrepository.com/artifact/org.projectfloodlight/openflowj)

For ONOS controller: [ONOS OpenFlowJ](https://mvnrepository.com/artifact/org.onosproject/openflowj)

For OpenDaylight controller: [OpenDaylight OpenFlowJava](https://mvnrepository.com/artifact/org.opendaylight.openflowplugin.openflowjava/openflow-protocol-impl)

Based on the API provided by these Decoders, we use them to parse the OpenFlow message sequence, namely **of13_sequence.pcap**( Contains all types of OpenFlow Message that switch can send to the controller ) after the strategy execution.

According to the results of the different Decoders parse, a further guidance is given to the choice of strategy. In the process of strategy evolution, strategies that may lead to differences are more likely to be selected.

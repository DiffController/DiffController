# Topology Build

We use dot files as input to describe the network nodes in the topology, namely switches and hosts. An example of a dot file is as follows (**networktopo.dot**) :
```
graph networktopo {
    rankdir = LR;
    node [shape=circle] s1
    node [shape=circle] s2
    node [shape=circle] s3
    node [shape=circle] s4
    node [shape=circle] h1
    node [shape=circle] h2
    node [shape=circle] h3
    node [shape=circle] h4   
    s1 -- s2 ;
    s1 -- s3 ;
    s3 -- s4 ;
    s1 -- h1 ;
    s2 -- h2 ;
    s3 -- h3 ;
    s4 -- h4 ;
}
```
In the dot file, we define the switch as s<sub>i</sub> and the host as h<sub>i</sub>  ,further define the links between them.
Next, run buildSameTopo.py to get the custom topology python file (for different controllers) accepted by Mininet:
```
    python buildSameTopo.py
```
The different files represent the same topology, but the controller type is added to the node names (For example, ryu-s3, fl-s3, onos-s3, odl-s3) to prevent name conflicts.




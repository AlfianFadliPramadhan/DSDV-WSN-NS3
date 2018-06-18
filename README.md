# DSDV-WSN NS3
Destination-Sequenced Distance-Vector (DSDV) Routing Protocol simulation for Wireless Sensor Network in NS3

Minimum Requirements:
- NS-3.28
- NetAnim-3.108

Installation:
- Copy .cc and wscript to /ns-3.28/src/netanim/examples/
- Edit another 'wscript' in /ns-3.28/src/netanim/ with following line:
    module = bld.create_ns3_module ('netanim', ['internet', 'mobility', 'wimax', 'wifi', 'csma', 'lte', 'uan', 'lr-wpan', 'energy', 'wave', 'point-to-point-layout', 'dsdv'])
- Build (./waf build)
- Run (./waf --run dsdv -vis)
- Simulate .xml file with NetAnim

DOCUMENTATION: https://www.youtube.com/watch?v=Lw2HHAvi9Ao

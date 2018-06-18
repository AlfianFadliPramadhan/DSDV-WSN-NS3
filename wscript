## -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

def build(bld):
    obj = bld.create_ns3_program('dumbbell-animation',
                                 ['netanim', 'applications', 'point-to-point-layout'])
    obj.source = 'dumbbell-animation.cc'

    obj = bld.create_ns3_program('grid-animation',
                                 ['netanim', 'applications', 'point-to-point-layout'])
    obj.source = 'grid-animation.cc'

    obj = bld.create_ns3_program('star-animation',
                                 ['netanim', 'applications', 'point-to-point-layout'])
    obj.source = 'star-animation.cc'

    obj = bld.create_ns3_program('wireless-animation',
                                 ['netanim', 'applications', 'point-to-point', 'csma', 'wifi', 'mobility', 'network'])
    obj.source = 'wireless-animation.cc'
    
    obj = bld.create_ns3_program('uan-animation',
                                 ['netanim', 'internet', 'mobility', 'applications', 'uan'])
    obj.source = 'uan-animation.cc'

    obj = bld.create_ns3_program('colors-link-description',
                                 ['netanim', 'applications', 'point-to-point-layout'])
    obj.source = 'colors-link-description.cc'

    obj = bld.create_ns3_program('resources-counters',
                                 ['netanim', 'applications', 'point-to-point-layout'])
    obj.source = 'resources-counters.cc'

    obj = bld.create_ns3_program('dsdv',
                                 ['netanim', 'applications', 'point-to-point-layout'])
    obj.source = 'dsdv.cc'


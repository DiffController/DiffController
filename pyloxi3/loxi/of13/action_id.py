# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.
# See the file LICENSE.pyloxi which should have been included in the source distribution

# Automatically generated by LOXI from template module.py
# Do not modify

import struct
import loxi
from . import util
import functools
import loxi.generic_util

import sys
ofp = sys.modules['loxi.of13']

class action_id(loxi.OFObject):
    subtypes = {}


    def __init__(self, type=None):
        if type != None:
            self.type = type
        else:
            self.type = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!H', 0)
        subclass = action_id.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = action_id()
        obj.type = reader.read("!H")[0]
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.type != other.type: return False
        return True

    def pretty_print(self, q):
        q.text("action_id {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')


class experimenter(action_id):
    subtypes = {}

    type = 65535

    def __init__(self, experimenter=None):
        if experimenter != None:
            self.experimenter = experimenter
        else:
            self.experimenter = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!L', 4)
        subclass = experimenter.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = experimenter()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        obj.experimenter = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.experimenter != other.experimenter: return False
        return True

    def pretty_print(self, q):
        q.text("experimenter {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[65535] = experimenter

class bsn(experimenter):
    subtypes = {}

    type = 65535
    experimenter = 6035143

    def __init__(self, subtype=None):
        if subtype != None:
            self.subtype = subtype
        else:
            self.subtype = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!L', 8)
        subclass = bsn.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = bsn()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        obj.subtype = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.subtype != other.subtype: return False
        return True

    def pretty_print(self, q):
        q.text("bsn {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

experimenter.subtypes[6035143] = bsn

class bsn_checksum(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 4

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_checksum()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("bsn_checksum {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn.subtypes[4] = bsn_checksum

class bsn_gentable(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 5

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_gentable()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 5)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("bsn_gentable {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn.subtypes[5] = bsn_gentable

class bsn_mirror(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 1

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_mirror()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 1)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("bsn_mirror {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn.subtypes[1] = bsn_mirror

class bsn_set_tunnel_dst(bsn):
    type = 65535
    experimenter = 6035143
    subtype = 2

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.subtype))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_set_tunnel_dst()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _subtype = reader.read("!L")[0]
        assert(_subtype == 2)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("bsn_set_tunnel_dst {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn.subtypes[2] = bsn_set_tunnel_dst

class copy_ttl_in(action_id):
    type = 12

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = copy_ttl_in()
        _type = reader.read("!H")[0]
        assert(_type == 12)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("copy_ttl_in {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[12] = copy_ttl_in

class copy_ttl_out(action_id):
    type = 11

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = copy_ttl_out()
        _type = reader.read("!H")[0]
        assert(_type == 11)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("copy_ttl_out {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[11] = copy_ttl_out

class dec_mpls_ttl(action_id):
    type = 16

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = dec_mpls_ttl()
        _type = reader.read("!H")[0]
        assert(_type == 16)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("dec_mpls_ttl {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[16] = dec_mpls_ttl

class dec_nw_ttl(action_id):
    type = 24

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = dec_nw_ttl()
        _type = reader.read("!H")[0]
        assert(_type == 24)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("dec_nw_ttl {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[24] = dec_nw_ttl

class group(action_id):
    type = 22

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = group()
        _type = reader.read("!H")[0]
        assert(_type == 22)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("group {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[22] = group

class nicira(experimenter):
    subtypes = {}

    type = 65535
    experimenter = 8992

    def __init__(self, subtype=None):
        if subtype != None:
            self.subtype = subtype
        else:
            self.subtype = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!H", self.subtype))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!H', 8)
        subclass = nicira.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = nicira()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 8992)
        obj.subtype = reader.read("!H")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.subtype != other.subtype: return False
        return True

    def pretty_print(self, q):
        q.text("nicira {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

experimenter.subtypes[8992] = nicira

class nicira_dec_ttl(nicira):
    type = 65535
    experimenter = 8992
    subtype = 18

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!H", self.subtype))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = nicira_dec_ttl()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 8992)
        _subtype = reader.read("!H")[0]
        assert(_subtype == 18)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("nicira_dec_ttl {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

nicira.subtypes[18] = nicira_dec_ttl

class output(action_id):
    type = 0

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = output()
        _type = reader.read("!H")[0]
        assert(_type == 0)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("output {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[0] = output

class pop_mpls(action_id):
    type = 20

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = pop_mpls()
        _type = reader.read("!H")[0]
        assert(_type == 20)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("pop_mpls {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[20] = pop_mpls

class pop_pbb(action_id):
    type = 27

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = pop_pbb()
        _type = reader.read("!H")[0]
        assert(_type == 27)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("pop_pbb {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[27] = pop_pbb

class pop_vlan(action_id):
    type = 18

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = pop_vlan()
        _type = reader.read("!H")[0]
        assert(_type == 18)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("pop_vlan {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[18] = pop_vlan

class push_mpls(action_id):
    type = 19

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = push_mpls()
        _type = reader.read("!H")[0]
        assert(_type == 19)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("push_mpls {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[19] = push_mpls

class push_pbb(action_id):
    type = 26

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = push_pbb()
        _type = reader.read("!H")[0]
        assert(_type == 26)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("push_pbb {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[26] = push_pbb

class push_vlan(action_id):
    type = 17

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = push_vlan()
        _type = reader.read("!H")[0]
        assert(_type == 17)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("push_vlan {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[17] = push_vlan

class set_field(action_id):
    type = 25

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = set_field()
        _type = reader.read("!H")[0]
        assert(_type == 25)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("set_field {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[25] = set_field

class set_mpls_ttl(action_id):
    type = 15

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = set_mpls_ttl()
        _type = reader.read("!H")[0]
        assert(_type == 15)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("set_mpls_ttl {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[15] = set_mpls_ttl

class set_nw_ttl(action_id):
    type = 23

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = set_nw_ttl()
        _type = reader.read("!H")[0]
        assert(_type == 23)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("set_nw_ttl {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[23] = set_nw_ttl

class set_queue(action_id):
    type = 21

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = set_queue()
        _type = reader.read("!H")[0]
        assert(_type == 21)
        _len = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_len, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("set_queue {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

action_id.subtypes[21] = set_queue



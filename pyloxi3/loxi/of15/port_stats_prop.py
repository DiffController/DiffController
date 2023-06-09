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
ofp = sys.modules['loxi.of15']

class port_stats_prop(loxi.OFObject):
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
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!H', 0)
        subclass = port_stats_prop.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = port_stats_prop()
        obj.type = reader.read("!H")[0]
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.type != other.type: return False
        return True

    def pretty_print(self, q):
        q.text("port_stats_prop {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')


class ethernet(port_stats_prop):
    type = 0

    def __init__(self, rx_frame_err=None, rx_over_err=None, rx_crc_err=None, collisions=None):
        if rx_frame_err != None:
            self.rx_frame_err = rx_frame_err
        else:
            self.rx_frame_err = 0
        if rx_over_err != None:
            self.rx_over_err = rx_over_err
        else:
            self.rx_over_err = 0
        if rx_crc_err != None:
            self.rx_crc_err = rx_crc_err
        else:
            self.rx_crc_err = 0
        if collisions != None:
            self.collisions = collisions
        else:
            self.collisions = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(b'\x00' * 4)
        packed.append(struct.pack("!Q", self.rx_frame_err))
        packed.append(struct.pack("!Q", self.rx_over_err))
        packed.append(struct.pack("!Q", self.rx_crc_err))
        packed.append(struct.pack("!Q", self.collisions))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = ethernet()
        _type = reader.read("!H")[0]
        assert(_type == 0)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        reader.skip(4)
        obj.rx_frame_err = reader.read("!Q")[0]
        obj.rx_over_err = reader.read("!Q")[0]
        obj.rx_crc_err = reader.read("!Q")[0]
        obj.collisions = reader.read("!Q")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.rx_frame_err != other.rx_frame_err: return False
        if self.rx_over_err != other.rx_over_err: return False
        if self.rx_crc_err != other.rx_crc_err: return False
        if self.collisions != other.collisions: return False
        return True

    def pretty_print(self, q):
        q.text("ethernet {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("rx_frame_err = ");
                q.text("%#x" % self.rx_frame_err)
                q.text(","); q.breakable()
                q.text("rx_over_err = ");
                q.text("%#x" % self.rx_over_err)
                q.text(","); q.breakable()
                q.text("rx_crc_err = ");
                q.text("%#x" % self.rx_crc_err)
                q.text(","); q.breakable()
                q.text("collisions = ");
                q.text("%#x" % self.collisions)
            q.breakable()
        q.text('}')

port_stats_prop.subtypes[0] = ethernet

class experimenter(port_stats_prop):
    subtypes = {}

    type = 65535

    def __init__(self, experimenter=None, exp_type=None):
        if experimenter != None:
            self.experimenter = experimenter
        else:
            self.experimenter = 0
        if exp_type != None:
            self.exp_type = exp_type
        else:
            self.exp_type = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
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
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        obj.experimenter = reader.read("!L")[0]
        obj.exp_type = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.experimenter != other.experimenter: return False
        if self.exp_type != other.exp_type: return False
        return True

    def pretty_print(self, q):
        q.text("experimenter {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("exp_type = ");
                q.text("%#x" % self.exp_type)
            q.breakable()
        q.text('}')

port_stats_prop.subtypes[65535] = experimenter

class experimenter_intel(experimenter):
    type = 65535
    experimenter = 43521
    exp_type = 1

    def __init__(self, rx_1_to_64_packets=None, rx_65_to_127_packets=None, rx_128_to_255_packets=None, rx_256_to_511_packets=None, rx_512_to_1023_packets=None, rx_1024_to_1522_packets=None, rx_1523_to_max_packets=None, tx_1_to_64_packets=None, tx_65_to_127_packets=None, tx_128_to_255_packets=None, tx_256_to_511_packets=None, tx_512_to_1023_packets=None, tx_1024_to_1522_packets=None, tx_1523_to_max_packets=None, tx_multicast_packets=None, rx_broadcast_packets=None, tx_broadcast_packets=None, rx_undersized_errors=None, rx_oversize_errors=None, rx_fragmented_errors=None, rx_jabber_errors=None):
        if rx_1_to_64_packets != None:
            self.rx_1_to_64_packets = rx_1_to_64_packets
        else:
            self.rx_1_to_64_packets = 0
        if rx_65_to_127_packets != None:
            self.rx_65_to_127_packets = rx_65_to_127_packets
        else:
            self.rx_65_to_127_packets = 0
        if rx_128_to_255_packets != None:
            self.rx_128_to_255_packets = rx_128_to_255_packets
        else:
            self.rx_128_to_255_packets = 0
        if rx_256_to_511_packets != None:
            self.rx_256_to_511_packets = rx_256_to_511_packets
        else:
            self.rx_256_to_511_packets = 0
        if rx_512_to_1023_packets != None:
            self.rx_512_to_1023_packets = rx_512_to_1023_packets
        else:
            self.rx_512_to_1023_packets = 0
        if rx_1024_to_1522_packets != None:
            self.rx_1024_to_1522_packets = rx_1024_to_1522_packets
        else:
            self.rx_1024_to_1522_packets = 0
        if rx_1523_to_max_packets != None:
            self.rx_1523_to_max_packets = rx_1523_to_max_packets
        else:
            self.rx_1523_to_max_packets = 0
        if tx_1_to_64_packets != None:
            self.tx_1_to_64_packets = tx_1_to_64_packets
        else:
            self.tx_1_to_64_packets = 0
        if tx_65_to_127_packets != None:
            self.tx_65_to_127_packets = tx_65_to_127_packets
        else:
            self.tx_65_to_127_packets = 0
        if tx_128_to_255_packets != None:
            self.tx_128_to_255_packets = tx_128_to_255_packets
        else:
            self.tx_128_to_255_packets = 0
        if tx_256_to_511_packets != None:
            self.tx_256_to_511_packets = tx_256_to_511_packets
        else:
            self.tx_256_to_511_packets = 0
        if tx_512_to_1023_packets != None:
            self.tx_512_to_1023_packets = tx_512_to_1023_packets
        else:
            self.tx_512_to_1023_packets = 0
        if tx_1024_to_1522_packets != None:
            self.tx_1024_to_1522_packets = tx_1024_to_1522_packets
        else:
            self.tx_1024_to_1522_packets = 0
        if tx_1523_to_max_packets != None:
            self.tx_1523_to_max_packets = tx_1523_to_max_packets
        else:
            self.tx_1523_to_max_packets = 0
        if tx_multicast_packets != None:
            self.tx_multicast_packets = tx_multicast_packets
        else:
            self.tx_multicast_packets = 0
        if rx_broadcast_packets != None:
            self.rx_broadcast_packets = rx_broadcast_packets
        else:
            self.rx_broadcast_packets = 0
        if tx_broadcast_packets != None:
            self.tx_broadcast_packets = tx_broadcast_packets
        else:
            self.tx_broadcast_packets = 0
        if rx_undersized_errors != None:
            self.rx_undersized_errors = rx_undersized_errors
        else:
            self.rx_undersized_errors = 0
        if rx_oversize_errors != None:
            self.rx_oversize_errors = rx_oversize_errors
        else:
            self.rx_oversize_errors = 0
        if rx_fragmented_errors != None:
            self.rx_fragmented_errors = rx_fragmented_errors
        else:
            self.rx_fragmented_errors = 0
        if rx_jabber_errors != None:
            self.rx_jabber_errors = rx_jabber_errors
        else:
            self.rx_jabber_errors = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
        packed.append(b'\x00' * 4)
        packed.append(struct.pack("!Q", self.rx_1_to_64_packets))
        packed.append(struct.pack("!Q", self.rx_65_to_127_packets))
        packed.append(struct.pack("!Q", self.rx_128_to_255_packets))
        packed.append(struct.pack("!Q", self.rx_256_to_511_packets))
        packed.append(struct.pack("!Q", self.rx_512_to_1023_packets))
        packed.append(struct.pack("!Q", self.rx_1024_to_1522_packets))
        packed.append(struct.pack("!Q", self.rx_1523_to_max_packets))
        packed.append(struct.pack("!Q", self.tx_1_to_64_packets))
        packed.append(struct.pack("!Q", self.tx_65_to_127_packets))
        packed.append(struct.pack("!Q", self.tx_128_to_255_packets))
        packed.append(struct.pack("!Q", self.tx_256_to_511_packets))
        packed.append(struct.pack("!Q", self.tx_512_to_1023_packets))
        packed.append(struct.pack("!Q", self.tx_1024_to_1522_packets))
        packed.append(struct.pack("!Q", self.tx_1523_to_max_packets))
        packed.append(struct.pack("!Q", self.tx_multicast_packets))
        packed.append(struct.pack("!Q", self.rx_broadcast_packets))
        packed.append(struct.pack("!Q", self.tx_broadcast_packets))
        packed.append(struct.pack("!Q", self.rx_undersized_errors))
        packed.append(struct.pack("!Q", self.rx_oversize_errors))
        packed.append(struct.pack("!Q", self.rx_fragmented_errors))
        packed.append(struct.pack("!Q", self.rx_jabber_errors))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = experimenter_intel()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 43521)
        _exp_type = reader.read("!L")[0]
        assert(_exp_type == 1)
        reader.skip(4)
        obj.rx_1_to_64_packets = reader.read("!Q")[0]
        obj.rx_65_to_127_packets = reader.read("!Q")[0]
        obj.rx_128_to_255_packets = reader.read("!Q")[0]
        obj.rx_256_to_511_packets = reader.read("!Q")[0]
        obj.rx_512_to_1023_packets = reader.read("!Q")[0]
        obj.rx_1024_to_1522_packets = reader.read("!Q")[0]
        obj.rx_1523_to_max_packets = reader.read("!Q")[0]
        obj.tx_1_to_64_packets = reader.read("!Q")[0]
        obj.tx_65_to_127_packets = reader.read("!Q")[0]
        obj.tx_128_to_255_packets = reader.read("!Q")[0]
        obj.tx_256_to_511_packets = reader.read("!Q")[0]
        obj.tx_512_to_1023_packets = reader.read("!Q")[0]
        obj.tx_1024_to_1522_packets = reader.read("!Q")[0]
        obj.tx_1523_to_max_packets = reader.read("!Q")[0]
        obj.tx_multicast_packets = reader.read("!Q")[0]
        obj.rx_broadcast_packets = reader.read("!Q")[0]
        obj.tx_broadcast_packets = reader.read("!Q")[0]
        obj.rx_undersized_errors = reader.read("!Q")[0]
        obj.rx_oversize_errors = reader.read("!Q")[0]
        obj.rx_fragmented_errors = reader.read("!Q")[0]
        obj.rx_jabber_errors = reader.read("!Q")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.rx_1_to_64_packets != other.rx_1_to_64_packets: return False
        if self.rx_65_to_127_packets != other.rx_65_to_127_packets: return False
        if self.rx_128_to_255_packets != other.rx_128_to_255_packets: return False
        if self.rx_256_to_511_packets != other.rx_256_to_511_packets: return False
        if self.rx_512_to_1023_packets != other.rx_512_to_1023_packets: return False
        if self.rx_1024_to_1522_packets != other.rx_1024_to_1522_packets: return False
        if self.rx_1523_to_max_packets != other.rx_1523_to_max_packets: return False
        if self.tx_1_to_64_packets != other.tx_1_to_64_packets: return False
        if self.tx_65_to_127_packets != other.tx_65_to_127_packets: return False
        if self.tx_128_to_255_packets != other.tx_128_to_255_packets: return False
        if self.tx_256_to_511_packets != other.tx_256_to_511_packets: return False
        if self.tx_512_to_1023_packets != other.tx_512_to_1023_packets: return False
        if self.tx_1024_to_1522_packets != other.tx_1024_to_1522_packets: return False
        if self.tx_1523_to_max_packets != other.tx_1523_to_max_packets: return False
        if self.tx_multicast_packets != other.tx_multicast_packets: return False
        if self.rx_broadcast_packets != other.rx_broadcast_packets: return False
        if self.tx_broadcast_packets != other.tx_broadcast_packets: return False
        if self.rx_undersized_errors != other.rx_undersized_errors: return False
        if self.rx_oversize_errors != other.rx_oversize_errors: return False
        if self.rx_fragmented_errors != other.rx_fragmented_errors: return False
        if self.rx_jabber_errors != other.rx_jabber_errors: return False
        return True

    def pretty_print(self, q):
        q.text("experimenter_intel {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("rx_1_to_64_packets = ");
                q.text("%#x" % self.rx_1_to_64_packets)
                q.text(","); q.breakable()
                q.text("rx_65_to_127_packets = ");
                q.text("%#x" % self.rx_65_to_127_packets)
                q.text(","); q.breakable()
                q.text("rx_128_to_255_packets = ");
                q.text("%#x" % self.rx_128_to_255_packets)
                q.text(","); q.breakable()
                q.text("rx_256_to_511_packets = ");
                q.text("%#x" % self.rx_256_to_511_packets)
                q.text(","); q.breakable()
                q.text("rx_512_to_1023_packets = ");
                q.text("%#x" % self.rx_512_to_1023_packets)
                q.text(","); q.breakable()
                q.text("rx_1024_to_1522_packets = ");
                q.text("%#x" % self.rx_1024_to_1522_packets)
                q.text(","); q.breakable()
                q.text("rx_1523_to_max_packets = ");
                q.text("%#x" % self.rx_1523_to_max_packets)
                q.text(","); q.breakable()
                q.text("tx_1_to_64_packets = ");
                q.text("%#x" % self.tx_1_to_64_packets)
                q.text(","); q.breakable()
                q.text("tx_65_to_127_packets = ");
                q.text("%#x" % self.tx_65_to_127_packets)
                q.text(","); q.breakable()
                q.text("tx_128_to_255_packets = ");
                q.text("%#x" % self.tx_128_to_255_packets)
                q.text(","); q.breakable()
                q.text("tx_256_to_511_packets = ");
                q.text("%#x" % self.tx_256_to_511_packets)
                q.text(","); q.breakable()
                q.text("tx_512_to_1023_packets = ");
                q.text("%#x" % self.tx_512_to_1023_packets)
                q.text(","); q.breakable()
                q.text("tx_1024_to_1522_packets = ");
                q.text("%#x" % self.tx_1024_to_1522_packets)
                q.text(","); q.breakable()
                q.text("tx_1523_to_max_packets = ");
                q.text("%#x" % self.tx_1523_to_max_packets)
                q.text(","); q.breakable()
                q.text("tx_multicast_packets = ");
                q.text("%#x" % self.tx_multicast_packets)
                q.text(","); q.breakable()
                q.text("rx_broadcast_packets = ");
                q.text("%#x" % self.rx_broadcast_packets)
                q.text(","); q.breakable()
                q.text("tx_broadcast_packets = ");
                q.text("%#x" % self.tx_broadcast_packets)
                q.text(","); q.breakable()
                q.text("rx_undersized_errors = ");
                q.text("%#x" % self.rx_undersized_errors)
                q.text(","); q.breakable()
                q.text("rx_oversize_errors = ");
                q.text("%#x" % self.rx_oversize_errors)
                q.text(","); q.breakable()
                q.text("rx_fragmented_errors = ");
                q.text("%#x" % self.rx_fragmented_errors)
                q.text(","); q.breakable()
                q.text("rx_jabber_errors = ");
                q.text("%#x" % self.rx_jabber_errors)
            q.breakable()
        q.text('}')

experimenter.subtypes[43521] = experimenter_intel

class optical(port_stats_prop):
    type = 1

    def __init__(self, flags=None, tx_freq_lmda=None, tx_offset=None, tx_grid_span=None, rx_freq_lmda=None, rx_offset=None, rx_grid_span=None, tx_pwr=None, rx_pwr=None, bias_current=None, temperature=None):
        if flags != None:
            self.flags = flags
        else:
            self.flags = 0
        if tx_freq_lmda != None:
            self.tx_freq_lmda = tx_freq_lmda
        else:
            self.tx_freq_lmda = 0
        if tx_offset != None:
            self.tx_offset = tx_offset
        else:
            self.tx_offset = 0
        if tx_grid_span != None:
            self.tx_grid_span = tx_grid_span
        else:
            self.tx_grid_span = 0
        if rx_freq_lmda != None:
            self.rx_freq_lmda = rx_freq_lmda
        else:
            self.rx_freq_lmda = 0
        if rx_offset != None:
            self.rx_offset = rx_offset
        else:
            self.rx_offset = 0
        if rx_grid_span != None:
            self.rx_grid_span = rx_grid_span
        else:
            self.rx_grid_span = 0
        if tx_pwr != None:
            self.tx_pwr = tx_pwr
        else:
            self.tx_pwr = 0
        if rx_pwr != None:
            self.rx_pwr = rx_pwr
        else:
            self.rx_pwr = 0
        if bias_current != None:
            self.bias_current = bias_current
        else:
            self.bias_current = 0
        if temperature != None:
            self.temperature = temperature
        else:
            self.temperature = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(b'\x00' * 4)
        packed.append(struct.pack("!L", self.flags))
        packed.append(struct.pack("!L", self.tx_freq_lmda))
        packed.append(struct.pack("!L", self.tx_offset))
        packed.append(struct.pack("!L", self.tx_grid_span))
        packed.append(struct.pack("!L", self.rx_freq_lmda))
        packed.append(struct.pack("!L", self.rx_offset))
        packed.append(struct.pack("!L", self.rx_grid_span))
        packed.append(struct.pack("!H", self.tx_pwr))
        packed.append(struct.pack("!H", self.rx_pwr))
        packed.append(struct.pack("!H", self.bias_current))
        packed.append(struct.pack("!H", self.temperature))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return functools.reduce(lambda x,y: x+y, packed)

    @staticmethod
    def unpack(reader):
        obj = optical()
        _type = reader.read("!H")[0]
        assert(_type == 1)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        reader.skip(4)
        obj.flags = reader.read("!L")[0]
        obj.tx_freq_lmda = reader.read("!L")[0]
        obj.tx_offset = reader.read("!L")[0]
        obj.tx_grid_span = reader.read("!L")[0]
        obj.rx_freq_lmda = reader.read("!L")[0]
        obj.rx_offset = reader.read("!L")[0]
        obj.rx_grid_span = reader.read("!L")[0]
        obj.tx_pwr = reader.read("!H")[0]
        obj.rx_pwr = reader.read("!H")[0]
        obj.bias_current = reader.read("!H")[0]
        obj.temperature = reader.read("!H")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.flags != other.flags: return False
        if self.tx_freq_lmda != other.tx_freq_lmda: return False
        if self.tx_offset != other.tx_offset: return False
        if self.tx_grid_span != other.tx_grid_span: return False
        if self.rx_freq_lmda != other.rx_freq_lmda: return False
        if self.rx_offset != other.rx_offset: return False
        if self.rx_grid_span != other.rx_grid_span: return False
        if self.tx_pwr != other.tx_pwr: return False
        if self.rx_pwr != other.rx_pwr: return False
        if self.bias_current != other.bias_current: return False
        if self.temperature != other.temperature: return False
        return True

    def pretty_print(self, q):
        q.text("optical {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("flags = ");
                q.text("%#x" % self.flags)
                q.text(","); q.breakable()
                q.text("tx_freq_lmda = ");
                q.text("%#x" % self.tx_freq_lmda)
                q.text(","); q.breakable()
                q.text("tx_offset = ");
                q.text("%#x" % self.tx_offset)
                q.text(","); q.breakable()
                q.text("tx_grid_span = ");
                q.text("%#x" % self.tx_grid_span)
                q.text(","); q.breakable()
                q.text("rx_freq_lmda = ");
                q.text("%#x" % self.rx_freq_lmda)
                q.text(","); q.breakable()
                q.text("rx_offset = ");
                q.text("%#x" % self.rx_offset)
                q.text(","); q.breakable()
                q.text("rx_grid_span = ");
                q.text("%#x" % self.rx_grid_span)
                q.text(","); q.breakable()
                q.text("tx_pwr = ");
                q.text("%#x" % self.tx_pwr)
                q.text(","); q.breakable()
                q.text("rx_pwr = ");
                q.text("%#x" % self.rx_pwr)
                q.text(","); q.breakable()
                q.text("bias_current = ");
                q.text("%#x" % self.bias_current)
                q.text(","); q.breakable()
                q.text("temperature = ");
                q.text("%#x" % self.temperature)
            q.breakable()
        q.text('}')

port_stats_prop.subtypes[1] = optical



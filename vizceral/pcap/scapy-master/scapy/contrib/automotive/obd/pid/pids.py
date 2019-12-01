# flake8: noqa: F405

# This file is part of Scapy
# See http://www.secdev.org/projects/scapy for more information
# Copyright (C) Andreas Korb <andreas.d.korb@gmail.com>
# Copyright (C) Nils Weiss <nils@we155.de>
# This program is published under a GPLv2 license

# scapy.contrib.status = skip

from scapy.packet import Packet, bind_layers
from scapy.fields import PacketListField

from scapy.contrib.automotive.obd.services import OBD_S01, OBD_S02
from scapy.contrib.automotive.obd.pid.pids_00_1F import *
from scapy.contrib.automotive.obd.pid.pids_20_3F import *
from scapy.contrib.automotive.obd.pid.pids_40_5F import *
from scapy.contrib.automotive.obd.pid.pids_60_7F import *
from scapy.contrib.automotive.obd.pid.pids_80_9F import *
from scapy.contrib.automotive.obd.pid.pids_A0_C0 import *


class OBD_S01_PR_Record(Packet):
    fields_desc = [
        XByteField("pid", 0),
    ]


class OBD_S01_PR(Packet):
    name = "Parameter IDs"
    fields_desc = [
        PacketListField("data_records", [], OBD_S01_PR_Record)
    ]

    def answers(self, other):
        return other.__class__ == OBD_S01 \
            and all(r.pid in other.pid for r in self.data_records)


class OBD_S02_PR_Record(Packet):
    fields_desc = [
        XByteField("pid", 0),
        XByteField("frame_no", 0),
    ]


class OBD_S02_PR(Packet):
    name = "Parameter IDs"
    fields_desc = [
        PacketListField("data_records", [], OBD_S02_PR_Record)
    ]

    def answers(self, other):
        return other.__class__ == OBD_S02 \
            and all(r.pid in [o.pid for o in other.requests] for r in self.data_records)


bind_layers(OBD_S01_PR_Record, OBD_PID00, pid=0x00)
bind_layers(OBD_S01_PR_Record, OBD_PID01, pid=0x01)
bind_layers(OBD_S01_PR_Record, OBD_PID02, pid=0x02)
bind_layers(OBD_S01_PR_Record, OBD_PID03, pid=0x03)
bind_layers(OBD_S01_PR_Record, OBD_PID04, pid=0x04)
bind_layers(OBD_S01_PR_Record, OBD_PID05, pid=0x05)
bind_layers(OBD_S01_PR_Record, OBD_PID06, pid=0x06)
bind_layers(OBD_S01_PR_Record, OBD_PID07, pid=0x07)
bind_layers(OBD_S01_PR_Record, OBD_PID08, pid=0x08)
bind_layers(OBD_S01_PR_Record, OBD_PID09, pid=0x09)
bind_layers(OBD_S01_PR_Record, OBD_PID0A, pid=0x0A)
bind_layers(OBD_S01_PR_Record, OBD_PID0B, pid=0x0B)
bind_layers(OBD_S01_PR_Record, OBD_PID0C, pid=0x0C)
bind_layers(OBD_S01_PR_Record, OBD_PID0D, pid=0x0D)
bind_layers(OBD_S01_PR_Record, OBD_PID0E, pid=0x0E)
bind_layers(OBD_S01_PR_Record, OBD_PID0F, pid=0x0F)
bind_layers(OBD_S01_PR_Record, OBD_PID10, pid=0x10)
bind_layers(OBD_S01_PR_Record, OBD_PID11, pid=0x11)
bind_layers(OBD_S01_PR_Record, OBD_PID12, pid=0x12)
bind_layers(OBD_S01_PR_Record, OBD_PID13, pid=0x13)
bind_layers(OBD_S01_PR_Record, OBD_PID14, pid=0x14)
bind_layers(OBD_S01_PR_Record, OBD_PID15, pid=0x15)
bind_layers(OBD_S01_PR_Record, OBD_PID16, pid=0x16)
bind_layers(OBD_S01_PR_Record, OBD_PID17, pid=0x17)
bind_layers(OBD_S01_PR_Record, OBD_PID18, pid=0x18)
bind_layers(OBD_S01_PR_Record, OBD_PID19, pid=0x19)
bind_layers(OBD_S01_PR_Record, OBD_PID1A, pid=0x1A)
bind_layers(OBD_S01_PR_Record, OBD_PID1B, pid=0x1B)
bind_layers(OBD_S01_PR_Record, OBD_PID1C, pid=0x1C)
bind_layers(OBD_S01_PR_Record, OBD_PID1D, pid=0x1D)
bind_layers(OBD_S01_PR_Record, OBD_PID1E, pid=0x1E)
bind_layers(OBD_S01_PR_Record, OBD_PID1F, pid=0x1F)
bind_layers(OBD_S01_PR_Record, OBD_PID20, pid=0x20)
bind_layers(OBD_S01_PR_Record, OBD_PID21, pid=0x21)
bind_layers(OBD_S01_PR_Record, OBD_PID22, pid=0x22)
bind_layers(OBD_S01_PR_Record, OBD_PID23, pid=0x23)
bind_layers(OBD_S01_PR_Record, OBD_PID24, pid=0x24)
bind_layers(OBD_S01_PR_Record, OBD_PID25, pid=0x25)
bind_layers(OBD_S01_PR_Record, OBD_PID26, pid=0x26)
bind_layers(OBD_S01_PR_Record, OBD_PID27, pid=0x27)
bind_layers(OBD_S01_PR_Record, OBD_PID28, pid=0x28)
bind_layers(OBD_S01_PR_Record, OBD_PID29, pid=0x29)
bind_layers(OBD_S01_PR_Record, OBD_PID2A, pid=0x2A)
bind_layers(OBD_S01_PR_Record, OBD_PID2B, pid=0x2B)
bind_layers(OBD_S01_PR_Record, OBD_PID2C, pid=0x2C)
bind_layers(OBD_S01_PR_Record, OBD_PID2D, pid=0x2D)
bind_layers(OBD_S01_PR_Record, OBD_PID2E, pid=0x2E)
bind_layers(OBD_S01_PR_Record, OBD_PID2F, pid=0x2F)
bind_layers(OBD_S01_PR_Record, OBD_PID30, pid=0x30)
bind_layers(OBD_S01_PR_Record, OBD_PID31, pid=0x31)
bind_layers(OBD_S01_PR_Record, OBD_PID32, pid=0x32)
bind_layers(OBD_S01_PR_Record, OBD_PID33, pid=0x33)
bind_layers(OBD_S01_PR_Record, OBD_PID34, pid=0x34)
bind_layers(OBD_S01_PR_Record, OBD_PID35, pid=0x35)
bind_layers(OBD_S01_PR_Record, OBD_PID36, pid=0x36)
bind_layers(OBD_S01_PR_Record, OBD_PID37, pid=0x37)
bind_layers(OBD_S01_PR_Record, OBD_PID38, pid=0x38)
bind_layers(OBD_S01_PR_Record, OBD_PID39, pid=0x39)
bind_layers(OBD_S01_PR_Record, OBD_PID3A, pid=0x3A)
bind_layers(OBD_S01_PR_Record, OBD_PID3B, pid=0x3B)
bind_layers(OBD_S01_PR_Record, OBD_PID3C, pid=0x3C)
bind_layers(OBD_S01_PR_Record, OBD_PID3D, pid=0x3D)
bind_layers(OBD_S01_PR_Record, OBD_PID3E, pid=0x3E)
bind_layers(OBD_S01_PR_Record, OBD_PID3F, pid=0x3F)
bind_layers(OBD_S01_PR_Record, OBD_PID40, pid=0x40)
bind_layers(OBD_S01_PR_Record, OBD_PID41, pid=0x41)
bind_layers(OBD_S01_PR_Record, OBD_PID42, pid=0x42)
bind_layers(OBD_S01_PR_Record, OBD_PID43, pid=0x43)
bind_layers(OBD_S01_PR_Record, OBD_PID44, pid=0x44)
bind_layers(OBD_S01_PR_Record, OBD_PID45, pid=0x45)
bind_layers(OBD_S01_PR_Record, OBD_PID46, pid=0x46)
bind_layers(OBD_S01_PR_Record, OBD_PID47, pid=0x47)
bind_layers(OBD_S01_PR_Record, OBD_PID48, pid=0x48)
bind_layers(OBD_S01_PR_Record, OBD_PID49, pid=0x49)
bind_layers(OBD_S01_PR_Record, OBD_PID4A, pid=0x4A)
bind_layers(OBD_S01_PR_Record, OBD_PID4B, pid=0x4B)
bind_layers(OBD_S01_PR_Record, OBD_PID4C, pid=0x4C)
bind_layers(OBD_S01_PR_Record, OBD_PID4D, pid=0x4D)
bind_layers(OBD_S01_PR_Record, OBD_PID4E, pid=0x4E)
bind_layers(OBD_S01_PR_Record, OBD_PID4F, pid=0x4F)
bind_layers(OBD_S01_PR_Record, OBD_PID50, pid=0x50)
bind_layers(OBD_S01_PR_Record, OBD_PID51, pid=0x51)
bind_layers(OBD_S01_PR_Record, OBD_PID52, pid=0x52)
bind_layers(OBD_S01_PR_Record, OBD_PID53, pid=0x53)
bind_layers(OBD_S01_PR_Record, OBD_PID54, pid=0x54)
bind_layers(OBD_S01_PR_Record, OBD_PID55, pid=0x55)
bind_layers(OBD_S01_PR_Record, OBD_PID56, pid=0x56)
bind_layers(OBD_S01_PR_Record, OBD_PID57, pid=0x57)
bind_layers(OBD_S01_PR_Record, OBD_PID58, pid=0x58)
bind_layers(OBD_S01_PR_Record, OBD_PID59, pid=0x59)
bind_layers(OBD_S01_PR_Record, OBD_PID5A, pid=0x5A)
bind_layers(OBD_S01_PR_Record, OBD_PID5B, pid=0x5B)
bind_layers(OBD_S01_PR_Record, OBD_PID5C, pid=0x5C)
bind_layers(OBD_S01_PR_Record, OBD_PID5D, pid=0x5D)
bind_layers(OBD_S01_PR_Record, OBD_PID5E, pid=0x5E)
bind_layers(OBD_S01_PR_Record, OBD_PID5F, pid=0x5F)
bind_layers(OBD_S01_PR_Record, OBD_PID60, pid=0x60)
bind_layers(OBD_S01_PR_Record, OBD_PID61, pid=0x61)
bind_layers(OBD_S01_PR_Record, OBD_PID62, pid=0x62)
bind_layers(OBD_S01_PR_Record, OBD_PID63, pid=0x63)
bind_layers(OBD_S01_PR_Record, OBD_PID64, pid=0x64)
bind_layers(OBD_S01_PR_Record, OBD_PID65, pid=0x65)
bind_layers(OBD_S01_PR_Record, OBD_PID66, pid=0x66)
bind_layers(OBD_S01_PR_Record, OBD_PID67, pid=0x67)
bind_layers(OBD_S01_PR_Record, OBD_PID68, pid=0x68)
bind_layers(OBD_S01_PR_Record, OBD_PID69, pid=0x69)
bind_layers(OBD_S01_PR_Record, OBD_PID6A, pid=0x6A)
bind_layers(OBD_S01_PR_Record, OBD_PID6B, pid=0x6B)
bind_layers(OBD_S01_PR_Record, OBD_PID6C, pid=0x6C)
bind_layers(OBD_S01_PR_Record, OBD_PID6D, pid=0x6D)
bind_layers(OBD_S01_PR_Record, OBD_PID6E, pid=0x6E)
bind_layers(OBD_S01_PR_Record, OBD_PID6F, pid=0x6F)
bind_layers(OBD_S01_PR_Record, OBD_PID70, pid=0x70)
bind_layers(OBD_S01_PR_Record, OBD_PID71, pid=0x71)
bind_layers(OBD_S01_PR_Record, OBD_PID72, pid=0x72)
bind_layers(OBD_S01_PR_Record, OBD_PID73, pid=0x73)
bind_layers(OBD_S01_PR_Record, OBD_PID74, pid=0x74)
bind_layers(OBD_S01_PR_Record, OBD_PID75, pid=0x75)
bind_layers(OBD_S01_PR_Record, OBD_PID76, pid=0x76)
bind_layers(OBD_S01_PR_Record, OBD_PID77, pid=0x77)
bind_layers(OBD_S01_PR_Record, OBD_PID78, pid=0x78)
bind_layers(OBD_S01_PR_Record, OBD_PID79, pid=0x79)
bind_layers(OBD_S01_PR_Record, OBD_PID7A, pid=0x7A)
bind_layers(OBD_S01_PR_Record, OBD_PID7B, pid=0x7B)
bind_layers(OBD_S01_PR_Record, OBD_PID7C, pid=0x7C)
bind_layers(OBD_S01_PR_Record, OBD_PID7D, pid=0x7D)
bind_layers(OBD_S01_PR_Record, OBD_PID7E, pid=0x7E)
bind_layers(OBD_S01_PR_Record, OBD_PID7F, pid=0x7F)
bind_layers(OBD_S01_PR_Record, OBD_PID80, pid=0x80)
bind_layers(OBD_S01_PR_Record, OBD_PID81, pid=0x81)
bind_layers(OBD_S01_PR_Record, OBD_PID82, pid=0x82)
bind_layers(OBD_S01_PR_Record, OBD_PID83, pid=0x83)
bind_layers(OBD_S01_PR_Record, OBD_PID84, pid=0x84)
bind_layers(OBD_S01_PR_Record, OBD_PID85, pid=0x85)
bind_layers(OBD_S01_PR_Record, OBD_PID86, pid=0x86)
bind_layers(OBD_S01_PR_Record, OBD_PID87, pid=0x87)
bind_layers(OBD_S01_PR_Record, OBD_PID88, pid=0x88)
bind_layers(OBD_S01_PR_Record, OBD_PID89, pid=0x89)
bind_layers(OBD_S01_PR_Record, OBD_PID8A, pid=0x8A)
bind_layers(OBD_S01_PR_Record, OBD_PID8B, pid=0x8B)
bind_layers(OBD_S01_PR_Record, OBD_PID8C, pid=0x8C)
bind_layers(OBD_S01_PR_Record, OBD_PID8D, pid=0x8D)
bind_layers(OBD_S01_PR_Record, OBD_PID8E, pid=0x8E)
bind_layers(OBD_S01_PR_Record, OBD_PID8F, pid=0x8F)
bind_layers(OBD_S01_PR_Record, OBD_PID90, pid=0x90)
bind_layers(OBD_S01_PR_Record, OBD_PID91, pid=0x91)
bind_layers(OBD_S01_PR_Record, OBD_PID92, pid=0x92)
bind_layers(OBD_S01_PR_Record, OBD_PID93, pid=0x93)
bind_layers(OBD_S01_PR_Record, OBD_PID94, pid=0x94)
bind_layers(OBD_S01_PR_Record, OBD_PID98, pid=0x98)
bind_layers(OBD_S01_PR_Record, OBD_PID99, pid=0x99)
bind_layers(OBD_S01_PR_Record, OBD_PID9A, pid=0x9A)
bind_layers(OBD_S01_PR_Record, OBD_PID9B, pid=0x9B)
bind_layers(OBD_S01_PR_Record, OBD_PID9C, pid=0x9C)
bind_layers(OBD_S01_PR_Record, OBD_PID9D, pid=0x9D)
bind_layers(OBD_S01_PR_Record, OBD_PID9E, pid=0x9E)
bind_layers(OBD_S01_PR_Record, OBD_PID9F, pid=0x9F)
bind_layers(OBD_S01_PR_Record, OBD_PIDA0, pid=0xA0)
bind_layers(OBD_S01_PR_Record, OBD_PIDA1, pid=0xA1)
bind_layers(OBD_S01_PR_Record, OBD_PIDA2, pid=0xA2)
bind_layers(OBD_S01_PR_Record, OBD_PIDA3, pid=0xA3)
bind_layers(OBD_S01_PR_Record, OBD_PIDA4, pid=0xA4)
bind_layers(OBD_S01_PR_Record, OBD_PIDA5, pid=0xA5)
bind_layers(OBD_S01_PR_Record, OBD_PIDA6, pid=0xA6)
bind_layers(OBD_S01_PR_Record, OBD_PIDC0, pid=0xC0)


# Service 2

bind_layers(OBD_S02_PR_Record, OBD_PID00, pid=0x00)
bind_layers(OBD_S02_PR_Record, OBD_PID01, pid=0x01)
bind_layers(OBD_S02_PR_Record, OBD_PID02, pid=0x02)
bind_layers(OBD_S02_PR_Record, OBD_PID03, pid=0x03)
bind_layers(OBD_S02_PR_Record, OBD_PID04, pid=0x04)
bind_layers(OBD_S02_PR_Record, OBD_PID05, pid=0x05)
bind_layers(OBD_S02_PR_Record, OBD_PID06, pid=0x06)
bind_layers(OBD_S02_PR_Record, OBD_PID07, pid=0x07)
bind_layers(OBD_S02_PR_Record, OBD_PID08, pid=0x08)
bind_layers(OBD_S02_PR_Record, OBD_PID09, pid=0x09)
bind_layers(OBD_S02_PR_Record, OBD_PID0A, pid=0x0A)
bind_layers(OBD_S02_PR_Record, OBD_PID0B, pid=0x0B)
bind_layers(OBD_S02_PR_Record, OBD_PID0C, pid=0x0C)
bind_layers(OBD_S02_PR_Record, OBD_PID0D, pid=0x0D)
bind_layers(OBD_S02_PR_Record, OBD_PID0E, pid=0x0E)
bind_layers(OBD_S02_PR_Record, OBD_PID0F, pid=0x0F)
bind_layers(OBD_S02_PR_Record, OBD_PID10, pid=0x10)
bind_layers(OBD_S02_PR_Record, OBD_PID11, pid=0x11)
bind_layers(OBD_S02_PR_Record, OBD_PID12, pid=0x12)
bind_layers(OBD_S02_PR_Record, OBD_PID13, pid=0x13)
bind_layers(OBD_S02_PR_Record, OBD_PID14, pid=0x14)
bind_layers(OBD_S02_PR_Record, OBD_PID15, pid=0x15)
bind_layers(OBD_S02_PR_Record, OBD_PID16, pid=0x16)
bind_layers(OBD_S02_PR_Record, OBD_PID17, pid=0x17)
bind_layers(OBD_S02_PR_Record, OBD_PID18, pid=0x18)
bind_layers(OBD_S02_PR_Record, OBD_PID19, pid=0x19)
bind_layers(OBD_S02_PR_Record, OBD_PID1A, pid=0x1A)
bind_layers(OBD_S02_PR_Record, OBD_PID1B, pid=0x1B)
bind_layers(OBD_S02_PR_Record, OBD_PID1C, pid=0x1C)
bind_layers(OBD_S02_PR_Record, OBD_PID1D, pid=0x1D)
bind_layers(OBD_S02_PR_Record, OBD_PID1E, pid=0x1E)
bind_layers(OBD_S02_PR_Record, OBD_PID1F, pid=0x1F)
bind_layers(OBD_S02_PR_Record, OBD_PID20, pid=0x20)
bind_layers(OBD_S02_PR_Record, OBD_PID21, pid=0x21)
bind_layers(OBD_S02_PR_Record, OBD_PID22, pid=0x22)
bind_layers(OBD_S02_PR_Record, OBD_PID23, pid=0x23)
bind_layers(OBD_S02_PR_Record, OBD_PID24, pid=0x24)
bind_layers(OBD_S02_PR_Record, OBD_PID25, pid=0x25)
bind_layers(OBD_S02_PR_Record, OBD_PID26, pid=0x26)
bind_layers(OBD_S02_PR_Record, OBD_PID27, pid=0x27)
bind_layers(OBD_S02_PR_Record, OBD_PID28, pid=0x28)
bind_layers(OBD_S02_PR_Record, OBD_PID29, pid=0x29)
bind_layers(OBD_S02_PR_Record, OBD_PID2A, pid=0x2A)
bind_layers(OBD_S02_PR_Record, OBD_PID2B, pid=0x2B)
bind_layers(OBD_S02_PR_Record, OBD_PID2C, pid=0x2C)
bind_layers(OBD_S02_PR_Record, OBD_PID2D, pid=0x2D)
bind_layers(OBD_S02_PR_Record, OBD_PID2E, pid=0x2E)
bind_layers(OBD_S02_PR_Record, OBD_PID2F, pid=0x2F)
bind_layers(OBD_S02_PR_Record, OBD_PID30, pid=0x30)
bind_layers(OBD_S02_PR_Record, OBD_PID31, pid=0x31)
bind_layers(OBD_S02_PR_Record, OBD_PID32, pid=0x32)
bind_layers(OBD_S02_PR_Record, OBD_PID33, pid=0x33)
bind_layers(OBD_S02_PR_Record, OBD_PID34, pid=0x34)
bind_layers(OBD_S02_PR_Record, OBD_PID35, pid=0x35)
bind_layers(OBD_S02_PR_Record, OBD_PID36, pid=0x36)
bind_layers(OBD_S02_PR_Record, OBD_PID37, pid=0x37)
bind_layers(OBD_S02_PR_Record, OBD_PID38, pid=0x38)
bind_layers(OBD_S02_PR_Record, OBD_PID39, pid=0x39)
bind_layers(OBD_S02_PR_Record, OBD_PID3A, pid=0x3A)
bind_layers(OBD_S02_PR_Record, OBD_PID3B, pid=0x3B)
bind_layers(OBD_S02_PR_Record, OBD_PID3C, pid=0x3C)
bind_layers(OBD_S02_PR_Record, OBD_PID3D, pid=0x3D)
bind_layers(OBD_S02_PR_Record, OBD_PID3E, pid=0x3E)
bind_layers(OBD_S02_PR_Record, OBD_PID3F, pid=0x3F)
bind_layers(OBD_S02_PR_Record, OBD_PID40, pid=0x40)
bind_layers(OBD_S02_PR_Record, OBD_PID41, pid=0x41)
bind_layers(OBD_S02_PR_Record, OBD_PID42, pid=0x42)
bind_layers(OBD_S02_PR_Record, OBD_PID43, pid=0x43)
bind_layers(OBD_S02_PR_Record, OBD_PID44, pid=0x44)
bind_layers(OBD_S02_PR_Record, OBD_PID45, pid=0x45)
bind_layers(OBD_S02_PR_Record, OBD_PID46, pid=0x46)
bind_layers(OBD_S02_PR_Record, OBD_PID47, pid=0x47)
bind_layers(OBD_S02_PR_Record, OBD_PID48, pid=0x48)
bind_layers(OBD_S02_PR_Record, OBD_PID49, pid=0x49)
bind_layers(OBD_S02_PR_Record, OBD_PID4A, pid=0x4A)
bind_layers(OBD_S02_PR_Record, OBD_PID4B, pid=0x4B)
bind_layers(OBD_S02_PR_Record, OBD_PID4C, pid=0x4C)
bind_layers(OBD_S02_PR_Record, OBD_PID4D, pid=0x4D)
bind_layers(OBD_S02_PR_Record, OBD_PID4E, pid=0x4E)
bind_layers(OBD_S02_PR_Record, OBD_PID4F, pid=0x4F)
bind_layers(OBD_S02_PR_Record, OBD_PID50, pid=0x50)
bind_layers(OBD_S02_PR_Record, OBD_PID51, pid=0x51)
bind_layers(OBD_S02_PR_Record, OBD_PID52, pid=0x52)
bind_layers(OBD_S02_PR_Record, OBD_PID53, pid=0x53)
bind_layers(OBD_S02_PR_Record, OBD_PID54, pid=0x54)
bind_layers(OBD_S02_PR_Record, OBD_PID55, pid=0x55)
bind_layers(OBD_S02_PR_Record, OBD_PID56, pid=0x56)
bind_layers(OBD_S02_PR_Record, OBD_PID57, pid=0x57)
bind_layers(OBD_S02_PR_Record, OBD_PID58, pid=0x58)
bind_layers(OBD_S02_PR_Record, OBD_PID59, pid=0x59)
bind_layers(OBD_S02_PR_Record, OBD_PID5A, pid=0x5A)
bind_layers(OBD_S02_PR_Record, OBD_PID5B, pid=0x5B)
bind_layers(OBD_S02_PR_Record, OBD_PID5C, pid=0x5C)
bind_layers(OBD_S02_PR_Record, OBD_PID5D, pid=0x5D)
bind_layers(OBD_S02_PR_Record, OBD_PID5E, pid=0x5E)
bind_layers(OBD_S02_PR_Record, OBD_PID5F, pid=0x5F)
bind_layers(OBD_S02_PR_Record, OBD_PID60, pid=0x60)
bind_layers(OBD_S02_PR_Record, OBD_PID61, pid=0x61)
bind_layers(OBD_S02_PR_Record, OBD_PID62, pid=0x62)
bind_layers(OBD_S02_PR_Record, OBD_PID63, pid=0x63)
bind_layers(OBD_S02_PR_Record, OBD_PID64, pid=0x64)
bind_layers(OBD_S02_PR_Record, OBD_PID65, pid=0x65)
bind_layers(OBD_S02_PR_Record, OBD_PID66, pid=0x66)
bind_layers(OBD_S02_PR_Record, OBD_PID67, pid=0x67)
bind_layers(OBD_S02_PR_Record, OBD_PID68, pid=0x68)
bind_layers(OBD_S02_PR_Record, OBD_PID69, pid=0x69)
bind_layers(OBD_S02_PR_Record, OBD_PID6A, pid=0x6A)
bind_layers(OBD_S02_PR_Record, OBD_PID6B, pid=0x6B)
bind_layers(OBD_S02_PR_Record, OBD_PID6C, pid=0x6C)
bind_layers(OBD_S02_PR_Record, OBD_PID6D, pid=0x6D)
bind_layers(OBD_S02_PR_Record, OBD_PID6E, pid=0x6E)
bind_layers(OBD_S02_PR_Record, OBD_PID6F, pid=0x6F)
bind_layers(OBD_S02_PR_Record, OBD_PID70, pid=0x70)
bind_layers(OBD_S02_PR_Record, OBD_PID71, pid=0x71)
bind_layers(OBD_S02_PR_Record, OBD_PID72, pid=0x72)
bind_layers(OBD_S02_PR_Record, OBD_PID73, pid=0x73)
bind_layers(OBD_S02_PR_Record, OBD_PID74, pid=0x74)
bind_layers(OBD_S02_PR_Record, OBD_PID75, pid=0x75)
bind_layers(OBD_S02_PR_Record, OBD_PID76, pid=0x76)
bind_layers(OBD_S02_PR_Record, OBD_PID77, pid=0x77)
bind_layers(OBD_S02_PR_Record, OBD_PID78, pid=0x78)
bind_layers(OBD_S02_PR_Record, OBD_PID79, pid=0x79)
bind_layers(OBD_S02_PR_Record, OBD_PID7A, pid=0x7A)
bind_layers(OBD_S02_PR_Record, OBD_PID7B, pid=0x7B)
bind_layers(OBD_S02_PR_Record, OBD_PID7C, pid=0x7C)
bind_layers(OBD_S02_PR_Record, OBD_PID7D, pid=0x7D)
bind_layers(OBD_S02_PR_Record, OBD_PID7E, pid=0x7E)
bind_layers(OBD_S02_PR_Record, OBD_PID7F, pid=0x7F)
bind_layers(OBD_S02_PR_Record, OBD_PID80, pid=0x80)
bind_layers(OBD_S02_PR_Record, OBD_PID81, pid=0x81)
bind_layers(OBD_S02_PR_Record, OBD_PID82, pid=0x82)
bind_layers(OBD_S02_PR_Record, OBD_PID83, pid=0x83)
bind_layers(OBD_S02_PR_Record, OBD_PID84, pid=0x84)
bind_layers(OBD_S02_PR_Record, OBD_PID85, pid=0x85)
bind_layers(OBD_S02_PR_Record, OBD_PID86, pid=0x86)
bind_layers(OBD_S02_PR_Record, OBD_PID87, pid=0x87)
bind_layers(OBD_S02_PR_Record, OBD_PID88, pid=0x88)
bind_layers(OBD_S02_PR_Record, OBD_PID89, pid=0x89)
bind_layers(OBD_S02_PR_Record, OBD_PID8A, pid=0x8A)
bind_layers(OBD_S02_PR_Record, OBD_PID8B, pid=0x8B)
bind_layers(OBD_S02_PR_Record, OBD_PID8C, pid=0x8C)
bind_layers(OBD_S02_PR_Record, OBD_PID8D, pid=0x8D)
bind_layers(OBD_S02_PR_Record, OBD_PID8E, pid=0x8E)
bind_layers(OBD_S02_PR_Record, OBD_PID8F, pid=0x8F)
bind_layers(OBD_S02_PR_Record, OBD_PID90, pid=0x90)
bind_layers(OBD_S02_PR_Record, OBD_PID91, pid=0x91)
bind_layers(OBD_S02_PR_Record, OBD_PID92, pid=0x92)
bind_layers(OBD_S02_PR_Record, OBD_PID93, pid=0x93)
bind_layers(OBD_S02_PR_Record, OBD_PID94, pid=0x94)
bind_layers(OBD_S02_PR_Record, OBD_PID98, pid=0x98)
bind_layers(OBD_S02_PR_Record, OBD_PID99, pid=0x99)
bind_layers(OBD_S02_PR_Record, OBD_PID9A, pid=0x9A)
bind_layers(OBD_S02_PR_Record, OBD_PID9B, pid=0x9B)
bind_layers(OBD_S02_PR_Record, OBD_PID9C, pid=0x9C)
bind_layers(OBD_S02_PR_Record, OBD_PID9D, pid=0x9D)
bind_layers(OBD_S02_PR_Record, OBD_PID9E, pid=0x9E)
bind_layers(OBD_S02_PR_Record, OBD_PID9F, pid=0x9F)
bind_layers(OBD_S02_PR_Record, OBD_PIDA0, pid=0xA0)
bind_layers(OBD_S02_PR_Record, OBD_PIDA1, pid=0xA1)
bind_layers(OBD_S02_PR_Record, OBD_PIDA2, pid=0xA2)
bind_layers(OBD_S02_PR_Record, OBD_PIDA3, pid=0xA3)
bind_layers(OBD_S02_PR_Record, OBD_PIDA4, pid=0xA4)
bind_layers(OBD_S02_PR_Record, OBD_PIDA5, pid=0xA5)
bind_layers(OBD_S02_PR_Record, OBD_PIDA6, pid=0xA6)
bind_layers(OBD_S02_PR_Record, OBD_PIDC0, pid=0xC0)

import struct
from typing import Dict

MAX_PKT_SIZE = 1024
MAX_DATA_SIZE = MAX_PKT_SIZE - 4 * 4


class Packet:
    def __init__(self, frame_no: int, seq_no: int, total_seq_no: int, size: int, data: str):
        self.frame_no: int = frame_no
        self.seq_no: int = seq_no
        self.total_seq_no: int = total_seq_no
        self.size: int = size
        self.data: str = data

    def pack(self):
        return struct.pack("!IIII{}s".format(self.size), self.frame_no, self.seq_no, self.total_seq_no, self.size,
                           self.data)

    def to_dict(self) -> Dict:
        return {
            "frame_no": self.frame_no,
            "seq_no": self.seq_no,
            "total_seq_no": self.total_seq_no,
            "size": self.size,
            "data": self.data
        }

    @staticmethod
    def unpack(msg):
        t = struct.unpack("!IIII{}s".format(len(msg) - 4 * 4), msg)
        return Packet(t[0], t[1], t[2], t[3], t[4])  # Takes all except for the padding

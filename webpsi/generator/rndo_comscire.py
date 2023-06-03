from webpsi.generator.base import Generator
from randonautentropy import rndo, temporal
import requests
import os

class Randonautica_QRNG(Generator, id='rndo', bit_numbering=Generator.BitNumbering.UNKNOWN):
    def get_bytes(self, length):
        return bytes.fromhex(rndo.get(length))

class Temporal_QRNG(Generator, id='temporal', bit_numbering=Generator.BitNumbering.UNKNOWN):
    def get_bytes(self, length):
        return bytes.fromhex(temporal.get(length))
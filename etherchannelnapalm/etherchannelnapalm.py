# -*- coding: utf-8 -*-
"""etherchannelnapalm.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yzrPnqfA9OqzCv_Xl5voVGo1mNGiykms
"""

import napalm
from napalm import get_network_driver
import time
import os


def init(self, hostname=None, username=None, password=None):
    driver = get_network_driver("ios")
    self.connection = driver('192.168.122.33', 'pythonauto', 'python123')


def connect(self):
    self.connection.open()

def get_facts(self):
    self.connect()
    facts = self.connection.get_facts()
    #time stamped file creating to save the config with jason indent
    current_time = time.strftime("%m.%d.%y %H:%M", time.localtime())
    output_name = 'networkreportcorelayer%s.txt' % current_time
    print(output_name)
    facts2 = json.dumps(facts, 4)
    print(facts2)
    output_file = open(output_name, "w+")
    output_file.write(facts2)
    output_file.close()

    # uploading timestamped file to github

def get_interfaces(self):
    self.connect()
    facts3 = self.connection.get_interfaces()
    facts4 = json.dumps(facts3, 4)
    print(facts4)
    current_time = time.strftime("%m.%d.%y %H:%M", time.localtime())
    output_name = 'interfacedetails%s.txt' % current_time
    output_file = open(output_name, "w+")
    output_file.write(facts4)
    output_file.close()

def disconnect(self):
    self.connection.close()
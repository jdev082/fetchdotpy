#!/usr/bin/env python3
# jdev082, 2023, MIT license
# fetchdotpy - fetch.py
import platform
import os
from os.path import exists
from pathlib import Path
import sys 
import subprocess
import socket
import lib.cpuinfo as cpuinfo
from gpuinfo import GPUInfo

# variables
name = platform.system()
release =  platform.release()
hostname = socket.gethostname()
user = os.environ.get('USER', os.environ.get('USERNAME'))
cpu = cpuinfo.cpu.info[0]['model name']

# hard-coded config and config init
class DefaultConfig:
    name = True
    release = True
    userinf = True
    cpu = True
    gpu = True

sys.path.insert(0, f'{Path.home()}/fetch/')

try:
    from config import Config as conf
except ImportError:
    conf = DefaultConfig()

# print system information     
if getattr(conf, 'userinf', 'True') == True:
    print(f'Hostname: {user}@{hostname}')
if getattr(conf, 'name', 'True') == True:
    print(f'OS: {name}')
if getattr(conf, 'release', 'True') == True:
    print(f'Release: {release}')
if getattr(conf, 'cpu', 'True') == True:
    print(f'CPU: {cpu}')
if getattr(conf, 'gpu', 'True') == True:
    print(f'GPU: Cannot display.')

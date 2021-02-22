import os
import sys
import random
from colorama import init, Fore, Back, Style
import time
from time import sleep

from bricks import *
from input import *
import signal



hight=os.get_terminal_size().lines-3
width=os.get_terminal_size().columns

#paddle positions
x=hight-5
y=10


#!/bin/bash/env python2

from random import *
import deck
import time

card_count = 52

while card_count > 0:
    print(deck.card[(card_count)])
    card_count-=1
    time.sleep(0.3)
    
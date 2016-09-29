# Tide App for listening to BBC Radio
#
#   @left_button.press
#   @midleft_button.press
#   @midright_button.press
#   @right_button.press

import tingbot
import json
import atexit
from tingbot import *
from subprocess import Popen, check_call


with open('stations.json') as stations_file:    
    stations = json.load(stations_file)

state = {
  'station': 0,
  'volume': 10,
  'playing': None
}

proc = None


@atexit.register
def stop_stream():
    global proc
    if proc != None:
        proc.terminate();

def start_stream(stream_url):
    global proc
    stop_stream()
    proc = Popen(['mpg123', '-@', stream_url], env={"PATH": "/usr/local/bin:/usr/bin"})

def set_volume(percent):
    check_call(["amixer", "set", "PCM", str(percent) + '%'])

@left_button.press
def press():
    state['station'] -= 1
    if state['station'] < 0:
        state['station'] = len(stations) - 1

@right_button.press
def press():
    state['station'] += 1
    if state['station'] >= len(stations):
        state['station'] = 0

@midleft_button.press
def press():
    state['volume'] -= 10
    if state['volume'] < 0:
        state['volume'] = 0
    set_volume(state['volume'])

@midright_button.press
def press():
    state['volume'] += 10
    if state['volume'] >= 100:
        state['volume'] = 100
    set_volume(state['volume'])

@every(seconds=0.1)
def loop():
    station = stations[state['station']]
    screen.image(station['logo'])
    if state['station'] != state['playing']:
        start_stream(station['stream']['url'])
        state['playing'] = state['station']

tingbot.run()

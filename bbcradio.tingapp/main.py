# Tide App for listening to BBC Radio
#
#   @left_button.press
#   @midleft_button.press
#   @midright_button.press
#   @right_button.press

import tingbot
import json
from tingbot import *


with open('stations.json') as stations_file:    
    stations = json.load(stations_file)

state = {
  'station': 0
}

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

@every(seconds=0.1)
def loop():
    station = stations[state['station']]
    screen.image(station['logo'])

tingbot.run()

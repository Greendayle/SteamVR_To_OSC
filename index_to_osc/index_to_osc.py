import json
import openvr
import sys
import os
import shutil
import time
from pythonosc import udp_client
client_osc = udp_client.SimpleUDPClient("127.0.0.1", 9000)


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


# application = openvr.init(openvr.VRApplication_Overlay)
application = openvr.init(openvr.VRApplication_Utility)
action_path = os.path.join(resource_path('bindings'),
                           'index_bypasser_actions.json')

print(action_path)

openvr.VRInput().setActionManifestPath(action_path)


action_set_bypasser = openvr.VRInput().getActionSetHandle('/actions/bypasser')

input2d1 = openvr.VRInput().getActionHandle('/actions/bypasser/in/input2d1')
input2d2 = openvr.VRInput().getActionHandle('/actions/bypasser/in/input2d2')
input2d3 = openvr.VRInput().getActionHandle('/actions/bypasser/in/input2d3')
input2d4 = openvr.VRInput().getActionHandle('/actions/bypasser/in/input2d4')

input1d1 = openvr.VRInput().getActionHandle('/actions/bypasser/in/input1d1')
input1d2 = openvr.VRInput().getActionHandle('/actions/bypasser/in/input1d2')
input1d3 = openvr.VRInput().getActionHandle('/actions/bypasser/in/input1d3')
input1d4 = openvr.VRInput().getActionHandle('/actions/bypasser/in/input1d4')

bool_amount = 30
inputbools = []
for i in range(bool_amount):
    inputbool = openvr.VRInput().getActionHandle('/actions/bypasser/in/inputbool{}'.format(i + 1))
    inputbools.append(inputbool)

config_file_path = os.path.join(os.path.join(resource_path('config.json')))
if not os.path.exists(config_file_path):
    shutil.copyfile(config_file_path + '.template', config_file_path)
config = json.load(open(os.path.join(os.path.join(resource_path('config.json')))))

def handle_input():
    event = openvr.VREvent_t()
    has_events = True
    while has_events:
        has_events = application.pollNextEvent(event)
    action_sets = (openvr.VRActiveActionSet_t * 1)()
    action_set = action_sets[0]
    action_set.ulActionSet = action_set_bypasser
    openvr.VRInput().updateActionState(action_sets)

    x =  openvr.VRInput().getAnalogActionData(input2d1,
                                             openvr.k_ulInvalidInputValueHandle).x
    if x!=0:
        client_osc.send_message(config["input2d1x"], float(x))
    x = openvr.VRInput().getAnalogActionData(input2d2,
                                             openvr.k_ulInvalidInputValueHandle).x
    if x != 0:
        client_osc.send_message(config["input2d2x"], float(x))
    x = openvr.VRInput().getAnalogActionData(input2d3,
                                             openvr.k_ulInvalidInputValueHandle).x
    if x != 0:
        client_osc.send_message(config["input2d3x"], float(x))
    x = openvr.VRInput().getAnalogActionData(input2d4,
                                             openvr.k_ulInvalidInputValueHandle).x
    if x != 0:
        client_osc.send_message(config["input2d4x"], float(x))

    y = openvr.VRInput().getAnalogActionData(input2d1,
                                             openvr.k_ulInvalidInputValueHandle).y
    if y != 0:
        client_osc.send_message(config["input2d1y"], float(y))

    y = openvr.VRInput().getAnalogActionData(input2d2,
                                             openvr.k_ulInvalidInputValueHandle).y
    if y != 0:
        client_osc.send_message(config["input2d2y"], float(y))

    y = openvr.VRInput().getAnalogActionData(input2d3,
                                             openvr.k_ulInvalidInputValueHandle).y
    if y != 0:
        client_osc.send_message(config["input2d3y"], float(y))

    y = openvr.VRInput().getAnalogActionData(input2d4,
                                             openvr.k_ulInvalidInputValueHandle).y
    if y != 0:
        client_osc.send_message(config["input2d4y"], float(y))



    client_osc.send_message(config["input1d1"], float(
        openvr.VRInput().getAnalogActionData(input1d1,
                                             openvr.k_ulInvalidInputValueHandle).x
    )
                            )

    client_osc.send_message(config["input1d2"], float(
        openvr.VRInput().getAnalogActionData(input1d2,
                                             openvr.k_ulInvalidInputValueHandle).x
    )
                            )
    client_osc.send_message(config["input1d3"], float(
        openvr.VRInput().getAnalogActionData(input1d3,
                                             openvr.k_ulInvalidInputValueHandle).x
    )
                            )
    client_osc.send_message(config["input1d4"], float(
        openvr.VRInput().getAnalogActionData(input1d4,
                                             openvr.k_ulInvalidInputValueHandle).x
    )
                            )

    for i in range(bool_amount):
        client_osc.send_message(config["inputbool{}".format(i+1)], int(
            openvr.VRInput().getDigitalActionData(inputbools[i],
                                                 openvr.k_ulInvalidInputValueHandle).bState
        )
                            )


while True:
    handle_input()
    time.sleep(0.005)
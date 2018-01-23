import time
import os
import json
import f2_script_reader


def validate(data):
    '''(dict) => bool
    Checks JSON file for malformed or malicious data'''
    for c in ('command','system','parameters','f2_data'):
        if c not in data:
            return False, "Invalid file " + c + " not found"
    return True, True

with open("functions.json", 'r') as file:
    functions = json.load(file)

while True:
    time.sleep(1)
    arr = os.listdir('messages')
    arr.sort()
    if arr:
        filename = "messages/" + arr[0]
        with open(filename,'r') as file:
            data = json.load(file)
            if validate(data)[0]:
                system = data['system']
                command = data['command']
                parameters = data['parameters']
                f2_data = data['f2_data']
                f2_script_reader.interpret(system, command, parameters, f2_data)
                print(1)
            else:
                print(validate(data)[1])
        os.rename(filename, 'processed_' + filename)
        time.sleep(3



                   )

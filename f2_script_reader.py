from autof2.interface import send_data # will need a local version of this that is tuneable...
from autof2.interface import window
from autof2.interface import clipboard
from autof2.navigation import navigation
from autof2.readf2 import parse

import ast
import time

def interpret(f2_system, filename, perimeters, batch):
    send = send_data.SendData()
    window.get_window()
    with open(filename, 'r') as script:
        for line in script:
            time.sleep(.1)
            cmd, data = line.split('\t')
            data = data.strip()
            cmd = cmd.strip().lower()
            if cmd == "send":
                send.send(data)
            elif cmd == "go_to":
                if data in locations:
                    locations[data]()
            elif cmd == "go_to_date":
                if data in locations:
                    locations[data](perimeters['date'])
            elif cmd == "perimeter_send":
                if data in perimeters:
                    send.send(perimeters[data])
            elif cmd == "batch":
                batch_file = batch_process[data]
                for b in batch:
                    interpret(f2_system, batch_file, b, None )
            elif cmd == "verify_screen":
                time.sleep(.5)
                data = ast.literal_eval(data)
                if not navigation.verify(data):
                    print("no")
                    return False
                else:
                    print("yes")
            elif cmd == 'sleep':
                print(11)
                time.sleep(float(data))
            elif cmd == 'perimeter_copy_paste':
                time.sleep(1)
                clipboard.set_clipbaord(perimeters[data])
                send.send('%v')
            elif cmd == "multi_paged":
                left, right, target = data.split('-')
                left = int(left)
                right = int(right)
                send.send('{HOME 3}')
                time.sleep(.3)
                next_page = parse.process_scene(window.get_window())[left:right]
                pages = [next_page]
                while True:
                    send.send('{PGDN}')
                    time.sleep(.3)
                    next_page = parse.process_scene(window.get_window())[left:right]
                    if next_page in pages:
                        break
                    else:
                        pages.append(next_page)
                send.send('{HOME 3}')
                index = 0
                for page in pages:

                    for line in page:
                        if perimeters[target] in line:
                            send.send('{DOWN %s}' % index)
                            print(index)
                            return None
                        index += 1
            elif cmd == "multi_paged_2":
                left, right, target1, target2 = data.split('-')
                left = int(left)
                right = int(right)
                print(perimeters[target1])
                print(perimeters[target2])
                send.send('{HOME 3}')
                time.sleep(.3)
                next_page = parse.process_scene(window.get_window())[left:right]
                pages = [next_page]
                while True:
                    send.send('{PGDN}')
                    time.sleep(.3)
                    next_page = parse.process_scene(window.get_window())[left:right]
                    if next_page in pages:
                        break
                    else:
                        pages.append(next_page)
                send.send('{HOME 3}')
                index = 0
                breakout = False
                for page in pages:

                    for line in page:
                        if perimeters[target1] in line and perimeters[target2] in line :
                            print(line)
                            send.send('{DOWN %s}' % index)
                            breakout = True
                            break
                        if breakout:
                            break
                        index += 1
            elif cmd == "if_not":
                window.get_window()
                target, command = data.split('-')
                if perimeters[target] not in window.get_window():
                    interpret(f2_system, command, perimeters, batch)
            elif cmd == "run_script":
                interpret(f2_system, data, perimeters, batch)
            elif cmd == 'if_not_insert':
                if data not in window.get_window():
                    print(data)
                    send.send('{INSERT}')
            elif cmd == "if_not_same_line":
                    lines = parse.process_scene(window.get_window())
                    target1, target2, command = data.split('-')
                    match = False
                    for line in lines:
                        if target1 in line and target2 in line:
                            match = True
                            break
                    if not match:
                        interpret(f2_system, command, perimeters, batch)
            elif cmd == "go_to_menu":
                command_order = data.split('-')
                navigation.to_menu(command_order)
                print("done")





locations = {"main_menu": navigation.to_main,
             "input_purchase":navigation.to_input_purchase_insert,
             "input_purchases_ps":navigation.to_input_purchase_ps_insert,
             "input_purchases_mix":navigation.to_input_purchase_mix_insert}
batch_process = {'input_purchase':'scripts/input_purchase.f2s','mix_input_purchase':'scripts/mix_input_purchase.f2s'}

if __name__ == '__main__':
    filename = 'scripts/enter_shipment.f2s'
    perimeters = {'date':'25/12/17', 'awb': '123-456-789', 'shipment_code':'61-MIAG','logistical_route':'MIA-YYZ (truck)'}
    batch = [{'assortment':'uni.B0zI5u',
                    'price': '1.05','quantity':2, 'packing':15,'supplier':'CAPRIN'}, {'assortment':'uni.B0zI5u',
                    'price': '1.05','quantity':65, 'packing':15,'supplier':'CAPRIN'}]
    interpret('f2_Canada',filename, perimeters, batch)
'''
perimeters = {'assortment':'uni.B0zI5u',
                'price': '1.05','quantity':55, 'packing':15,'supplier':'CAPRIN'}

interpret('f2_Canada','scripts/input_purchase.f2s', perimeters, None)
'''
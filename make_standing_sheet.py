from openpyxl import Workbook
from autof2.readf2 import parse
from autof2.navigation import navigation
from autof2.interface.send_data import SendData
import time

def get_data(lotts):
    data = []
    send = SendData()
    navigation.to_input_purchase('31/12/17')
    send.send('{F12}')
    time.sleep(.1)
    send.send('+{F11}')
    time.sleep(.2)
    for lott in lotts:
        send.send('{F7}')
        send.send(lott)
        send.send('{ENTER}')
        send.send('{F11}')
        time.sleep(.3)
        data.append(parse.get_input_purchase_info())
        send.send('{F12 2}')
        time.sleep(.3)
    send.send('{F12}')
    return data

lotts = ['507331','507332','507333']
f2_data = get_data(lotts)
#f2_data = [{'quantity': '1', 'box_size': 'E04', 'assortment': 'mirsweet0', 'price': '0,56', 'packing': '25', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirtopaz0', 'price': '0,56', 'packing': '25', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirnenaM5r', 'price': '0,56', 'packing': '50', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'H12', 'assortment': 'recpurpM0', 'price': '0,56', 'packing': '25', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'H12', 'assortment': 'mirsonr44g', 'price': '0,56', 'packing': '25', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirsweuM5r', 'price': '0,56', 'packing': '25', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirearlM0', 'price': '0,58', 'packing': '100', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirfrees4o', 'price': '0,59', 'packing': '100', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirhotpM0', 'price': '0,56', 'packing': '125', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirnenaM0', 'price': '0,48', 'packing': '100', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirchekm71', 'price': '0,56', 'packing': '25', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirfirlM0', 'price': '0,56', 'packing': '25', 'supplier': 'CAROPR'}, {'quantity': '10', 'box_size': 'Q06', 'assortment': 'mirfreed81', 'price': '0,44', 'packing': '100', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirfreed81', 'price': '0,55', 'packing': '100', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirredpM0', 'price': '0,50', 'packing': '100', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirredpM6r', 'price': '0,52', 'packing': '100', 'supplier': 'CAROPR'}, {'quantity': '1', 'box_size': 'Q06', 'assortment': 'mirpolsM5w', 'price': '0,56', 'packing': '100', 'supplier': 'CAROPR'}]

wb = Workbook()
ws = wb.active
ws.title="standing"
#create_sheet("standing")
#wb.remove_sheet("Sheet")
headings = list(f2_data[0].keys())
headings.sort()

ws.append(headings)
for d in f2_data:
    line = []
    for h in headings:
        line.append(d[h])
    ws.append(line)
wb.save("standings/terranova.xlsx")
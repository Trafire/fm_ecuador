import number_message
import json

def make_json(command,f2_system, date, awb, shipment_code, logistical_route,supplier,invoice_num, f2_data):
    data = {
        "command": command,
        "system": f2_system,
        "parameters": {"date": date, "awb": awb, "shipment_code": shipment_code,
                       "logistical_route": logistical_route, "supplier": supplier, "invoice_num": invoice_num},
        "f2_data": f2_data
    }
    request_type = command[command.rindex('/') + 1:].strip('.f2s').strip()
    filename = number_message.next_filename(request_type)
    with open('messages/%s' % filename, 'w') as file:
        json.dump(data, file)

command = "scripts/enter_shipment_mix.f2s"
f2_system = "f2Canada"
date = "07/12/17"
awb = "123-456-789"
shipment_code = "49-MIAG3"
logistical_route = "MIA-YYZ (truck)"
supplier = "CADENS"
invoice_num = "9876"
f2_data = [{"assortment":"flxmagti0", "box_size":"H10",
    "price": "1.85","quantity":17, "packing":25,"supplier":supplier}]
make_json(command,f2_system, date, awb, shipment_code, logistical_route,supplier,invoice_num, f2_data)
supplier = "CACHIL"
f2_data = [{"assortment":"flxmagti0", "box_size":"H10",
    "price": "1.85","quantity":17, "packing":25,"supplier":supplier}]
make_json(command,f2_system, date, awb, shipment_code, logistical_route,supplier,invoice_num, f2_data)
supplier = "CAROSA"
f2_data = [{"assortment":"flxmagti0", "box_size":"H10",
    "price": "1.85","quantity":17, "packing":25,"supplier":supplier}]
make_json(command,f2_system, date, awb, shipment_code, logistical_route,supplier,invoice_num, f2_data)

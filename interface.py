import easygui
import make_json
import excel_to_dict

def enter_mix_shipment():
    command = "scripts/enter_shipment_mix2.f2s"
    f2_system = "f2Canada"
    fields = ["date","awb", "Shipment Code"]
    date, awb, shipment_code = get_info(fields)
    logistical_route = get_shipment()
    filename = easygui.fileopenbox(default='standings')
    invoice_num = easygui.enterbox("enter invoice num")
    f2_data = excel_to_dict.get_dict(filename)
    supplier = f2_data[0]["supplier"]

    commands = []
    commands.append((command,f2_system, date, awb, shipment_code, logistical_route,supplier,invoice_num, f2_data))

    while easygui.boolbox("do you have additional invoices to enter?"):
        filename = easygui.fileopenbox(default='standings')
        invoice_num = easygui.enterbox("enter invoice num")
        f2_data = excel_to_dict.get_dict(filename)
        supplier = f2_data[0]["supplier"]
        commands.append((command, f2_system, date, awb, shipment_code, logistical_route, supplier, invoice_num, f2_data))

    for c in commands:
        make_json.make_json(*c)
    print("enter_mix_shipment")
    #make_json.make_json(command,f2_system, date, awb, shipment_code, logistical_route,supplier,invoice_num, f2_data)



def enter_direct_shipment():
    command ="scripts/purchasing_script.f2s"
    awb, shipment_code, logistical_route, invoice_num = '', '', '', ''
    f2_system = "f2Canada"
    fields = ["date"]
    date = get_info(fields)[0]
    filename = easygui.fileopenbox(default='standings')
    f2_data = excel_to_dict.get_dict(filename)
    print(f2_data)
    supplier = f2_data[0]["supplier"]

    commands = []
    commands.append((command, f2_system, date, awb, shipment_code, logistical_route, supplier, invoice_num, f2_data))
    while easygui.boolbox("do you have additional invoices to enter?"):
        filename = easygui.fileopenbox(default='standings')
        f2_data = excel_to_dict.get_dict(filename)
        supplier = f2_data[0]["supplier"]
        commands.append(
            (command, f2_system, date, awb, shipment_code, logistical_route, supplier, invoice_num, f2_data))
    for c in commands:
        make_json.make_json(*c)



def purchase_normal():
    command = "scripts/purchasing_script.f2s"
    f2_system = "f2Canada"

    
'''
def enter_from_assortment_direct():
    command = "scripts/purchasing_script.f2s"
    awb, shipment_code, logistical_route, invoice_num = '', '', '', ''
    f2_system = "f2Canada"
    fields = ["date"]
    date = get_info(fields)[0]
    filename = easygui.fileopenbox(default='standings')
    assortment = excel_to_dict.get_dict(filename)

    filenames = []
    for






    supplier = f2_data[0]["supplier"]

    commands = []
    commands.append((command, f2_system, date, awb, shipment_code, logistical_route, supplier, invoice_num, f2_data))
    while easygui.boolbox("do you have additional invoices to enter?"):
        filename = easygui.fileopenbox(default='standings')
        f2_data = excel_to_dict.get_dict(filename)
        supplier = f2_data[0]["supplier"]
        commands.append(
            (command, f2_system, date, awb, shipment_code, logistical_route, supplier, invoice_num, f2_data))
    for c in commands:
        make_json.make_json(*c)
'''

def get_info(fieldNames):
    title = "Get Shipment Info"
    msg = "Fill in details below"
    return easygui.multenterbox(msg,title, fieldNames)

def get_shipment():
    title = "Logistics"
    msg = "Choose Shipment"
    choices = ['BOG-MIA-YUL (consol.)', 'BOG-MIA-YYZ (consol.)', 'BOG-YUL, American Airl.', 'BOG-YUL, Cubana',
               'BOG-YYZ, American Airl.', 'BOG-YYZ, Cubana', 'LIM-MIA-YUL (consol.)', 'LIM-MIA-YYZ (consol.)',
               'MDE-MIA-YUL (consol.)', 'MDE-MIA-YYZ (consol.)', 'MDE-YYZ, direct flight', 'MIA-YUL (truck)',
               'MIA-YYZ (truck)', 'UIO-MIA-YUL (consol.)', 'UIO-MIA-YYZ (consol.)', 'UIO-YUL, Direct',
               'UIO-YYZ, Direct', 'UIO-YYZ, Taca/Tampa']
    return easygui.choicebox(msg, title, choices)





commands = {'Enter Mix Shipment': enter_mix_shipment,
            "Enter Purchase direct": enter_direct_shipment}

list_item = easygui.buttonbox("What would you like to do?",
                           choices = list(commands) )

func = commands[list_item]
func()





'''
msg = "Enter your personal information"
title = "Credit Card Application"
fieldNames = ["Name","Street Address","City","State","ZipCode"]
fieldValues = []  # we start with blanks for the values
fieldValues = easygui.multenterbox(msg,title, fieldNames)

# make sure that none of the fields was left blank
while 1:
    if fieldValues == None: break
    errmsg = ""
    for i in range(len(fieldNames)):
      if fieldValues[i].strip() == "":
        errmsg = errmsg + ('"%s" is a required field.\n\n' % fieldNames[i])
    if errmsg == "": break # no problems found
    fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
print ("Reply was:", fieldValues)

'''


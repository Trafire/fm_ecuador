from autof2.navigation import navigation
from autof2.readf2 import parse

import sqlite3



def filter_category_packing(category, packing):
    data = c.execute('''Select * from f2data where category="%s" AND packing="%s"''' % (category, packing)).fetchall()
    return data

def filter_category(category):
    data = c.execute('''Select * from f2data where category="%s"''' % category).fetchall()
    return data

def get_list(category):
    navigation.to_assortment_category(category)
    products = parse.parse_assortment_category_section(category)
    for p in products:
        add_item(p)

def add_item(product):
    c.execute("INSERT OR IGNORE INTO f2data (code, category, assortment, colour, length, quality, packing ) VALUES %s" % str(product))
    conn.commit()

def add_to_supplier(supplier_code, assortment_code):
    supplier_code = supplier_code.upper()
    c.execute(
        "INSERT OR IGNORE INTO supplier_assortment (assortment_code, supplier_code) VALUES %s" % str(
            (assortment_code,supplier_code)))
    conn.commit()

def get_supplier_list(supplier):
    supplier = supplier.upper()
    data = c.execute('''Select * from supplier_assortment where supplier_code="%s"''' % supplier).fetchall()
    return data



conn = sqlite3.connect('data/buying.db')
c = conn.cursor()

#category = 'Lisi ON'
#assortment_code = 'lioontar+w'
#supplier_code = 'CAROSA'
#add_to_supplier(supplier_code, assortment_code)

#get_list(category)
#print(filter_category(category))
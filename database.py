import sqlite3

conn = sqlite3.connect('data/buying.db')
c = conn.cursor()

def filter_category_packing(category, packing):
    data = c.execute('''Select * from f2data where category="%s" AND packing="%s"''' % (category, packing)).fetchall()
    return data

def filter_category(category):
    data = c.execute('''Select * from f2data where category="%s"''' % category).fetchall()
    return data

print(filter_category("Vari M"))
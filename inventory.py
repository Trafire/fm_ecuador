from openpyxl import Workbook, load_workbook
wb = load_workbook('standings/Queens.xlsx')
ws = wb["Sheet"]

data = []
index = 0
for line in ws:
    if index == 0:
        header = []
        for cell in line:
            if cell.value == None:
                break
            header.append(str(cell.value).strip('='))
        index += 1
    else:
        col = 0
        l = {}
        for cell in line:
            if cell.value == None:
                break
            l[header[col]] =  str(cell.value).strip('=')
            col += 1
        data.append(l)



print(data)
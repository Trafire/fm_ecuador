def next_filename(request_type):
    with open('settings/current_number.txt','r') as file:
        num = int(file.readline().strip())
    with open('settings/current_number.txt', 'w') as file:
        file.write(str(num + 1))
    return '%012d_%s.json' % (num,request_type)


from autof2.readf2 import parse
from autof2.interface import window


total = []
w = parse.process_scene(window.get_window())

for target in ('Q06',):
    i = 0
    for line in w:
        if target in line:
            total.append((target, i, line.index(target)))
            break
        i += 1

print(total)

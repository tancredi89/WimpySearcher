import pandas as pd 
from pathlib import Path 


def split(word): 
    return list(word) 

lines = []

passes = [{},{},{}]

for i in range(1,4):
    wimpy_name = 'wimpy_m0{0}'.format(i)

    with open("""P:\groups\OPS\EPS System Ops\Wimpys\\{0}""".format(wimpy_name),'r') as file:
        content = file.readlines()
        file.close()
        for c in content:
            lines.append(c.split('\n'))

    for x,l in enumerate(lines):
        if l == ['']:
            lines.remove(l)
        elif '-' not in l[0]:
            lines.remove(l)
        elif l == [' --------------- - - -------  ---------  ---------  ---------  ---------  ---------  ---------  ---------']:
            lines.remove(l)
        elif 'Wimpy' in l[0]:
            lines.remove(l)
        else:
            if len(lines[x]) > 1:
                del lines[x][1] 
            StringLineBefore = split(str(lines[x-1]))
            StringLine = split(str(l))
            orbit = ''
            for o in range(23,29):
                orbit = orbit+StringLine[o]
            
            time = ''
            for t in range(6,19):
                time = time + StringLine[t]
            
            Az = ''
            if '*' in StringLine[0:40] and '*' not in StringLineBefore[0:40] and 'l' not in StringLineBefore[0:40]: 
                for a in range(32,35):
                    Az = Az + StringLine[a]
                # print(wimpy_name)
                # print("Before: ",StringLineBefore[0:40])
                # print("After: ",StringLine[0:40])
                Az = int(Az)
                if Az > 260:
                    Az = Az - 360
                passes[i-1]["M0{1}-{0}-Az".format(orbit,i)] = str(Az)

            if StringLine[39] == 'a' and (StringLine[40] == '1' or StringLine[40] == '2'):

                passes[i-1]["M0{1}-{0}-AOS".format(orbit,i)] = time
            elif StringLine[39] == 'A':
                passes[i-1]["M0{1}-{0}-AOS5".format(orbit,i)] = time
            elif StringLine[39] == 'L':
                passes[i-1]["M0{1}-{0}-LOS5".format(orbit,i)] = time
            elif StringLine[39] == 'l':
                passes[i-1]["M0{1}-{0}-LOS".format(orbit,i)] = time


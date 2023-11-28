#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if i == ord('e') or i == ord('f'):
        continue
    print('{}' .format(chr(i)), end='')

'''
recaman.py

hopefully the accent on the a doesn't end up obfuscaing the title

This file contains a function to creates the Recaman seqeunce

Time:
    O(n)
Space:
    O(n)

Seems Optimal
'''

# returns the recaman sequence up to when some
# element is greater than n
def recaman(n):
    increment = 1
    recaman = [0]
    while True:
        back = recaman[-1] - increment
        forward = recaman[-1] + increment
        if back > 0 and back not in recaman:
            recaman.append(back)
        elif forward <= n:
            recaman.append(forward)
        else:
            break
        increment += 1
    return recaman

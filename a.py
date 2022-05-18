# Part one
from math import floor

with open('aInput.txt') as f:
    scans = f.readlines()


n = int(scans[0])
d = list(map(int, scans[1].split()))
h = list(map(int, scans[2].split()))
ducks = list(map(int, scans[3].split()))

times = []
total = []
for i in range(len(d)):
    for j in range(len(d)):
        total.append(floor(h[i]/(d[i]+ducks[j])))
    times.append(total)
    total =[]

for i in range(len(times)):
    print(times[i])


nums = []
matrix = []
indexes = []

        

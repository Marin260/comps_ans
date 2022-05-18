couples = int(input())
questions = int(input())


score = []
for i in range(couples):
    m = input()
    f = input()
    sum = 0
    for i in range(len(m)):
        if m[i] != f[i]:
            sum += 1
    score.append(sum)
    sum = 0

for i in range(len(score)):
    print(score[i])


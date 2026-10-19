n, m = map(int, input(). split())
data = [tuple(input(). split()) for _ in range(n)]
dbtb = [tuple(input(). split()) for _ in range(m)]
# seca = [0] * 2000000
# secb = [0] * 2000000
lista = []
listb = []
nowa = 1000000
nowb = 1000000

for idx in range(n):
    da, ta = data[idx]
    if da == 'R':
        for _ in range(int(ta)):
            nowa += 1
            lista.append(nowa)
    else:
        for _ in range(int(ta)):
            nowa -= 1
            lista.append(nowa)
     
for idx in range(m):
    db, tb = dbtb[idx]
    if db == 'R':
        for _ in range(int(tb)):
            nowb += 1
            listb.append(nowb)
    else:
        for _ in range(int(tb)):
            nowb -= 1
            listb.append(nowb)

result = -1
if len(lista) >= len(listb):
    for sec in range(len(lista)):
        if lista[sec] == listb[sec]:
            result = sec + 1
            break
else:
    for sec in range(len(listb)):
        if lista[sec] == listb[sec]:
            result = sec + 1
            break
print(result)
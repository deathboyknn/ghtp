
sber = dict()
strng = input().split()
while strng:
    if strng[0] == "WITHDRAW":
        nm, sm = strng[1], int(strng[2])
        if nm not in sber:
            sber[nm] = -sm
        else:
            sber[nm] -= sm
    elif strng[0] == "DEPOSIT":
        nm, sm = strng[1], int(strng[2])
        if nm not in sber:
            sber[nm] = sm
        else:
            sber[nm] += sm
    elif strng[0] == "BALANCE":
        nm = strng[1].rstrip()
        if nm not in sber:
            print("ERROR")
        else:
            print(sber[nm])
    elif strng[0] == "INCOME":
        pcnt = int(strng[1])
        for i in sber:
            if sber[i] > 0:
                sber[i] = sber[i] * (100 + pcnt) // 100
    else:
        nm1, nm2, sm = strng[1], strng[2], int(strng[3])
        if nm1 not in sber:
            sber[nm1] = -sm
        else:
            sber[nm1] -= sm
        if nm2 not in sber:
            sber[nm2] = sm
        else:
            sber[nm2] += sm
    try:
        strng = input().split()
    except EOFError:
        strng = ""


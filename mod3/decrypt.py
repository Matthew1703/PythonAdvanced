def decrypt(strin):
    count = 0
    strinlst = []
    encryptlst = []
    for symbol in strin:
        strinlst.append(symbol)
    for isymbol in range(len(strinlst)-1):
        if count == 1:
            count = 0
            continue
        if strinlst[isymbol] == '.' and strinlst[isymbol+1] == '.' and encryptlst:
            encryptlst.pop(-1)
            count += 1
        elif strinlst[isymbol] != '.':
            encryptlst.append(strinlst[isymbol])
    if strinlst[-1] != '.':
        encryptlst.append(strinlst[-1])

    encrypt = ''.join(encryptlst)
    return encrypt


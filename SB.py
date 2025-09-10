
def int2hex(a):
    if a < 10:
        return str(a)
    return chr(ord('A') - 10 + a)


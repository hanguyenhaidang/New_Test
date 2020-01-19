
keys=input('Enter a one character: ')
def PhoneKeyPad(n):
    n = n.upper()
    for i in n:
        if i == 'A' or i == 'C' or i == 'C' :
            print('2')
        if i == 'D' or i == 'E' or i == 'F' :
            print('3')
        if i == 'G' or i == 'H' or i == 'I' :
            print('4')
        if i == 'J' or i == 'K' or i == 'L' :
            print('5')
        if i == 'M' or i == 'N' or i == 'O' :
            print('6')
        if i == 'P' or i == 'Q' or i == 'R' or i == 'S':
            print('7')
        if i == 'W' or i == 'X' or i == 'I' or i == 'Z':
            print('8')
PhoneKeyPad(keys)
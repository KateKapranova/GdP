#program which converts binary numbers into decimals
def binToDec():
    a = 'y'
    #loop which runs as long as the user wants to convert binaries
    while (a == 'y'):
        #asking for user input
        n = input('Submit a binary number for conversion: ')
        output = 0
        #check if input is a binary number
        check = binaryCheck(n)
        if check == 0:
            continue
        #invert the string n for simplicity of conversion:
        bin = ''
        for i in range(len(n)-1,-1,-1):
            bin=bin+n[i]

        #conversion to decimal:
        for i in range(0,len(bin)):
            if bin[i]=='1':
                output = output + 2**i
        print(output)

        #ask the user if she wants to continue
        print('Do you want to continue? (y/n)')
        a = str(input())
    return 'Binary converter terminated'

#help function to check if input is binary
def binaryCheck(string):
    L = ['0', '1']
    for digit in string:
        if digit not in L:
            print('Submitted value is not binary')
            return 0
    return 1

print(binToDec())

def addStrings(string1, string2):
    x = len(string1) 
    y = len(string2)
    x_dec = x - (string1.find('.')+1)
    y_dec = y - (string2.find('.')+1)
    if (string1.find('.')== -1):
        x_dec = 0
    if (string2.find('.')== -1):
        y_dec = 0
    string1 = float(string1) * 10**(x_dec)
    string2 = float(string2) * 10**(y_dec)
    string1=str(int(string1))
    string2=str(int(string2))
    print(string1, x_dec)
    print(string2,y_dec)
    num1=0
    num2=0
    i=0
    for e in string1:
        i=i+1
        num1=num1 + int(e)*(10**(x-i))
    num1 = num1 * 10**(-x_dec)
    print("this is num1 ",num1)
    i=0
    for e in string2:
        i=i+1
        num2=num2 + int(e)*(10**(y-i))
    print("this is num2 ",num2,i,y)
    
   
    
    print(num1+num2)
    return("the sum is ",num1+num2)


def main():
    addStrings("121","2060")
    

main()

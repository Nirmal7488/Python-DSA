#1Write a Recursive function to Calculate sum of first n natural number.
#2.Write a recursive function to print first N natural number.
#3.Write a recursive function to print first N natural number in reverse order.
#4.Write a recursive function to print first N odd natural numbers.
#5.Write a recursive function to print first N even natural numbers.
#6.Write a recursive function to print first N odd natural number in reverse order.
#7.Write a recursive function to print first N even natural number in reverse order.


#1
def sum(num):
    if num == 1 or num==0:
        return num
    return num+sum(num-1)

#2
def printNatural(num):
    if num<=0:
        return 
    printNatural(num-1)
    print(num,end=" ")

#3
def revPrintNatural(num):
    if num<=0:
        return 
    print(num,end=" ")
    revPrintNatural(num-1)

#4
def printEven(num):
    if num<0:
        return
    printEven(num-1)
    if num%2==0:   
        print(num,end=" ")
    else:
        pass

#5
def revprintEven(num):
    if num<0:
        return
    if num%2==0:   
        print(num,end=" ")
    else:
        pass
    revprintEven(num-1)

#6
def printOdd(num):
    if num<0:
        return
    printOdd(num-1)
    if num%2==0:
        pass
    else:
        print(num,end=" ")

#7
def revprintOdd(num):
    if num<0:
        return
    if num%2==0:
        pass
    else:
        print(num,end=" ")
    revprintOdd(num-1)

    


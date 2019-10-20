#No By Fingre Counting 
#COOL SUPER COOL
def num(n):
    r = n % 8
    if r == 1 :
        return r
    if r == 5:
        return r
    if r == 0  or r == 2:
        return 2
    if r == 6 or r == 4:
        return 4
    if r == 3  or r == 7:
        return 3
#number = input("Take a NO: ")
#n = number
n = 4356
print(num(n))




            
        
    

#Count the given numbers on your fingers and find the correct finger on which the number ends.
# The first number starts from the thumb, second on the index finger, third on the middle finger, fourth on the ring finger and fifth on the little finger.
# Again six comes on the ring finger and so on.
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




            
        
    

def ladd(n):
    for i in range(n+1):
        print("*   *")
        print("*   *")
        if i < n:
            print("*****")

n = 5
print(ladd(n))

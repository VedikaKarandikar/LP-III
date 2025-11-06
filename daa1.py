def non_recursive_fibonacci(n):
    if n <= 0:
        print("Invalid input")
        return 0
    elif n == 1:
        print("Non-Recursive Fibonacci Series: 0")
        return 0
    a, b = 0, 1
    print("Non-Recursive Fibonacci Series:", end=" ")
    print(a, b, end=" ")
    for _ in range(2, n):
        c = a + b
        print(c, end=" ")
        a, b = b, c
    print()  
    return b

def recursive_fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)

def analyse_complexity():
    print("\nNon Recursive Fibonacci:")
    print("Time Complexity: O(n)")
    print("Space Complexity: O(1)")
    print("\nRecursive Fibonacci:")
    print("Time Complexity: O(2^n)")
    print("Space Complexity: O(n)")

n=int(input("Enter any number:"))
print("Non recursive fibonacci of ",n," is: ",non_recursive_fibonacci(n))
print("Recursive fibonacci of ",n," is: ",recursive_fibonacci(n))
print("Recursive Fibonacci Series:", end=" ")
for i in range(n):
    print(recursive_fibonacci(i), end=" ")
print()


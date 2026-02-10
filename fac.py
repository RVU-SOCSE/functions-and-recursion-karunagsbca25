#NAME-KARUNA G S
#USN-1RUA25BCA0047
#FACTORIAL USING FUNCTION

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))
print("Factorial is:", factorial(num))

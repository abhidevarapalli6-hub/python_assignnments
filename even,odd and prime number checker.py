def even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

def prime(num):
    if num <= 1:
        print(num, "is Not Prime")
        return

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(num, "is Not Prime")
            return

    print(num, "is Prime")

num = int(input("Enter a number: "))

even_odd(num)
prime(num)

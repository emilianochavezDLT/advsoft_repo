#This is homework 1 for Advanced Software Engineering 4300
#Emiliano Chavez De La Torre

def main():

    # Task 1: Introduction to Replit
    print(hello_Replit())

    # Task 2: Varaibles and Data Types
    print(int_number())
    print(float_number())
    print(string())
    print(boolean())

    # Task 3: Control Structures

    # Part A
    print(sign_check(10))
    print(sign_check(-10))
    print(sign_check(0))

    # Part B
    print(first_ten_prime_numbers())

    #part C
    print(hundred_number_sum())

    

# Task 1: Introduction to Replit
def hello_Replit():
    return "Hello Replit!"

# Task 2: Varaibles and Data Types
def int_number():
    int_num = 10
    return int_num

def float_number():
    float_num = 10.10
    return float_num

def string():
    string = "Hello World"
    return string

def boolean():
    boolean = True
    return boolean

# Task 3: Control Structures
def sign_check(num):
    sign = ""
    if num > 0:
        sign = "Positive"
    elif num < 0:
        sign = "Negative"
    else:
        sign = "Zero"
    return sign

def first_ten_prime_numbers():
    
    #using an array/list for testing purposes and convenience
    prime_nums = []

    #using a while loop to find the first 10 prime numbers
    lower = 2
    upper_limit = 30 

    for i in range (lower, upper_limit): 
        for j in range(2, i): 
            if (i % j) == 0: #if the number is divisible by any other number, it is not prime
                break
        else: #if the number is not divisible by any other number, it is prime
            prime_nums.append(i)
            if len(prime_nums) == 10:
                break
    return prime_nums

    
def hundred_number_sum():
    total = 0 
    limit = 0

    while limit < 100:
        limit += 1
        total = total + limit
    
    return total



if __name__ == "__main__":
    main()

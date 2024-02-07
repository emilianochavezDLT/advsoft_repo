#This is homework 1 for Advanced Software Engineering 4300
#Emiliano Chavez De La Torre

import numpy as np

# Task 4: Functions and Ducktyping

#If it looks like a product, scans like a product, and calculates discounts like a product, then it is a product.
class Product:
    #defining the function to calculate the discount
    def calculate_discount(self, price, discount):
        discunted_price = price * discount
        new_price = price - discunted_price
        return new_price

#If it looks like a service, drains your bank account like a service, and calculates discounts like a service, then it is a service.
class Service:
    #defining the function to calculate the discount
    def calculate_discount(self, price, discount):
        discunted_price = price * discount
        new_price = price - discunted_price
        return new_price


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

    #Task 4: Functions and Ducktyping
    product = Product()
    service = Service()
    print(product.calculate_discount(100, 0.30))
    print(service.calculate_discount(200, 0.10))

    #Task 5: Lists and Dictionaries
    
    #calling the function to return the first 3 books
    fav_books = my_favorite_books()
    print(fav_books)

    #creating a dictionary to represent a student
    student_db = student_database()

    #Task 6: File Handeling and Metaprogramming
    #calling the function to count the words in a file
    file_path = "task6file.txt"
    file_path2 = "task6file2.txt"
    print(count_words_in_file(file_path))
    print(count_words_in_file(file_path2))

    #Task 7: Package Control in Replit
    arr = np.array([1, 2, 3, 4, 5])
    print(arr)
    
    
    

    

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
# Part A
def sign_check(num):
    sign = ""
    if num > 0:
        sign = "Positive"
    elif num < 0:
        sign = "Negative"
    else:
        sign = "Zero"
    return sign

# Part B
def first_ten_prime_numbers():
    
    #using an array/list for testing purposes and convenience
    prime_nums = []

    #using a while loop to find the first 10 prime numbers
    lower = 2 #the first prime number is 2
    upper_limit = 30 #the upper limit is 30, which is just arbitrary

    for i in range (lower, upper_limit): 
        for j in range(2, i): #from 2 to the number itself
            if (i % j) == 0: #if the number is divisible by any other number, it is not prime
                break
        else: #if the number is not divisible by any other number, it is prime
            prime_nums.append(i)

            #if the list has 10 prime numbers, break the loop
            if len(prime_nums) == 10:
                break
    return prime_nums

# Part C
def hundred_number_sum():
    total = 0 
    limit = 0

    #using the while loop to find the sum of the first 100 numbers
    while limit < 100:
        #incrementing the limit and adding it to the total
        limit += 1
        total = total + limit
    
    return total


# Task 5: Lists and Dictionaries
def my_favorite_books():
    
    #using a list to store the favorite books
    fav_books = ["Beginning Python","Linear Algebra for Dummies","The Hobbit", "The Lord of the Rings", "The Odyssey"]
    
    #slicing the list to print the first 3 books
    first_three_books = fav_books[:3]
    return first_three_books

def student_database():
    student_db = {
        #The id is the occurance of the student in the dictionary
        #The student's name and student_id are stored in a dictionary
        1:{"name": "John Doe", "student_id": 1234},
        2:{"name": "Jane Doe", "student_id": 5678},
    }
    return student_db

# Task 6: File Handeling and Metaprogramming
def count_words_in_file(file_path):
    #using the with statement to open the file
    with open(file_path, 'r') as file:
        #reading the file and splitting the words
        words = file.read().split()
        #counting the words
        word_count = len(words)
    return word_count



if __name__ == "__main__":
    main()

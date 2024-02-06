from main import count_words_in_file


# Task 6: File Handeling and Metaprogramming

#Putting all of the text files in the directory into a list
text_files = [("task6file.txt", 8), ("task6file2.txt", 5)]

def create_test_function(file_path, expected_output):
    def test_count_words_in_file():
        assert count_words_in_file(file_path) == expected_output
    return test_count_words_in_file

#Dynamically creating test functions for each file in the directory
for file, exepected_count in text_files: #file and expected_count are tuples and are from the text_files list
    #So here we are splitting the file path and getting the name of the file without the extension
    test_name = f"test_{file.split('/')[-1].split('.')[0]}" #This is the name of the test function
    test = create_test_function(file, exepected_count) #This is the function that we are going to create
    
    #Resource: https://www.geeksforgeeks.org/python-globals-function/
    globals()[test_name] = test #This is creating the function in the global scope
    
    
    









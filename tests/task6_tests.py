from main import count_words_in_file
import os #Tech Doc: https://docs.python.org/3/library/os.html#files-and-directories

# Task 6: File Handeling and Metaprogramming

#We are going to dynamically generate function names for our pytest tests based on the file names in the directory
directory = "../"

#Putting all of the text files in the directory into a list
text_files = [("../task6file.txt", 8), ("../task6file2.txt", 5)]

def create_test_function(file_path, expected_output):
    def test_count_words_in_file():
        assert count_words_in_file(file_path) == expected_output
    return test_count_words_in_file

#Dynamically creating test functions for each file in the directory
for file, exepected_count in text_files:
    test_name = f"test_{file.split('/')[-1].split('.')[0]}"
    test = create_test_function(file, exepected_count)
    globals()[test_name] = test
    
    
    









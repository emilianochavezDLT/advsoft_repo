from main import count_words_in_file
import os #Tech Doc: https://docs.python.org/3/library/os.html#files-and-directories

# Task 6: File Handeling and Metaprogramming

#We are going to dynamically generate function names for our pytest tests based on the file names in the directory
directory = "../"

#Putting all of the text files in the directory into a list
text_files = [("../task6file.txt", 8), ("../task6file2.txt", 5)]

for file, expected_count in text_files:
    def test_count_words_in_file():
        assert count_words_in_file(file) == expected_count
    test_name = f"test_{file.split('/')[-1].split('.')[0]}"
    globals[test_name] = test_count_words_in_file









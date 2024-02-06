from main import count_words_in_file, text_file_test


# Task 6: File Handeling and Metaprogramming

#We are going to dynamically generate function names for our pytest tests based on the file names in the directory
directory = "../"
@text_file_test(directory)
def test_count_words_in_file(file_path):
    #We are going to use the count_words_in_file function to test the word count in the file
    assert count_words_in_file(file_path) == 8
    assert count_words_in_file(file_path) == 5








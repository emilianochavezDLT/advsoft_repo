from main import my_favorite_books, student_database

def test_my_favorite_books():
    assert my_favorite_books() == ["Beginning Python","Linear Algebra for Dummies","The Hobbit"], "should be ['Beginning Python','Linear Algebra for Dummies','The Hobbit']"

#This test should fail because it is not the first 3 books, it is the last 2 books
def fail_test_my_favorite_books():
    assert my_favorite_books() == ["The Lord of the Rings", "The Odyssey"], "should fail the test"

#This test should fail because it is not the first 3 books, it is the first two and last book
def fail_test_my_favorite_books_2():
    assert my_favorite_books() == ["The Hobbit", "The Lord of the Rings", "The Odyssey"], "should fail the test"

def test_student_database():
    assert student_database() == {1:{"name": "John Doe", "student_id": 1234}, 2:{"name": "Jane Doe", "student_id": 5678}}, "look at the main file for the dictionary"

def test_student_database_names():
    student_db = student_database()
    for id, student_dict in student_db.items():
        assert student_dict["name"] == "John Doe" and student_dict["name"] == "Jane Doe", "should be John Doe or Jane Doe"

from main import my_favorite_books, student_database

def test_my_favorite_books():
    assert my_favorite_books() == ["Beginning Python","Linear Algebra for Dummies","The Hobbit"], "should be ['Beginning Python','Linear Algebra for Dummies','The Hobbit']"



def test_student_database():
    assert student_database() == {1:{"name": "John Doe", "student_id": 1234}, 2:{"name": "Jane Doe", "student_id": 5678}}, "look at the main file for the dictionary"

def test_student_database_names():
    student_db = student_database()
    names = []
    for id, student_dict in student_db.items():
        names.append(student_dict["name"])
    assert names == ["John Doe", "Jane Doe"], "should be ['John Doe', 'Jane Doe']"

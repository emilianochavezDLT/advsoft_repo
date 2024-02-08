'''
This will test the querying of the database to make sure that the student's name is returned

class StudentTestCase(TestCase):
    def setUp(self):
        student = Student(name="John Doe", student_id=1234, age=20)
        student.save()
    
    def test_student_name(self):
        student = Student.objects.get(student_id=1234)
        self.assertEqual(student.name, "John Doe")

'''
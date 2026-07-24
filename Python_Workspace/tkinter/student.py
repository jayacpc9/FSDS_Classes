# student.py
class Student:
    def __init__(self, name, course, fees,id=None):
        self._id = id
        self._name = name
        self._course = course
        self._fees = fees

    def __str__(self):
        return f"ID : {self._id} | Student: {self._name} | Course: {self._course} | Fees: {self._fees}"

    def id(self):
        return self._id
    
    def name(self):
        return self._name

    def course(self):
        return self._course

  
    def fees(self):
        return self._fees

   


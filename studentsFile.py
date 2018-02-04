class Person:
    def __init__(self, gender, age, name, country, city):
        self.gender = gender
        self.age = age
        self.name = name
        self.country = country
        self.city = city

class Student(Person):
    score = {}
    def __init__(self, university, course, faculty):
        self.university = university
        self.course = course
        self.faculty = faculty

    def _validateEstimate(self, estimate):
        try:
            int(estimate)
        except ValueError:
            return False
        if  estimate > 0  and estimate <=100:
            return True
        else:
            return False

    def addEstimate(self, subject, estimate):
        if self._validateEstimate(estimate):
            estimation = {2: [0, 61], 3: [61, 74], 4: [74, 90], 5: [90, 100]}
            for key, value in estimation.items():
                if estimate in range (value[0], value[1]):
                    self.score[subject] = {'score':key, 'points':  estimate}

    def writeToFile(self):
        dict = self.score
        text = 'University: ' + self.university + '\n'
        text += 'Course: ' + str(self.course) + '\n'
        text += 'Faculty: ' + self.faculty + '\n'
        for key, value in dict.items():
            text += 'Subject: ' + key + ' Score: ' + str(value['score']) + '\n'
        with open ('student.txt', 'w') as f:
            f.write(text)

student = Student('Taras Schevchenko National University of Kyiv', 5, 'management')
student.gender = 'female'
student.age = 21
student.name = 'Maria'
student.country = 'Ukraine'
student.city = 'Kyiv'
student.addEstimate('Math', 90)
student.addEstimate('Economy', 95)
student.writeToFile()
print(student.score)
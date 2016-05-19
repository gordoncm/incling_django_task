from django.db import models

# the student model
# student1 = Student(first_name="Cameron", last_name="Gordon")
class Student(models.Model): 
    first_name = models.TextField(default="") 
    last_name = models.TextField(default="") 
    
    def __str__(self): 
        return "%s %s" (self.first_name, self.last_name)

# the classroom model 
# class1 = Classroom(classroom_name="Class1",student=student1)
class Classroom(models.Model): 
    classroom_name = models.TextField(default="")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default="")
    
    def __unicode__(self):
        return "{0} {1} {2}".format( self.classroom_name, self.student.first_name, self.student.last_name)
        
# the school model
# school1 = School(school_name="School1", classroom=class1)
class School(models.Model): 
    school_name = models.TextField(default="")
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, default="")
    
    def __str__(self): 
        return "%s" (self.school_name)
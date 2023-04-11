from django.db import models

class Students(models.Model):
    rollno = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class Subjects(models.Model):
    sub_code = models.CharField(max_length=10)
    sub_name = models.CharField(max_length=20)

class Marks(models.Model):
    rollno = models.ForeignKey('Students', on_delete=models.CASCADE)
    sub_code = models.ForeignKey('Subjects', on_delete=models.CASCADE)
    marks = models.IntegerField()

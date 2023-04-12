from django.db import models

class Branch(models.Model):
    br_code = models.CharField(max_length=10)
    br_name = models.CharField(max_length=50)
    def __str__(self):
        return self.br_code

class Students(models.Model):
    rollno = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE)
    def __str__(self):
        return self.rollno


class Subjects(models.Model):
    sub_code = models.CharField(max_length=10)
    sub_name = models.CharField(max_length=20)
    def __str__(self):
        return self.sub_code

class Branch_Subjects(models.Model):
    br_code=models.ForeignKey('Branch', on_delete=models.CASCADE)
    sub_code=models.ForeignKey('Subjects', on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.br_code} {self.sub_code}'

class Marks(models.Model):
    rollno = models.ForeignKey('Students', on_delete=models.CASCADE)
    sub_code = models.ForeignKey('Subjects', on_delete=models.CASCADE)
    marks = models.IntegerField()
    def __str__(self):
        return f'{self.rollno} {self.sub_code}'

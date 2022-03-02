from django.db import models

# Create your models here.

class semester(models.Model):
    semester_name = models.CharField(max_length = 250)   

    def __str__(semester):
        return semester.semester_name
    

class Course(models.Model):

    course_name = models.CharField(max_length = 250)
    course_code = models.CharField(max_length = 250)
    semester = models.ForeignKey(semester, on_delete = models.CASCADE)

    def __str__(Course):
        return Course.course_name

    def get_name(self):
        return self.course_name


class note(models.Model):
    week = models.CharField(max_length = 250)
    file_type = models.CharField(max_length = 250)
    Course = models.ForeignKey(Course, on_delete = models.CASCADE)
    file_upload = models.FileField()

    def __str__(note):
        return note.week

class submit(models.Model):
    file_upload = models.FileField(upload_to="%m/%d/%y")

class Assignment(models.Model):
    name = models.CharField(max_length = 250)
    discription = models.CharField(max_length = 250)
    submited_by = models.CharField(max_length = 250)
    Course = models.ForeignKey(Course, on_delete = models.CASCADE)
    file_upload = models.FileField()

    def __str__(assignment):
        return assignment.name

class submit(models.Model):
    file_upload = models.FileField(upload_to="%m/%d/%y")

class project(models.Model):
    name = models.CharField(max_length = 250)
    discription = models.CharField(max_length = 250)
    submited_by = models.CharField(max_length = 250)
    Course = models.ForeignKey(Course, on_delete = models.CASCADE)
    file_upload = models.FileField()

    def __str__(project):
        return project.name
        
class submit(models.Model):
    file_upload = models.FileField(upload_to="%m/%d/%y")


class sign_up(models.Model):
    first_name = models.CharField(max_length = 250)
    last_name = models.CharField(max_length = 250)
    student_class = models.CharField(max_length = 250)
    phone_number = models.CharField(max_length = 250)
    password = models.CharField(max_length = 250)
    student_ID = models.CharField(max_length = 250)


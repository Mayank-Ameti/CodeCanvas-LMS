from django.db import models

# Instructor Model
class Instructor(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    phone_num=models.CharField(max_length=100)
    skills = models.CharField(max_length=100, default='')
    class Meta:
        verbose_name_plural="1. Instructor"


# Student Model
class Student(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    qualification=models.CharField(max_length=100)
    phone_num=models.CharField(max_length=100)
    address=models.TextField()
    interested_categories = models.TextField()
    class Meta:
        verbose_name_plural="4. Student"



# Course Category Model
class CourseCategory(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()

    class Meta:
        verbose_name_plural="2. Course Categories"

# Course  Model
class Course(models.Model):
    category=models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    instrctor=models.ForeignKey(Instructor, on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    description=models.TextField()
    class Meta:
        verbose_name_plural="3. Courses"
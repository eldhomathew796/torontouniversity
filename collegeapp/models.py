from django.db import models

# Create your models here.

class department(models.Model):
    name=models.CharField(max_length=225)

    def __str__(self):
        return self.name
class course(models.Model):
    name=models.CharField(max_length=225)
    department=models.ForeignKey(department,on_delete=models.CASCADE) 

    def __str__(self):
        return self.name   

class studentdetails(models.Model):
    name=models.CharField(max_length=255)
    Dob=models.CharField(max_length=255)
    age=models.IntegerField(blank=True,null=True)
    gender=models.CharField(max_length=255)
    phonenumber=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    address=models.CharField(max_length=255)
    purpose=models.CharField(max_length=255,blank=True,null=True)
    course=models.ForeignKey(course,on_delete=models.SET_NULL, blank=True, null=True)
    department=models.ForeignKey(department,on_delete=models.SET_NULL, blank=True, null=True)
    
    def __str__(self):
        return self.name  
    
    
    
# from django.db import models


# class Country(models.Model):
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


# class City(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)

#     def __str__(self):
#         return self.name


# class Person(models.Model):
#     name = models.CharField(max_length=124)
#     country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
#     city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

#     def __str__(self):
#         return self.name    
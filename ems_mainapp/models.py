from email.policy import default
from django.db import models

# the model which we used as foreign key must be defined first.
class Department(models.Model):
  # dept_id = models.IntegerField(primary_key=True,default=0)
  name = models.CharField(max_length=25,null=False)
  location = models.CharField(max_length=25)

  def __str__(self):
    return "%s"%(self.name)

class Role(models.Model):
  # role_id = models.IntegerField(primary_key=True,default=0)
  name = models.CharField(max_length=25,null=False)

  def __str__(self):
    return "%s"%(self.name)

class Employee(models.Model):
  # emp_id = models.IntegerField(primary_key=True,default=0)
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  dept = models.ForeignKey(Department,on_delete=models.CASCADE)
  salary = models.IntegerField(default=0)
  bonus = models.IntegerField(default=0)
  role = models.ForeignKey(Role,on_delete=models.CASCADE)
  phone = models.IntegerField(default=0)
  joining_date = models.DateField()

  def __str__(self):
    return "%s %s %s" % (self.first_name,self.last_name,self.phone)
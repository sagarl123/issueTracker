from django.db import models
from users.models import CustomUser 
from django.urls import reverse 
# Create your models here.
issues = (('Checkout problem at evening','Checkout problem at evening'),('Takes multiple attempt to checkout','Takes multiple attempt to checkout'),('Face model trained but models does not recognize','Face model trained but models does not recognize'))

class Issue(models.Model):
    employeeId = models.ForeignKey(CustomUser, on_delete= models.CASCADE)
    issue = models.CharField(max_length=200, choices = issues, default=' ')
    
    def __str__(self):
        return self.issue 
    
    def get_absolute_url(self):
        return reverse('issueDetail', args = [str(self.id)])
    

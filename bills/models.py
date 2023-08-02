from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.urls import reverse
# Create your models here.
def bill_Date_default():
    start_date=date(year=2023,month=4,day=1)
    end_date=date(year=2024,month=3,day=31)
    return(start_date)
def Validate_DateRange(value):
    start_date=date(year=2023,month=4,day=1)
    end_date=date(year=2024,month=3,day=31)
    if value>=start_date and value<=end_date:
        return value
    else:
        raise ValidationError("Invalid Date Date should be between 1/04/2023 and 31/03/2024")
        
class bills(models.Model):
    bill_Date=models.DateField(verbose_name="Bill Issue Date",default=bill_Date_default(),help_text = "Please use the following format: <em>DD-MM-YYYY</em>.",validators=[Validate_DateRange])
    bill_Id=models.AutoField(primary_key=True)
    bill_No=models.CharField(max_length=20,help_text="Bill or Invoice Number",verbose_name="Bill Number")
    bill_Name=models.CharField(max_length=100,help_text="Bill Description",verbose_name="Bill Name")
    bill_Amount=models.PositiveIntegerField(help_text="Bill Amount in Rs Ps > 0",verbose_name="Bill Amount")

    class Meta:
        ordering =["bill_Date"]
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Model."""
        return reverse('model-detail-view', args=[str(self.bill_Id)])
    
    def __str__(self):
        """String for representing the Bill Name object (in Admin site etc.)."""
        return self.bill_Name    

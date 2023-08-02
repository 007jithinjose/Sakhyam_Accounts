from django.db import models
from datetime import date
from django.core.exceptions import ValidationError
from django.urls import reverse

# Create your models here.
def receipt_Date_default():
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
        
class receipts(models.Model):
    receipt_Date=models.DateField(verbose_name="Receipt Issue Date",default=receipt_Date_default(),help_text = "Please use the following format: <em>DD-MM-YYYY</em>.",validators=[Validate_DateRange])
    receipt_Id=models.AutoField(primary_key=True)
    receipt_No=models.CharField(max_length=20,help_text="Receipt or Invoice Number",verbose_name="Receipt Number")
    receipt_Name=models.CharField(max_length=100,help_text="Receipt Description",verbose_name="Receipt Name")
    receipt_Amount=models.PositiveIntegerField(help_text="Receipt Amount in Rs Ps > 0",verbose_name="Receipt Amount")

    class Meta:
        ordering =["receipt_Date"]
    def get_absolute_url(self):
        """Returns the url to access a particular instance of Model."""
        return reverse('model-detail-view', args=[str(self.receipt_Id)])
    
    def __str__(self):
        """String for representing the Receipt Name object (in Admin site etc.)."""
        return self.receipt_Name     
from django.db import models

class Dashboard(models.Model):
    Financials=models.IntegerField(default=0)
    academics=(
        ('R', 'Register_Units'),
        ('P', 'Provisional_results'),
        ('T', 'Provisional_Transcript'),
        ('E', 'Exam_Card'),
    )
    Academics=models.CharField(max_length=2,choices=academics)
    accomodation=(
        ('M', 'Mekatilili'),
        ('B', 'Blocks'),
        ('W', 'Mwangeka'),
        ('S', 'Starehe'),
    )
    Special_Exams=models.CharField(max_length=200)
    Accomodation=models.CharField(max_length=1,choices=accomodation)





    

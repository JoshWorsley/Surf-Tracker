from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

class Surfer(models.Model):
    Name = models.CharField(max_length=50)
    Preferd_Waves = models.DecimalField(decimal_places=1,max_digits=4)

    def __str__(self) -> str:
        return self.Name
    
class Session(models.Model):
    Spot = models.CharField(max_length=100)
    tide = models.CharField(max_length=100)
    Wind = models.IntegerField()
    Height = models.DecimalField(decimal_places=1,max_digits=4)
    Surfer = models.ForeignKey(Surfer,on_delete=models.PROTECT)
    Quality = models.IntegerField(validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    
    def __str__(self) -> str:
        return self.Spot




from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

class Surfer(models.Model):
    Name = models.CharField(max_length=50)
    Preferd_Break = models.CharField(max_length=5,choices=(
            ('Beach', 'beach'),
            ('Reef', 'reef'),
            ('River', 'river'),
             ('Point', 'point'),
       
        ))
    Preferd_Spot = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.Name
    
class Session(models.Model):
    Spot = models.CharField(max_length=100)
    # tide = models.CharField(max_length=100)
    Wind = models.CharField(max_length=3,choices=(
            ('sw', 'SW'),
            ('w', 'W'),
            ('Nw', 'NW'),
             ('N', 'n'),
            ('NE', 'ne'),
            ('E', 'e'),
            ('S', 's'),
        ))
    Height = models.DecimalField(decimal_places=1,max_digits=4)
    Surfer = models.ForeignKey(Surfer,on_delete=models.PROTECT)
    rating = models.CharField(
        max_length=4,  
        choices=(
            ('good', 'Good'),
            ('bad', 'Bad'),
            ('okay', 'Okay'),
        )
    )
    Tide = models.CharField(max_length=4,
                            choices=(
            ('high', 'High'),
            ('mid', 'Mid'),
            ('low', 'Low'),
        ),default="high"
                            )
    
    def __str__(self) -> str:
        return self.Spot




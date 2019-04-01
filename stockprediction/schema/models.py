from django.db import models
"""
def validate_age(value):
    if value>150 or value<18:
        raise ValidationError("Wrong age entered")
"""

class Users(models.Model):
    GENDER_CHOICES=(
    ('M','Male'),
    ('F','Female')
    )
    user_id = models.EmailField(primary_key=True)
    user_name = models.CharField(max_length=25)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES)
    age = models.IntegerField()
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)

class Password(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE,primary_key=True)
    password = models.CharField(max_length=25)

class Stocks(models.Model):
    stock_id = models.CharField(max_length=25,primary_key=True)
    company = models.CharField(max_length=25)
    ticker = models.CharField(max_length=25)
    industry = models.CharField(max_length=25)
    sector = models.CharField(max_length=25)


class HistoricalStockData(models.Model):
    stock_id = models.ForeignKey(Stocks, on_delete=models.CASCADE,unique=False)
    date = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()

# This will contain more recent stock data("Probably data with the past 6 months")
class RecentStockData(models.Model):
    stock_id = models.ForeignKey(Stocks, on_delete=models.CASCADE)
    date = models.DateTimeField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()

    class Meta:
        unique_together = (('stock_id','date'))

class UserStockData(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    stock_id = models.ForeignKey(Stocks, on_delete=models.CASCADE)

    class Meta:
        unique_together=(('user_id','stock_id'))

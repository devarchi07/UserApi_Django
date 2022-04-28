from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=20)
    user_id=models.AutoField(primary_key=True)
    address=models.TextField(default="[]")
    phonenumber=models.IntegerField()
    email_id=models.EmailField()
    age=models.PositiveIntegerField()
    country_code=models.IntegerField()
    profile_picture=models.ImageField(upload_to='media')
    isactive=models.BooleanField(default=False)
    
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(User, self).save(*args, **kwargs)

class Seller(models.Model):
    gstin=models.CharField(unique=True,max_length=30)
    name=models.CharField(max_length=20)
    email_id=models.EmailField()
    age=models.PositiveIntegerField()
    shop_address=models.TextField()
    user_id=models.ForeignKey(User,on_delete=CASCADE)
    phone_number=models.IntegerField()
    country_code=models.IntegerField()
    isVerified=models.BooleanField(default=False)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        return super(Seller, self).save(*args, **kwargs)



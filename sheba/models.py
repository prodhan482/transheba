from django.db import models
from django.urls import reverse
import uuid


class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    feedback = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class ComplainBox(models.Model):
    name = models.CharField(max_length=150)
    NID_no = models.IntegerField()
    email = models.CharField(max_length=150)
    report = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class createOTP(models.Model):
    code = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=11)

    def __str__(self):
        return f"{self.phone_number}"

    def save(self, *args, **kwargs):
        if self.code == "":
            self.code = str(uuid.uuid4()).replace("-", "").upper()[:4]
            return super().save(*args, **kwargs)


class post(models.Model):
    name = models.CharField(max_length=255)
    my_file = models.FileField(upload_to='')
    post_share = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class applyForRelief(models.Model):
    NID_No = models.CharField(max_length=17)
    Name = models.CharField(max_length=20)

    dhaka = 'Dhaka'
    chittagong = 'Chittagong'
    rajshahi = 'Rajshahi'
    sylhet = 'Sylhet'
    mymensingh = 'Mymensingh'
    barisal = 'Barisal'
    rangpur = 'Rangpur'
    khulna = 'Khulna'
    d = [
        (dhaka, 'Dhaka'),
        (chittagong, 'Chittagong'),
        (rajshahi, 'Rajshahi'),
        (sylhet, 'Sylhet'),
        (mymensingh, 'Mymensingh'),
        (barisal, 'Barisal'),
        (rangpur, 'Rangpur'),
        (khulna, 'Khulna'),
    ]
    Distric = models.CharField(max_length=20, choices=d, default=dhaka)
    Village = models.CharField(max_length=50)
    Phone_no = models.CharField(max_length=11)
    Birth_Date = models.DateField()
    married = 'Married'
    single = 'Single'
    m = [
        (married, 'Married'),
        (single, 'Single'),
    ]
    Marital_Status = models.CharField(max_length=10, choices=m, default=single)
    ZIP_Code = models.PositiveIntegerField()
    code = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.Phone_no}"

    def save(self, *args, **kwargs):
        if self.code == "":
            self.code = str(uuid.uuid4()).replace("-", "").upper()[:4]
            return super().save(*args, **kwargs)


class donation(models.Model):
    Name = models.CharField(max_length=15)
    Share_something = models.CharField(max_length=5000)
    Phone_no = models.IntegerField()
    married = 'Married'
    single = 'Single'
    m = [
        (married, 'Married'),
        (single, 'Single'),
    ]
    Marital_Status = models.CharField(max_length=10, choices=m, default=single)
    bkash = 'Bkash'
    nagad = 'Nagad'
    dbbl = 'DBBL'
    payment = [
        (bkash, 'Bkash'),
        (nagad, 'Nagad'),
        (dbbl, 'DBBL'),
    ]
    Payment_Method = models.CharField(
        max_length=15, choices=payment, default=bkash)
    
    dhaka = 'Dhaka'
    chittagong = 'Chittagong'
    rajshahi = 'Rajshahi'
    sylhet = 'Sylhet'
    mymensingh = 'Mymensingh'
    barisal = 'Barisal'
    rangpur = 'Rangpur'
    khulna = 'Khulna'
    d = [
        (dhaka, 'Dhaka'),
        (chittagong, 'Chittagong'),
        (rajshahi, 'Rajshahi'),
        (sylhet, 'Sylhet'),
        (mymensingh, 'Mymensingh'),
        (barisal, 'Barisal'),
        (rangpur, 'Rangpur'),
        (khulna, 'Khulna'),
    ]
    Area = models.CharField(max_length=20, choices=d, default=dhaka)

# sending sms by twilio
class Score(models.Model):
    result = models.PositiveIntegerField()

    def __sizeof__(self):
        return str(self.result)

    def save(self, *args, **kwargs):
        if self.result < 70:
            account_sid = 'ACf35d94d2877eee95ea6f214466ceb4a8'
            auth_token = 'f760596fe11e6bd8bf686cb5dd8e7ce6'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body="Very bad result- {self.result}",
                from_='+12184604033',
                to='+8801641366908'
            )

            print(message.sid)
        return super().save(*args, **kwargs)

from PIL import Image
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.
from django.db.models import Model

# def validate_slider_image(image):
#     file_size = image.file.size
#     limit_kb = 10000
#     if file_size > limit_kb * 1024:
#         raise ValidationError("Max size of Image Should Note Be More Then  1Mb" )
#     my_image = Image.open(image)
#     w, h = my_image.size
#     print(w,h)

#     if w<1000 & w>1400:
#         raise ValidationError("Image Width Should Be 1000px-1400px ")
#     if h<200:
#         raise ValidationError("Image Height Should Be 200px - 260px")
#     if h>250:
#         raise ValidationError("Image Height Should Be 200px - 260px")


class WebsiteName(Model):
    name_of_website=models.CharField(max_length=500)
    def __str__(self):
        return self.name_of_website

class Menu(Model):
    website=models.ForeignKey(WebsiteName,on_delete=models.CASCADE)
    name_of_nav_item=models.CharField(max_length=500)
    def __str__(self):
        return self.name_of_nav_item

class Sliders(Model):
    #,validators=[validate_slider_image]
    website = models.ForeignKey(WebsiteName,on_delete=models.CASCADE)
    Slider1 = models.ImageField(upload_to='static/slider_image/',default="static/default.jpg") 
    Slider2 = models.ImageField(upload_to='static/slider_image/',default="static/default.jpg")
    Slider3 = models.ImageField(upload_to='static/slider_image/',default="static/default.jpg")

class Images(Model):
    website=models.ForeignKey(WebsiteName,on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to='static/images/', default="static/default.jpg")
    image2 = models.ImageField(upload_to='static/images/', default="static/default.jpg")
    image3 = models.ImageField(upload_to='static/images/', default="static/default.jpg")
    image4 = models.ImageField(upload_to='static/images/', default="static/default.jpg")
    image5 = models.ImageField(upload_to='static/images/', default="static/default.jpg")
    image6 = models.ImageField(upload_to='static/images/', default="static/default.jpg")

class Footer(Model):
    contact_number = models.CharField(max_length=500,null=True)
    email_id = models.CharField(max_length=500,null=True)
    address = models.CharField(max_length=500,null=True)
    website = models.ForeignKey(WebsiteName, on_delete=models.CASCADE)

    def _str_(self):
        return str(self.web_name)
class ManagerLogin(Model):
    userid=models.CharField(max_length=520)
    password=models.CharField(max_length=250)
    def __str__(self):
        return self.userid

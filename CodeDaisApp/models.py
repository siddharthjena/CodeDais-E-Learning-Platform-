from django.db import models
from django.contrib.auth.models import User
from django.core.validators import validate_image_file_extension



    

class Course(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='course_images/',validators=[validate_image_file_extension])
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name
    
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_enrolled = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} enrolled in {self.course.name}"
from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    mobile_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ]
    )

    def __str__(self):
        return f"Email: {self.email}, Name: {self.name}, Mobile: {self.mobile_number}"

    @classmethod
    def create_user(cls, email, name, mobile_number):
        """Create a new user"""
        if not email:
            raise ValueError("Users must have an email address")
        if not name:
            raise ValueError("Users must have a name")
        if not mobile_number:
            raise ValueError("Users must have a mobile number")
        
        user = cls(email=email, name=name, mobile_number=mobile_number)
        user.save(using=models.db)
        return user

    def get_user_details(self):
        """Retrieve user details"""
        return {
            "email": self.email,
            "name": self.name,
            "mobile_number": self.mobile_number,
        }

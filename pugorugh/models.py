from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


GENDER = (
    ('m', 'male'),
    ('f', 'female'),
    ('u', 'unknown')
)

SIZE = (
    ('s', 'small'),
    ('m', 'medium'),
    ('l', 'large'),
    ('xl', 'extra large'),
    ('u', 'unknown'),
)

STATUS = (
    ('l', 'liked'),
    ('d', 'disliked'),
)

AGE = (
    ('b', 'baby'),
    ('y', 'young'),
    ('a', 'adult'),
    ('s', 'senior'),
)

STRELIZATION = (
    ('y', 'yes'),
    ('n', 'no'),
)


class Dog(models.Model):
    name = models.CharField(max_length=100)
    image_filename = models.CharField(max_length=30, default='')
    breed = models.CharField(max_length=255, default='unknown breed')
    age = models.IntegerField(default=1, blank=True)
    gender = models.CharField(choices=GENDER, default='unknown', max_length=15)
    size = models.CharField(choices=SIZE, default='unknown', max_length=10)
    sterilized = models.CharField(choices=STRELIZATION,
                                  default='unknwon',
                                  max_length=10)

    def __str__(self):
        return self.name


class UserDog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=10, default='undecided')

    # get_status display to get CHOICES field in django
    def __str__(self):
        return '{} {} {}'.format(self.user, self.dog, self.get_status_display())


class UserPref(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.CharField(choices=AGE, max_length=10, default='b,y,a,s')
    gender = models.CharField(choices=GENDER, max_length=15, default='f,m')
    size = models.CharField(choices=SIZE, max_length=10, default='s,m,l,xl')
    sterilized = models.CharField(choices=STRELIZATION, max_length=10, default='y,n')

    # method to save UserPref instance and associated fields using post_save
    def create_user_pref(sender, **kwargs):
        user = kwargs['instance']
        if kwargs['created']:
            user_pref = UserPref(user=user)
            user_pref.save()

    post_save.connect(create_user_pref, sender=User)

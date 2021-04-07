from django import forms 
from .models import *
from django.forms import ModelForm
class Mob(ModelForm):
    class Meta:
       model=Mobiles
       exclude=('discount',)


class Pcform(ModelForm):
    class Meta:
       model=Pc
       exclude=('discount',)


class Tvform(ModelForm):
    class Meta:
       model=Tv
       exclude=('discount',)


class Accessoriesform(ModelForm):
    class Meta:
       model=Accessories
       exclude=('discount','acctype','accfeatures','accinterfaces','acccapacity','accconnectivity')

class Appliancesform(ModelForm):
    class Meta:
       model=Appliances
       exclude=('discount','appsize','appfeatures')
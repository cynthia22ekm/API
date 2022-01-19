from rest_framework import serializers
from .models import employees,nationality


class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model=employees
        fields=('firstname','lastname','id','Gender','Nationality')

class nationalitySerializer(serializers.ModelSerializer):
    class Meta:
        model=nationality
        fields=('id','countrycode','countrydesc')


from rest_framework import serializers
from.import models

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Instructor
        fields=['id','full_name','email','password', 'qualification','phone_num','skills' ]

    
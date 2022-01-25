from rest_framework import serializers
from .models import Lecture

class StudentSerializers(serializers.ModelSerializer):
	class Meta:
		Model = Lecture
		fields = ["first_name","last_name","email","sid"]
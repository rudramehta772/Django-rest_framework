from rest_framework import serializers
from .models import Student

#Model Serializers
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name','roll','city']


#Simple Serializers
'''
class StudentSerializer(serializers.Serializer):
    #id = serializers.IntegerField()                        #To Include Id Field in serializers field
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        #print(instance.name,'******************')           #old value of the database in instence
        instance.name = validated_data.get('name', instance.name)
        #print(instance.name,'******************')           #new value of the datavase after update in instance
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance
'''
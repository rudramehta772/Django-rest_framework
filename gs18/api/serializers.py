from rest_framework import serializers
from .models import Student

#validators
#def start_with_r(value):
#    if value[0].lower() != 'r':
#        raise serializers.ValidationError('Name Should Be Start With R')

class StudentSerializer(serializers.ModelSerializer):

     #validators
    def start_with_r(value):
        if value[0].lower() != 'r':
            raise serializers.ValidationError('Name Should Be Start With R')

    name = serializers.CharField(validators = [start_with_r])

    class Meta:
        model = Student
        fields = ['id','name','roll','city']
    
    #field level Validation 
    def validate_roll(self, value):
        if value >= 50:
            raise serializers.ValidationError('Seat Full')
        return value

    #Object Level Validation
    def validate(self, data):
        Val_name = data.get('name')
        Val_city = data.get('city')
        if Val_name.lower() == 'rohit' and Val_city.lower() != 'ahmedabad':
            raise serializers.ValidationError('City Must Be Ahmedabad')
        return data
   
'''
class StudentSerializer(serializers.Serializer):
    #id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators= [start_with_r])
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
        
    #field level Validation 
    def validate_roll(self, value):
        if value >= 50:
            raise serializers.ValidationError('Seat Full')
        return value

    def validate(self, data):
        Val_name = data.get('name')
        Val_city = data.get('city')
        if Val_name.lower() == 'rohit' and Val_city.lower() != 'ahmedabad':
            raise serializers.ValidationError('City Must Be Ahmedabad')
        return data
'''
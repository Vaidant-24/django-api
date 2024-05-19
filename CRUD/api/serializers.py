from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.ModelSerializer):
    # def start_with_r(value):
    #     if value[0].lower() != 'r':
    #         raise serializers.ValidationError('Name must be start with r')
        
    # name = serializers.CharField(validators = [start_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll' , 'city']
    # name = serializers.CharField(max_length=100)
    # roll = serializers.IntegerField()
    # city = serializers.CharField(max_length=100)

    # def create(self, validated_data): #validated_data :new data submitted by user in front-end.
    #     return Student.objects.create(**validated_data)
    
    # def update(self ,instance, validated_data): #instance :old data that was already stored in database.
    #     print(instance.name)
    #     instance.name = validated_data.get('name', instance.name)
    #     print(instance.name)
    #     instance.roll = validated_data.get('roll', instance.roll)
    #     instance.city = validated_data.get('city', instance.city)
    #     instance.save()
    #     return instance
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from user.serializers import UserSerializer
from courses.models import Course

class CourseDisplaySerializer(ModelSerializer):
  
  student_no = serializers.IntegerField(source='get_enrolled_student')
  author = UserSerializer
  image_url = serializers.CharField(source='get_absolute_şmage_url')
  class Meta:
    model=Course
    fields = [
      'course_uuid',
      'title',
      'student-no',
      'author',
      'price',
      'image_url',
    ]
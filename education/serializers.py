from rest_framework import serializers
from rest_framework.fields import SerializerMethodField, IntegerField
from rest_framework.relations import SlugRelatedField

from education.models import Course, Lesson, Payment, Subscription
from education.validators import VideoValidator
from users.models import User


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'preview', 'description')


class CourseListSerializer(serializers.ModelSerializer):
    lessons_count = IntegerField()

    class Meta:
        model = Course
        fields = ('pk', 'title', 'description', 'lessons_count')


class CourseDetailSerializer(serializers.ModelSerializer):
    this_course_lessons = SerializerMethodField()

    def get_this_course_lessons(self, course):
        return [lesson.title for lesson in Lesson.objects.filter(course_lesson=course)]

    class Meta:
        model = Course
        fields = ('pk', 'title', 'preview', 'description', 'this_course_lessons')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        validators = [VideoValidator(field='link')]
        fields = ('pk', 'title', 'preview', 'link', 'course_lesson', 'buyer')


class LessonListSerializer(serializers.ModelSerializer):
    course_lesson = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    buyer = SlugRelatedField(slug_field='email', queryset=User.objects.all())

    class Meta:
        model = Lesson
        validators = [VideoValidator(field='link')]
        fields = ('pk', 'title', 'preview', 'link', 'course_lesson', 'buyer')


class LessonDetailSerializer(serializers.ModelSerializer):
    course_lesson = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    count_lesson_with_same_course = SerializerMethodField()

    def get_count_lesson_with_same_course(self, lesson):
        return Lesson.objects.filter(course_lesson=lesson.course_lesson).count()

    class Meta:
        model = Lesson
        validators = [VideoValidator(field='link')]
        fields = ('pk', 'title', 'preview', 'description', 'link', 'course_lesson', 'count_lesson_with_same_course')


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('pk', 'user', 'payment_date', 'paid_course', 'paid_lesson', 'payment_amount', 'payment_method')


class PaymentListSerializer(serializers.ModelSerializer):
    user = SlugRelatedField(slug_field='email', queryset=User.objects.all())
    paid_course = SlugRelatedField(slug_field='title', queryset=Course.objects.all())
    paid_lesson = SlugRelatedField(slug_field='title', queryset=Lesson.objects.all())

    class Meta:
        model = Payment
        fields = ('pk', 'user', 'payment_date', 'paid_course', 'paid_lesson', 'payment_amount', 'payment_method')


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'

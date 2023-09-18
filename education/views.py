import stripe
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, status
from rest_framework.filters import OrderingFilter
from rest_framework.generics import RetrieveAPIView, DestroyAPIView, ListAPIView, UpdateAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from education.models import Course, Lesson, Payment
from education.paginators import Pagination
from education.serializers import CourseSerializer, LessonSerializer, LessonDetailSerializer, CourseDetailSerializer, \
    LessonListSerializer, CourseListSerializer, PaymentListSerializer, PaymentSerializer, SubscriptionSerializer, \
    PaymentRetrieveSerializer, PaymentCreateSerializer
# from education.services import checkout_session, create_payment
from users.permissions import IsBuyer, IsModerator


class CourseViewSet(viewsets.ModelViewSet):
    """ Viewset for course"""

    serializer_class = CourseDetailSerializer
    permission_classes = [IsAuthenticated, IsBuyer | IsModerator]
    queryset = Course.objects.annotate(lessons_count=Count('lesson'))
    pagination_class = Pagination
    default_serializer = CourseSerializer
    serializers = {
        'list': CourseListSerializer,
        'retrieve': CourseDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)


class LessonListView(ListAPIView):
    """ Lesson list API View """

    serializer_class = LessonListSerializer
    queryset = Lesson.objects.all()
    pagination_class = Pagination
    permission_classes = [IsAuthenticated]


class LessonDetailView(RetrieveAPIView):
    """ Lesson detail API View """

    serializer_class = LessonDetailSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer | IsModerator]


class LessonCreateView(CreateAPIView):
    """ Lesson create API View """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonUpdateView(UpdateAPIView):
    """ Lesson update API View """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer | IsModerator]


class LessonDeleteView(DestroyAPIView):
    """ Lesson delete API View """

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer, IsModerator]


class PaymentListView(ListAPIView):
    serializer_class = PaymentListSerializer
    queryset = Payment.objects.all()
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('paid_course', 'paid_lesson', 'payment_method')
    ordering_fields = ('payment_date',)
    permission_classes = [IsAuthenticated]


class PaymentDetailView(RetrieveAPIView):
    serializer_class = PaymentRetrieveSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


class PaymentCreateView(CreateAPIView):
    serializer_class = PaymentCreateSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsBuyer, IsModerator]

# def post(self, request, *args, **kwargs):
#     """Создание платежа"""
#     serializer = self.get_serializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     session = checkout_session(
#         paid_course=serializer.validated_data['paid_course'],
#         user=self.request.user
#     )
#     create_payment(paid_course=serializer.validated_data['paid_course'],
#                    user=self.request.user)
#     return Response({'id': session['id']}, status=status.HTTP_201_CREATED)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Lesson.objects.all()


class PaymentUpdateView(UpdateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


class PaymentDeleteView(DestroyAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsModerator]


class SubscriptionCreateAPIView(CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Lesson.objects.all()


class SubscriptionDestroyAPIView(DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Lesson.objects.all()

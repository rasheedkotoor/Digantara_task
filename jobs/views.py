from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from rest_framework.response import Response
from rest_framework import status
from .tasks import schedule_job


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        job = serializer.save()
        # Schedule the job based on interval
        schedule_job.delay(job.id, job.interval)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response(response.data, status=status.HTTP_201_CREATED)

class JobDetail(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

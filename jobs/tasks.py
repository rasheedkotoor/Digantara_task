from celery import shared_task
from .models import Job
from django.utils import timezone
import datetime

@shared_task
def execute_job(job_id):
    try:
        job = Job.objects.get(id=job_id)
        # Dummy job logic (e.g., send an email, perform computations)
        print(f"Executing job: {job.name}")
        job.last_run = timezone.now()
        job.save()
        # Schedule the next run
        schedule_job(job_id, job.interval)
    except Job.DoesNotExist:
        print(f"Job with ID {job_id} does not exist.")

@shared_task
def schedule_job(job_id, interval):
    # Simple POC logic for scheduling based on interval
    # For example, if interval is "every Monday", schedule for next Monday
    job = Job.objects.get(id=job_id)
    now = timezone.now()

    if interval.lower() == 'every monday':
        next_run = now + datetime.timedelta(days=(7 - now.weekday()))
    elif interval.lower() == 'every day':
        next_run = now + datetime.timedelta(days=1)
    else:
        # Default to next day if interval is unrecognized
        next_run = now + datetime.timedelta(days=1)

    job.next_run = next_run
    job.save()

    # Schedule the execute_job task
    execute_job.apply_async((job_id,), eta=next_run)

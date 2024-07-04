from celery import shared_task
import logging
from django.utils import timezone
from .models import StudentAnket


@shared_task
def update_course():
    logging.log(logging.INFO, 'Task update_course started!')

    curr_date = timezone.now()
    objects = StudentAnket.objects.all()

    for obj in objects:
        end_year = obj.end_study_year
        if curr_date.year <= end_year:
            start_year = obj.start_study_year
            if curr_date.year == end_year and curr_date.month > 8:
                obj.course = end_year - start_year
            elif curr_date.month < 9:
                obj.course = curr_date.year - start_year
            else:
                obj.course = curr_date.year - start_year + 1
            obj.save()

    logging.log(logging.INFO, 'Task update_course completed!')


@shared_task
def test_task():
    logging.log(logging.INFO, 'Test task executed')
    return 'Task completed'

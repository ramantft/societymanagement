from celery.decorators import task
from celery.utils.log import get_task_logger

from django.core.mail import send_mail

logger = get_task_logger(__name__)

@task(name="send_email_otp")
def send_email_otp(email_id, otp):
    logger.info("sending otp on email")
    return send_mail('Email OTP login resend',"Your otp is: " + otp,[email_id],fail_silently=False,)
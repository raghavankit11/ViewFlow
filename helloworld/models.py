from django.contrib.auth.models import User
from django.db import models
from viewflow.models import Process


class HelloWorldProcess(Process):
    text = models.CharField(max_length=150)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Response(models.Model):
    store_name = models.CharField(max_length=128, null=False, blank=False, default='public')
    rating = models.IntegerField()
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.store_name} (Response {self.id})'

AUDIT_PASS = 'AUDIT_PASS'
AUDIT_FAIL = 'AUDIT_FAIL'
APPROVE_PASS = 'APPROVE_PASS'
APPROVE_FAIL = 'APPROVE_FAIL'


AUDIT_CHOICES = (
    (AUDIT_PASS, "Audit Pass"),
    (AUDIT_FAIL, "Audit Fail"),
)

APPROVE_CHOICES = (
    (APPROVE_PASS, "Approve Pass"),
    (APPROVE_FAIL, "Approve Fail"),
)

class ResponseSubmissionProcess(Process):
    # field_agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="response_processes")
    response = models.ForeignKey(Response, on_delete=models.CASCADE, related_name="response_processes")
    is_audited = models.CharField(null=True,choices=AUDIT_CHOICES, blank=True,max_length=20, default=None)
    is_approved = models.CharField(null=True,choices=APPROVE_CHOICES, blank=True,max_length=20, default=None)





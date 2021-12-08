from django import forms
from django.utils import timezone

from .models import ResponseSubmissionProcess, Response

class FieldForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super(FieldForm, self).save(commit=False)
        # instance.approved_at = timezone.now()
        if commit:
            instance.save()
        return instance

    class Meta:
        model = Response
        fields = ['store_name', 'rating']





class AuditForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super(ApproveForm, self).save(commit=False)
        # instance.approved_at = timezone.now()
        if commit:
            instance.save()
        return instance

    class Meta:
        model = ResponseSubmissionProcess
        fields = ['is_audited']



class ApproveForm(forms.ModelForm):
    def save(self, commit=True):
        instance = super(ApproveForm, self).save(commit=False)
        # instance.approved_at = timezone.now()
        if commit:
            instance.save()
        return instance

    class Meta:
        model = ResponseSubmissionProcess
        fields = ['is_approved']


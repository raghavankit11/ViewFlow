from django.shortcuts import render, redirect

from .forms import FieldForm, AuditForm, ApproveForm


def field_response(request):
    if request.method == 'POST':
        form = FieldForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('field-response')
    else:
        form = FieldForm()
    return render(request, 'helloworld/field_response.html', {'form': form})
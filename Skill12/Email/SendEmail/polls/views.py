from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from . forms import EmailForm


def emailsend(request):
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            subject = 'Email Confirmation'
            message = 'Sending Email through Gjango using Gmail'
            recipient = form.cleaned_data.get('email')
            send_mail(subject,
              message, settings.EMAIL_HOST_USER, [recipient], fail_silently=False)
            messages.success(request, 'Success!')
            return redirect('emailsend')
    return render(request, 'emailform.html', {'form': form})

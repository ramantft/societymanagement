from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm
from django.core.mail import send_mail
from random import randrange
from .models import Userotp, Userprofile
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if "otp" in request.POST.keys():
            print(request.POST)
            if "resend" in request.POST.keys():
                otp = randrange(1000, 9999)
                print(otp)
                send_mail('Email OTP login resend',"Your otp is: " + str(otp),'kakaney77768@gmail.com',[request.POST['usermail']],fail_silently=False,)
                user_otp = Userotp(email=request.POST['usermail'],otp=str(otp))
                user_otp.save()
                return render(request, 'register.html', {'otp_message': 'Otp mail resended', 'email': request.POST['usermail']})
            else:
                user = Userotp.objects.filter(email=request.POST['usermail']).order_by("-id")[0]
                if user.otp == request.POST['otp']:
                    user.is_verified = True
                    user.save()
                    return redirect('login')
                else:
                    return render(request, 'register.html', {'wrong_otp': "You entered a wrong otp", 'email': request.POST['usermail']})
        else:
            print(request.POST)
            user_list = Userprofile.objects.filter(email=request.POST['email'])
            print(user_list)
            if form.is_valid() and len(user_list)==0:
                form.save()
                otp = randrange(1000, 9999)
                print(otp)
                send_mail('Email OTP login',"Your otp is: " + str(otp),'kakaney77768@gmail.com',[form.cleaned_data.get('email')],fail_silently=False,)
                user = form.cleaned_data.get('email')
                user_otp = Userotp(email=form.cleaned_data.get('email'),otp=str(otp))
                user_otp.save()
                log_user = Userprofile(email=form.cleaned_data.get('email'), username=form.cleaned_data.get('username'), flat_no=form.cleaned_data.get('flat_no'), tower_no=form.cleaned_data.get('tower_no'))
                log_user.save()
                up_email = User.objects.get(username=form.cleaned_data.get('username'))
                up_email.email = form.cleaned_data.get('email')
                up_email.save()
                messages.success(request, 'Account was successfully created for ' + user)
                return render(request, 'register.html', {'otp_message': 'You must have received a mail. Verify your Id to login', 'email': form.cleaned_data.get('email')})
            elif len(user_list)>0:
                context = {'form': form, 'email_error': 'Error Processing Your Request, Account with this email already exists.'}
                return render(request, 'register.html', context)
            else:
                messages.error(request, 'Error Processing Your Request')
                context = {'form': form}
                return render(request, 'register.html', context)
    return render(request, 'register.html', {})

def home_page(request):
    return render(request, 'home_page.html')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home_page')
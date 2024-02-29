from django.core.mail import send_mail
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "index.html")


# def contact_us(request):
#     return render(request, "contact-us.html")


def design_page(request):
    return render(request, "design-page.html")


def about(request):
    return render(request, "about.html")


def training_plans(request):
    return render(request, "training-plans.html")


def games(request):
    return render(request, "games.html")


# Forms related code

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get("number")
        goals = request.POST.get('goals')
        additional_info = request.POST.get('additional-info')

        # Construct the email message
        subject = 'New Contact Form Submission'
        message = f'''
            Name: {name}
            Email: {email}
            Number: {number}
            Goals: {goals}
            Additional Information: {additional_info}
        '''
        recipient_email = 'theathleteapproach@gmail.com'
        send_mail(subject, message, email, [recipient_email])

        # Redirect after form submission
        return render(request, 'success.html')

    return render(request, 'contact.html')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get("number")
        training_plan = request.POST.get('training-plan')
        additional_info = request.POST.get('additional-info')

        # Construct the email message
        subject = 'New Contact Form Submission'
        message = f'''
            Name: {name}
            Email: {email}
            Number: {number}
            Training_plan: {training_plan}
            Additional Information: {additional_info}
        '''
        recipient_email = 'theathleteapproach@gmail.com'
        send_mail(subject, message, email, [recipient_email])

        # Redirect after form submission
        return render(request, 'success.html')

    return render(request, 'contact-us.html')


def success(request):
    return render(request, 'success.html')

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseBadRequest
from test import Command
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload_data(request):
    if request.method == 'POST' and request.FILES:
        # Get the uploaded file from the request
        file = request.FILES.get('file')
        if file:
            data_status = Command.handle(file)
            if data_status is True:
                # Send an email
                send_mail(
                    'Data Upload Successful',
                    'Your data has been successfully uploaded to the database.',
                    'radhegaur78@gmail.com',
                    ['radheshyampbt98@gmail.com'],
                    fail_silently=False,
                )
                return HttpResponse("data uploaded")
            else:
                # Define the email subject and message
                subject = 'Data Upload Failed'
                message = 'There was an error uploading the data.'
                file_bytes = file.read()
                m = memoryview(file_bytes)
                file_name = file.name

                # Create an email message object
                email = EmailMessage(subject, message, settings.DEFAULT_FROM_EMAIL, ['radheshyampbt98@gmail.com'])

                # Attach the XLSX file to the email
                email.attach(filename=file_name, content=m, mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

                # Send the email
                email.send()
                return HttpResponse("Failded mail sent succussfully !")
        return HttpResponseBadRequest('No file uploaded.')
    

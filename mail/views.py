from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
# Title, Message, from email, to email, throw error if email fails


def index(request):

    send_mail('Hello from L.A.B.S',
              'Good Work ',
              'medbooking@btinternet.com',
              ['fagiw13004@emailhost99.com'],
              fail_silently=False)

    return render(request, 'send/index.html')
    # return render(request, '../frontend/src/components/Profile.js')

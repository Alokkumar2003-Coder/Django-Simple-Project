from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from vege.seed import *
from .utils import send_email_to_client
from django.conf import settings
from home.models import Car

def send_email(request):
    subject = "This email is from Django server"
    message = "This is a text message from Django server email"
    recipient_list = ["alokkumar2000.5.5@gmail.com"]
    file_path = f"{settings.BASE_DIR}/main.xlsx"
    send_email_with_attachment(subject, message, recipient_list, file_path)
    return redirect('/')

def home(request):
    seed_db(20)

    Car.objects.create(car_name = f"Nexon-{random.randint(0 , 100)}")

    peoples = [
        {'name': 'Alok Kumar', 'age':21 },
        {'name': 'Arun Sharma', 'age':22 },
        {'name': 'Himalaya Singh', 'age':22 },
        {'name': 'Harshit Yadav', 'age':22 },
        {'name': 'John Don', 'age':15 },
    ]

    # for people in peoples:
    #     if people['age']:
    #         print("Yes")

    vegetables = ['Pumpin', 'Tomato', 'Potatoe']

    # text = """Lorem ipsum dolor sit amet consectetur adipisicing elit. Perferendis officia reiciendis voluptatum cupiditate quaerat temporibus ullam non quam atque omnis doloremque quidem hic, ex est exercitationem velit neque, quos tempora."""

    

    # for people in peoples:
    #     print(people)
    return render(request, "Home/index.html", context={'page': 'Django','peoples': peoples,'vegetables':vegetables})
    # return HttpResponse("""<h1>Hey I am a Django Server.</h1>
    # <p>Hey this is coming from Django server</p>
    # <hr>
    # <h3 style="color:red">Hope you are loving it.</h3>
    # """)
def about(request):
    about = {'page': 'About'}
    return render(request, "Home/about.html", about)

def contact(request):
    context = {'page': 'Contact'}
    return render(request, "Home/contact.html", context)


def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a Success page.</h1>")


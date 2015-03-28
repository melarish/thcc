from django.shortcuts import render_to_response
from models import Booking

def booking_list(request):
    print("book")
#     my_booking = Booking()
#     print my_booking
    return render_to_response("example.html")
from django.shortcuts import render, get_object_or_404, redirect
from models import Booking
from forms import BookingForm
from json import dumps
from django.views.decorators.http import require_POST

def booking_calendar(request):          
    bookings = Booking.objects.all()
    bookings_as_dicts = []
    for booking in bookings:
        bookings_as_dicts.append(booking.to_json())
    bookings_json_string = dumps(bookings_as_dicts)
    #print bookings_json_string
    form = BookingForm()
    return render(request, "calendar.html", {'bookings': bookings_json_string, 'form': form})

def booking_submit(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        print "posting"
        if not request.user.is_authenticated():
            return render(request, "booking_submitted.html", {"success":False})
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            
            # Verify that this booking will not conflict with any others
            # ie in the same room, with overlapping times
            # to do this quickly, find all bookings in same room, excluding those with start date after new end date and end date before new start date. This makes sense, I prmoise... 
            conflicting_bookings = Booking.objects.filter(room=booking.room).exclude(start_date__gte=booking.end_date).exclude(end_date__lte=booking.start_date)
            print conflicting_bookings
            if len(conflicting_bookings) > 0:
                print "conflicts found"
                return render(request, "booking_submitted.html", {"success":False})    
            print "no conflicts"
            booking.save()
            print booking
            return render(request, "booking_submitted.html", {"success":True})
        return render(request, "booking_submitted.html", {"success":False})
    else:
        return redirect('bookings.views.booking_calendar')


def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, "booking_list.html", {'bookings': bookings})

def booking_detail(request, pk):
    print "view details..."
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, "booking_details.html", {'booking': booking})

def booking_add(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()
            return render(request, "booking_list.html", {'bookings': Booking.objects.all()})
            #return redirect('blog.views.post_detail', pk=post.pk)
    else:
        form = BookingForm()
    return render(request, 'booking_edit.html', {'form': form})
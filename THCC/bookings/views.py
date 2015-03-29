from django.shortcuts import render, get_object_or_404
from models import Booking
from forms import BookingForm


def booking_calendar(request):
    bookings = Booking.objects.all()
    return render(request, "calendar.html", {'bookings': bookings})


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
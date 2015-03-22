from django.shortcuts import render_to_response
def mycalendar_view(request):
    print("noobs")
    return render_to_response("mycalendar.html")
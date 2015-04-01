from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    """Booking model - when, where and who"""
    # Which user/group created this booking
    user = models.ForeignKey(User)
    # Event title, reason etc
    title = models.CharField(null=False, max_length=200)
    # Event desc
    desc = models.TextField(null=False)
    # When the booking starts - should be in half hour intervals
    start_date = models.DateTimeField(null=False, blank=False)
    # When the booking period ends
    end_date = models.DateTimeField(null=False, blank=False)
    # When the booking was created - could be useful for conflict resolution, billing etc
    created = models.DateTimeField(auto_now_add=True)
    # Which room/resource was booked
    ROOM_CHOICES = [
        ("Hall", "Hall"),
        ("Kitchen", "Kitchen"),
        ("Lounge", "Lounge"),
        ("Office One", "Office One"),
    ]
    room = models.CharField(null=False, max_length=100, choices=ROOM_CHOICES)
    # Has this booking been approved by an admin
    approved = models.BooleanField(default=False, editable=True)
    
#     class Meta:
#         abstract = True

    def __unicode__(self):
        return str(self.start_date) + " Title: " + self.title + ", User: " + str(self.user) + ", Room: " + self.room

    def short_desc(self):
        """Default short description visible on reservation button"""
        return str(self.id)

    def to_json(self):
        bookingdict = self.__dict__.copy()  # copy or we modify object's _state etc
        bookingdict['start_date'] = bookingdict['start_date'].strftime("%Y-%m-%dT%H:%M:%S")  # format required by calendar
        bookingdict['end_date'] = bookingdict['end_date'].strftime("%Y-%m-%dT%H:%M:%S")  # format required by calendar
        bookingdict['created'] = ""
        bookingdict['_state'] = ""
#         print bookingdict
        return bookingdict
        
        
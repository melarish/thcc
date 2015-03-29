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
    room_id = models.IntegerField(null=False)
    # Has this booking been approved by an admin
    approved = models.BooleanField(default=False, editable=True)
    
#     class Meta:
#         abstract = True

    def __unicode__(self):
        return str(self.start_date) + " User: " + str(self.user) + ", Room: " + str(self.room_id)

    def short_desc(self):
        """Default short description visible on reservation button"""
        return str(self.id)

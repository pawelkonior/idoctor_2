from django.db import models


class Availability(models.Model):
    class Meta:
        verbose_name = 'Availability'
        verbose_name_plural = 'Availabilities'

    class BookType(models.IntegerChoices):
        APPOINTMENT = 1
        ADMINISTRATION = 2
        OTHER = 3

    room = models.ForeignKey('Room', on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    duration = models.DurationField()
    book_type = models.IntegerField(choices=BookType.choices)

    def __str__(self):
        return f'{self.room}'


class Room(models.Model):
    floor = models.SmallIntegerField()
    room_no = models.SmallIntegerField()

    def __str__(self):
        return f'Room {self.room_no} on floor {self.floor}'

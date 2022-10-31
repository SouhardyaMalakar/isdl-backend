from .views import authuser,Decode
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Hall
from .models import Booking
from .serializers import BookingSerializer
import datetime

@api_view(['POST','GET'])
def createBooking(request):
    user=authuser(request)
    if user:
        hallid = request.query_params.get('hall_id',None)
        hall = Hall.objects.get(pk=hallid)
        Booking.objects.create(actor=user,hall=hall,booked=False,pending=True,slotStart=str(datetime.datetime.now()),slotEnd=str(datetime.datetime.now()))                    
        print(Booking.objects.all())
        return Response({'Data':'Success'})
    else:
        return Response({'Data':'Failed'})

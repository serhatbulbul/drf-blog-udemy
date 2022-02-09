from rest_framework.generics import ListAPIView
from yazi.models import Yazi


class YaziListelemeAPIView(ListAPIView):  # dataların goruntulendiği yer
    queryset = Yazi.objects.all()

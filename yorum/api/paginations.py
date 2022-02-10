from rest_framework.pagination import PageNumberPagination


class YorumSayfalama(PageNumberPagination):
    page_size = 4

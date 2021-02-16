from rest_framework.pagination import PageNumberPagination


class OneByOnePagination(PageNumberPagination):
    page_size = 1

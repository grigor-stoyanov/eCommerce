from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class GenericPaginationStyle(PageNumberPagination):
    page_size = 5
    page_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(data)
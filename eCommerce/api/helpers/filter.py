from rest_framework.filters import BaseFilterBackend
import coreapi


class QueryParamFilter(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='date_start',
            location='query',
            required=True,
            type='string',
            description='Starting date of monthly report.',
        ), coreapi.Field(
            name='date_end',
            location='query',
            required=True,
            type='string',
            description='End date of monthly report.',
        ), coreapi.Field(
            name='metric',
            location='query',
            required=True,
            type='string',
            description='Type of Report.(count or price)',
        ), ]

    def filter_queryset(self, request, queryset, view):
        try:
            n = request.query_params['name']
            queryset = queryset.filter(name=n)
        except KeyError:
            # no query parameters
            pass
        return queryset

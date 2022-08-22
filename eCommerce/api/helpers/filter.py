from rest_framework.filters import BaseFilterBackend
import coreapi


class QueryParamFilter(BaseFilterBackend):
    def get_schema_fields(self, view):
        return [coreapi.Field(
            name='date_start',
            location='query',
            required=True,
            type='Date',
            description='Starting date of monthly report.',
            example='2022-08-11',
            schema={'type': 'string', 'format': 'date'}
        ), coreapi.Field(
            name='date_end',
            location='query',
            required=True,
            type='Date',
            description='End date of monthly report.',
            example='2022-08-11',
            schema={'type': 'string', 'format': 'date'}
        ), coreapi.Field(
            name='metric',
            location='query',
            required=True,
            type='Enum[‘price’, ‘count’]',
            description='Type of Report.(count or price)',
            example='count',
            schema={'type': 'string'}
        ), ]

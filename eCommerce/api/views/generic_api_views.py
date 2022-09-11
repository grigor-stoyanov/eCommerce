from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from rest_framework import generics as generic_api_views

from eCommerce.api.helpers.filter import QueryParamFilter
from eCommerce.api.models import Order
from eCommerce.api.serializiers import ReportSerializer, ValidateQueryParamsForReport


class GenerateReportApiView(generic_api_views.ListAPIView):
    serializer_class = ReportSerializer
    filter_backends = (QueryParamFilter,)

    def get_queryset(self):

        start_date = self.request.query_params.get('date_start')
        end_date = self.request.query_params.get('date_end')
        metric = self.request.query_params.get('metric')
        qp = ValidateQueryParamsForReport(data=self.request.query_params)
        qp.is_valid(raise_exception=True)

        queryset = Order.objects.filter(date__range=(start_date, end_date))

        if metric == 'price':
            return queryset.annotate(month=TruncMonth('date')) \
                .values('month') \
                .annotate(value=Sum("products__price")) \
                .order_by("month")
        elif metric == 'count':
            return queryset.annotate(month=TruncMonth('date')) \
                .values('month') \
                .annotate(value=Count("products__pk")) \
                .order_by("month")

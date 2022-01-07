import pandas as pd
from myapp.models import Drug
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class FileProcessor:

    def __init__(self, file):
        self.file = file

    def process(self):
        pass
        data = pd.read_csv(self.file, sep='|')
        # data.fillna('', inplace=True)
        data.rename({
            'manufacturer_name': 'manufacturer',
            'Pack_size': 'pack_size',
            'product_banned_flag': 'is_banned'
        }, axis=1, inplace=True)
        data_dict = data.to_dict('records')
        for i in data_dict:
            i.update({
                'price': float(i.get('price')) if i.get('price') else 0,
                'price_per_unit': float(ppunit) if ppunit and ppunit != '-' else 0,
                'is_banned': True if i.get('is_banned') == 'True' else False
            })
            Drug.objects.create(**i)


class StandardResultsSetPagination(PageNumberPagination):

    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 10000

    def get_paginated_response(self, data):
        return Response({
            'pagination_data': {
                'previous_page': self.page.number - 1 if self.page.has_previous() else None,
                'next_page': self.page.number + 1 if self.page.has_next() else None,
                'total_records': self.page.paginator.count,
            },
            'data': data,
        })

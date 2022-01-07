
import nltk
from nltk.corpus import stopwords, wordnet
from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.exceptions import ParseError

from myapp.models import Drug

from myapp.serializers.drug import DrugSerializer
from django.db.models import Q
# from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank

from myapp.utils import FileProcessor, StandardResultsSetPagination


class DrugViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    pagination_class = StandardResultsSetPagination
    nltk.download('stopwords')

    def list(self, request):
        search = request.query_params.get('search')
        page = request.query_params.get('page', 1)
        page_size = request.query_params.get('page_size', 12)

        if not page_size:
            page_size = 12

        keywords = set()
        if search:
            tknzr = TweetTokenizer()
            tokens = tknzr.tokenize(search)
            stp_words = set(stopwords.words('english'))
            for token in tokens:
                token = token
                if token not in stp_words:
                    keywords.add(token)

        drugs = Drug.objects.all()
        if search:
            q = None
            for word in keywords:
                q_aux = Q(sku_name__icontains=word) | Q(manufacturer__icontains=word) | Q(salt_name__icontains=word)
                q = (q_aux | q) if bool(q) else q_aux
            drugs = drugs.filter(q)

        self.pagination_class.page_size = page_size

        page = self.paginate_queryset(drugs)
        if page:
            serializer = DrugSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        return self.get_paginated_response(page)


    @action(url_path='csv-upload', methods=['post'], detail=False)
    def upload_csv(self, request):

        if 'file' not in request.data:
            raise ParseError({'file': ['Empty content']})
        try:
            the_file = request.FILES['file']
        except Exception:
            raise ParseError({'file': ['File not found']})

        if the_file.content_type not in ['text/csv', 'application/vnd.ms-excel']:
            raise ParseError({'file': ['Please upload valid csv file.']})

        results = \
            FileProcessor(
                the_file=the_file
                ).process()

        if not results.get('success'):
            return Response(results.get('errors', {}), status=400)

        return Response({
            'message': 'File uploaded in progress.'
        })

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from scraping.models import AccountCategory, Account
from scraping.serializers import AccountListSerializer, AccountFollowerListSerializer

need_categories = [
    {
        "id": 1048,
        "title": "Adult content"
    },
    {
        "id": 1002,
        "title": "Art/Artists"
    },
    {
        "id": 1020,
        "title": "Beauty"
    },
    {
        "id": 1018,
        "title": "Cars & Motorbikes"
    },
    {
        "id": 1032,
        "title": "Cinema & Actors/actresses"
    },
    {
        "id": 1034,
        "title": "Computers & Gadgets"
    },
    {
        "id": 1042,
        "title": "Family"
    },
    {
        "id": 1021,
        "title": "Fashion"
    },
    {
        "id": 1023,
        "title": "Fitness & Gym"
    },
    {
        "id": 1035,
        "title": "Food & Cooking"
    },
    {
        "id": 1036,
        "title": "Humor & Fun & Happiness"
    },
    {
        "id": 1041,
        "title": "Lifestyle"
    },
    {
        "id": 1039,
        "title": "Modeling"
    },
    {
        "id": 1027,
        "title": "Music"
    },
    {
        "id": 1038,
        "title": "Photography"
    },
    {
        "id": 1017,
        "title": "Shows"
    },
    {
        "id": 1013,
        "title": "Sports with a ball"
    }
]


class AccountCategoryViewSet(APIView):
    queryset = AccountCategory.objects.all()

    def get(self, request):
        read_serializer = AccountListSerializer(self.get_queryset(), many=True)

        return Response(
            {
                "accounts": read_serializer.data
            },
            status=status.HTTP_200_OK
        )

    def get_queryset(self):
        country = self.request.data['country']
        category = self.request.data['category']
        page = int(self.request.query_params['page'])
        items_count = self.request.data['items_count']

        offset = (page-1) * items_count

        return self.queryset.filter(category=category, account__country=country).order_by('-account__followers')[offset:offset+items_count]


class AccountFollowerViewSet(APIView):
    queryset = Account.objects.all()

    def post(self, request):
        read_serializer = AccountFollowerListSerializer(self.get_queryset(), many=True)

        return Response(
            {
                "accounts": read_serializer.data
            },
            status=status.HTTP_200_OK
        )

    def get_queryset(self):
        country = self.request.data['country']
        min_followers = self.request.data['min_followers']
        page = int(self.request.query_params['page'])
        items_count = self.request.data['items_count']

        offset = (page-1) * items_count

        return self.queryset.filter(followers__gt=min_followers, country=country).order_by('-followers')[offset:offset+items_count]

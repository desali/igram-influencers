from rest_framework import serializers

from scraping.models import AccountCategory, Category, Account


class CategoryRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["title", "hype_id"]


class CategoryFollowerRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["title"]


class AccountRetrieveSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['username', 'name', 'followers', ]


class AccountListSerializer(serializers.ModelSerializer):
    category = CategoryRetrieveSerializer()
    account = AccountRetrieveSerializer()

    class Meta:
        model = AccountCategory
        fields = ['category', 'account']


class AccountFollowerListSerializer(serializers.ModelSerializer):
    categories = serializers.SlugRelatedField(many=True, read_only=True, slug_field="title")

    class Meta:
        model = Account
        fields = ['username', 'name', 'followers', 'categories']

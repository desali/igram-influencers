from django.urls import path

from scraping.views import AccountCategoryViewSet, AccountFollowerViewSet

app_name = 'scraping'

urlpatterns = [
    path('accounts', AccountCategoryViewSet.as_view(), name="account_category"),
    path('accounts_follower', AccountFollowerViewSet.as_view(), name="account_follower")
]

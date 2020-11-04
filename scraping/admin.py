from django.contrib import admin

from scraping.models import Country, City, Category, GenderType, AgeInterval, Language, Interval, Account, \
    AccountCategory, AccountLanguage, AudienceGender, AudienceAge, AudienceCountry, AudienceCity

scraping_models = [Country, City, Category, GenderType, AgeInterval, Language, Interval, Account,
                   AccountCategory, AccountLanguage, AudienceGender, AudienceAge, AudienceCountry, AudienceCity]


admin.site.register(scraping_models)

from django.db import models


class Interval(models.Model):
    title = models.CharField(max_length=255)
    hype_id = models.CharField(max_length=255)


class GenderType(models.Model):
    title = models.CharField(max_length=255)
    hype_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'gender_types'


class AgeInterval(models.Model):
    title = models.CharField(max_length=255)
    hype_id = models.CharField(max_length=255)

    class Meta:
        db_table = 'age_intervals'


class Language(models.Model):
    title = models.CharField(max_length=255)
    hype_id = models.CharField(max_length=255)


class Country(models.Model):
    title = models.CharField(max_length=255)
    hype_id = models.CharField(max_length=255)


class City(models.Model):
    title = models.CharField(max_length=255)
    hype_id = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=255)
    hype_id = models.CharField(max_length=255)


class Account(models.Model):
    ACCOUNT_TYPE_SELECT = (
        (0, 'Не выбрано'),
        (1, 'Персональный'),
        (2, 'Бренд')
    )

    CONTACT_INFO_SELECT = (
        (0, 'Не выбрано'),
        (1, 'Есть почта или номер')
    )

    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    is_verified = models.BooleanField(default=False)
    followers = models.IntegerField()
    quality_followers = models.IntegerField()
    engagement_rate = models.FloatField()
    account_quality_score = models.FloatField()

    account_type = models.IntegerField(choices=ACCOUNT_TYPE_SELECT, default=0)
    contact_info = models.IntegerField(choices=CONTACT_INFO_SELECT, default=0)

    gender = models.ForeignKey(GenderType, blank=True, null=True, on_delete=models.DO_NOTHING, default=None)
    age = models.ForeignKey(AgeInterval, blank=True, null=True, on_delete=models.DO_NOTHING, default=None)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.DO_NOTHING, default=None)

    categories = models.ManyToManyField(Category, through='AccountCategory')
    languages = models.ManyToManyField(Language, through='AccountLanguage')


class AccountCategory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'account_categories'


class AccountLanguage(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'account_languages'


class AudienceGender(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    gender_type = models.ForeignKey(GenderType, on_delete=models.DO_NOTHING)
    interval = models.ForeignKey(Interval, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'audience_gender'


class AudienceAge(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    age_interval = models.ForeignKey(AgeInterval, on_delete=models.DO_NOTHING)
    interval = models.ForeignKey(Interval, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'audience_age'


class AudienceCountry(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    interval = models.ForeignKey(Interval, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'audience_country'


class AudienceCity(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    interval = models.ForeignKey(Interval, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'audience_city'

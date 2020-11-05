from django.db import models


class Country(models.Model):
    title = models.CharField(max_length=255)
    hype_id = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length=255)
    hype_id = models.CharField(max_length=255, unique=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255, unique=True)
    hype_id = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


class GenderType(models.Model):
    title = models.CharField(max_length=255)
    hype_id = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'gender_types'
        verbose_name = "Gender type"
        verbose_name_plural = "Gender types"

    def __str__(self):
        return self.title


class AgeInterval(models.Model):
    title = models.CharField(max_length=255)
    hype_start_id = models.IntegerField(null=True)
    hype_end_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'age_intervals'
        verbose_name = "Age interval"
        verbose_name_plural = "Age intervals"

    def __str__(self):
        return self.title


class Language(models.Model):
    title = models.CharField(max_length=255)
    hype_id = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Language"
        verbose_name_plural = "Languages"

    def __str__(self):
        return self.title


class Interval(models.Model):
    title = models.CharField(max_length=255)
    hype_id = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Interval"
        verbose_name_plural = "Intervals"

    def __str__(self):
        return self.title


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
    username = models.CharField(max_length=255, unique=True)
    is_verified = models.BooleanField(default=False)
    followers = models.IntegerField()
    quality_followers = models.IntegerField(null=True, blank=True)
    engagement_rate = models.FloatField()
    account_quality_score = models.CharField(max_length=255)

    account_type = models.IntegerField(choices=ACCOUNT_TYPE_SELECT, default=0)
    contact_info = models.IntegerField(choices=CONTACT_INFO_SELECT, default=0)

    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    gender = models.ForeignKey(GenderType, blank=True, null=True, on_delete=models.DO_NOTHING, default=None)
    age = models.ForeignKey(AgeInterval, blank=True, null=True, on_delete=models.DO_NOTHING, default=None)
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.DO_NOTHING, default=None)

    languages = models.ManyToManyField(Language, through='AccountLanguage')
    categories = models.ManyToManyField(Category, through='AccountCategory')

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.username


class AccountCategory(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, to_field="hype_id", on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'account_categories'
        verbose_name = "Account category"
        verbose_name_plural = "Account categories"

    def __str__(self):
        return f"{str(self.account)}-{str(self.category)}"


class AccountLanguage(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'account_languages'
        verbose_name = "Account language"
        verbose_name_plural = "Account languages"

    def __str__(self):
        return f"{str(self.account)}-{str(self.language)}"


class AudienceGender(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    gender_type = models.ForeignKey(GenderType, on_delete=models.DO_NOTHING)
    interval = models.ForeignKey(Interval, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'audience_gender'
        verbose_name = "Audience gender"
        verbose_name_plural = "Audience genders"

    def __str__(self):
        return f"{str(self.account)}-{str(self.gender_type)}-{str(self.interval)}"


class AudienceAge(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    age_interval = models.ForeignKey(AgeInterval, on_delete=models.DO_NOTHING)
    interval = models.ForeignKey(Interval, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'audience_age'
        verbose_name = "Audience age"
        verbose_name_plural = "Audience ages"

    def __str__(self):
        return f"{str(self.account)}-{str(self.age_interval)}-{str(self.interval)}"


class AudienceCountry(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    interval = models.ForeignKey(Interval, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'audience_country'
        verbose_name = "Audience country"
        verbose_name_plural = "Audience countries"

    def __str__(self):
        return f"{str(self.account)}-{str(self.country)}-{str(self.interval)}"


class AudienceCity(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    interval = models.ForeignKey(Interval, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'audience_city'
        verbose_name = "Audience city"
        verbose_name_plural = "Audience cities"

    def __str__(self):
        return f"{str(self.account)}-{str(self.city)}-{str(self.interval)}"

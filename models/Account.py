class Account(object):
    """Account class for instagram account"""

    name = ""
    username = ""
    is_verified = False
    followers = 0
    quality_followers = 0
    engagement_rate = 0
    account_quality_score = 0
    categories = []
    gender = ""
    age = ""

    def __init__(self):
        super(Account, self).__init__()

    def __str__(self):
        d = {
            'name': self.name,
            'username': self.username,
            'is_verified': self.is_verified,
            'followers': self.followers,
            'quality_followers': self.quality_followers,
            'engagement_rate': self.engagement_rate,
            'account_quality_score': self.account_quality_score,
            'categories': self.categories
        }

        return '''\
		Account name: {name}.
		Account username: {username}.
		Account is_verified: {is_verified}.
		Account followers: {followers}.
		Account quality_followers: {quality_followers}.
		Account engagement_rate: {engagement_rate}.
		Account account_quality_score: {account_quality_score}.
		Account categories: {categories}.\
		'''.format(**d)

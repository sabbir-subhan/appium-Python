# credentials - to change username, password or domain, change values in quotations ""


from generators import RandomGenerator


class Credentials(object):
    """A class containing credentials for accounts on OCA webpage"""

    # domain
    QA_domain = "https://bitnoiseqa.nogginoca.com"
    production_domain = 'https://nogginoca.com'

    # QA
    QA_username = "bitnoise"
    QA_password = "Bitn0!$e"

    # general_user
    general_username = "test_general"
    general_password = "test_general"

    # admin
    admin_username = "test_admin"
    admin_password = "test_admin"

    # expired_1_day_ago
    expired_username = "test_expired_1_day_ago"
    expired_password = "test_expired_1_day_ago"

    # expire_today
    expire_today_username = "test_expire_today"
    expire_today_password = "test_expire_today"

    # expire_in_1_day
    expire_in_1_day_username = "test_expire_in_1_day"
    expire_in_1_day_password = "test_expire_in_1_day"

    # suspended
    suspended_username = "test_suspended"
    suspended_password = "test_suspended"

    @staticmethod
    def get_username(username):

        if username == 'QA':
            return Credentials.QA_username
        elif username == 'general_user':
            return Credentials.general_username
        elif username == 'admin':
            return Credentials.admin_username
        elif username == 'expired_1_day_ago':
            return Credentials.expired_username
        elif username == 'expire_today':
            return  Credentials.expire_today_username
        elif username == 'expire_in_1_day':
            return Credentials.expire_in_1_day_username
        elif username == 'suspended':
            return Credentials.suspended_username
        else:
            pass

    @staticmethod
    def get_password(password):

        if password == 'QA':
            return Credentials.QA_password
        elif password == 'random':
            return RandomGenerator.pass_generator()
        elif password == 'general_user':
            return Credentials.general_password
        elif password == 'admin':
            return Credentials.admin_password
        elif password == 'expired_1_day_ago':
            return Credentials.expired_password
        elif password == 'expire_today':
            return  Credentials.expire_today_password
        elif password == 'expire_in_1_day':
            return Credentials.expire_in_1_day_password
        elif password == 'suspended':
            return Credentials.suspended_password
        else:
            pass

    @staticmethod
    def get_domain(domain):

        if domain == 'QA':
            return Credentials.QA_domain
        elif domain == 'production':
            return Credentials.production_domain
        else:
            pass




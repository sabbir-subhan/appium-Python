""" Credentials - to change username, password or domain, change values in quotations """

from Modules.generators import RandomGenerator

'''
You can use: 

QA
general_user
admin
expired_1_day_ago
expire_today
expire_in_1_day
suspended

'''


class ContactIdentifierPIN:
    """A class containing Contact Identifier PIN from invitation email"""

    pin = "abgersb"  # here You can change Contact Identifier PIN

    @staticmethod
    def get_contact_identifier_pin(test_pin):

        if test_pin == 'test_pin':
            return ContactIdentifierPIN.pin


class Credentials:
    """A class containing credentials for accounts on OCA web page"""

    # domain
    QA_domain = "https://bitnoiseqa.nogginoca.com"  # here You can change domain for tests
    production_domain = 'https://nogginoca.com'  # here You can change domain for production

    # QA
    QA_username = "bitnoise"  # here You can change username for QA
    QA_password = "bitnoise1"  # here You can change password for QA

    # general_user
    general_username = "test_general"  # here You can change username for general user
    general_password = "test_general"  # here You can change password for general user

    # admin
    admin_username = "test_admin"  # here You can change username for admin
    admin_password = "test_admin"  # here You can change password for admin

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
            return Credentials.expire_today_username
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
            return Credentials.expire_today_password
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





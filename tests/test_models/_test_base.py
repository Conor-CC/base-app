from user import serializers as s


class TestBase():
    TEST_PASS = '0000'
    USER_A = {
        'username': 'a',
        'email': 'a@email.com',
        'password': TEST_PASS,
        'first_name': 'first_name a',
        'last_name': 'last_name a',
        'organization': 'a Ltd.'
    }
    USER_B = {
        'username': 'b',
        'email': 'b@email.com',
        'password': TEST_PASS,
        'first_name': 'first_name a',
        'last_name': 'last_name a',
        'organization': 'a Ltd.'
    }
    USER_C = {
        'username': 'c',
        'email': 'c@email.com',
        'password': TEST_PASS,
        'first_name': 'first_name c',
        'last_name': 'last_name c',
        'organization': 'c Ltd.'
    }

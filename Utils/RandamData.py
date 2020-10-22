import random

class Utils():
    @classmethod
    def _get_random_alphanumeric_string(cls):
        return ''.join(random.choice('ABCDSFGEHIJK123456') for i in range(5))

    @classmethod
    def _get_random_numeric_string(cls):
        return ''.join(random.choice('1234567890') for i in range(10))

    @classmethod
    def _get_random_five_number_string(cls):
        return ''.join(random.choice('123456789') for i in range(5))

    @classmethod
    def _get_random_alphabetic_string(cls):
        return ''.join(random.choice('ABCDSFGEHIJK') for i in range(5))


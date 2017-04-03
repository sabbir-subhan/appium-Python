import random
import string


class RandomGenerator:
    """A class for random generator"""
    def id_generator(size=7, chars=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

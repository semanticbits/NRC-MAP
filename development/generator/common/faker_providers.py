from faker import Faker
import random

from faker.providers import BaseProvider

class ITAAC(BaseProvider):
    """
    Class for generating synthetic data related to ITAACs
    """
    target_flag_value = None

    def itaac_status(self):
        status_options = [
            'UIN Accepted',
            'ICN Verified',
            'Not Received'
        ]
        return random.choice(status_options)

    def icn_status(self):
        status_options = [
            'Pending',
            'Approved',
            'Failed'
        ]
        return random.choice(status_options)

    def effort_required(self):
        return random.choice(list(range(1, 80)))

    def facility(self):
        facilities = [
            'Vogtle 3',
            'Vogtle 4'
        ]
        return random.choice(facilities)

    def true_false_flag(self):
        self.target_flag_value = random.choice([True, False])
        return self.target_flag_value

    def target_amt(self):
        return_value = None

        if self.target_flag_value == True:
            return_value = random.choice(list(range(1,60)))

        return return_value


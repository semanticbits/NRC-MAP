"""Faker Provider

This Provider will be used for custom faker provider classes for
synthetic data.

"""
import random

from faker.providers import BaseProvider


class ITAAC(BaseProvider):
    """
    Class for generating synthetic data related to ITAACs
    """
    target_flag_value = None

    @staticmethod
    def itaac_status():
        """
        Generate a random selection of ITAAC status'
        """
        status_options = [
            'UIN Accepted',
            'ICN Verified',
            'Not Received'
        ]
        return random.choice(status_options)

    @staticmethod
    def icn_status():
        """
        Generate a random selection of ICN status'
        """
        status_options = [
            'Pending',
            'Approved',
            'Failed'
        ]
        return random.choice(status_options)

    @staticmethod
    def facility():
        """
        Generate a random selection of Vogtle facilities
        """
        facilities = [
            'Vogtle 3',
            'Vogtle 4'
        ]
        return random.choice(facilities)

    def true_false_flag(self):
        """
        Generate a random true/false value
        """
        self.target_flag_value = random.choice([True, False])
        return self.target_flag_value

    def target_amt(self):
        """
        Generate a random target amount
        """
        return_value = None

        if self.target_flag_value is True:
            return_value = random.choice(list(range(1, 60)))

        return return_value

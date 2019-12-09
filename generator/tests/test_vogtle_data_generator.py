"""PyTest Vogtle Data Generator File

Tests all Vogtle related synthetic data generator

"""
from vogtle_data_generator import VogtleDataGenerator
from common import validations
from . import test_values as tv


class TestVogtleDataGenerator(object):
    """ Class for all Vogtle Data Generator testing
    """
    VogtleDataGenerator = VogtleDataGenerator(directory='test_data/')

    def test_generate_inspections(self):
        """ Test inspection data generation
        """
        config = tv.VOGTLE_CONFIG['inspections']
        self.VogtleDataGenerator.generate_inspections(config['row_count'])

        assert validations.validate_csv(filename=config['filename'],
                                        header=config['header'],
                                        cols=config['col_count'],
                                        rows=config['row_count'])

    def test_generate_news_feed(self):
        """ Test news feed data generation
        """
        config = tv.VOGTLE_CONFIG['news_feed']
        self.VogtleDataGenerator.generate_news_feed(config['row_count'])

        assert validations.validate_csv(filename=config['filename'],
                                        header=config['header'],
                                        cols=config['col_count'],
                                        rows=config['row_count'])

    def test_generate_public_meetings(self):
        """ Test public meetings data generation
        """
        config = tv.VOGTLE_CONFIG['public_meetings']
        self.VogtleDataGenerator.generate_public_meetings(config['row_count'])

        assert validations.validate_csv(filename=config['filename'],
                                        header=config['header'],
                                        cols=config['col_count'],
                                        rows=config['row_count'])

    def test_generate_license_actions(self):
        """ Test inspection data generation
        """
        config = tv.VOGTLE_CONFIG['license_actions']
        self.VogtleDataGenerator.generate_license_actions(config['row_count'])

        assert validations.validate_csv(filename=config['filename'],
                                        header=config['header'],
                                        cols=config['col_count'],
                                        rows=config['row_count'])

    def test_generate_crop_findings(self):
        """ Test crop findings data generation
        """
        config = tv.VOGTLE_CONFIG['crop_findings']
        self.VogtleDataGenerator.generate_crop_findings(config['row_count'])

        assert validations.validate_csv(filename=config['filename'],
                                        header=config['header'],
                                        cols=config['col_count'],
                                        rows=config['row_count'])

    def test_generate_calendar(self):
        """ Test calendar data generation
        """
        config = tv.VOGTLE_CONFIG['calendar']
        self.VogtleDataGenerator.generate_calendar(config['start_year'],
                                                   config['end_year'])

        assert validations.validate_csv(filename=config['filename'],
                                        header=config['header'],
                                        cols=config['col_count'],
                                        rows=config['row_count'])

"""PyTest Vogtle Data Generator File

Tests all Vogtle related synthetic data generator

"""
import sys
import unittest
try:
    from unittest import mock
except ImportError:
    import mock
from vogtle_data_generator import VogtleDataGenerator
import vogtle_data_generator as vdg
from common import validations
from . import test_values as tv


class TestVogtleDataGenerator(unittest.TestCase):
    """ Class for all Vogtle Data Generator testing
    """
    VogtleDataGenerator = VogtleDataGenerator(directory='test_data/')

    def test_generate_inspections(self):
        """ Test inspection data generation
        """
        config = tv.VOGTLE_CONFIG['inspections']
        self.VogtleDataGenerator.generate_inspections(config['row_count'])

        validations.validate_csv(filename=config['filename'],
                                 header=config['header'],
                                 cols=config['col_count'],
                                 rows=config['row_count'])

    def test_generate_news_feed(self):
        """ Test news feed data generation
        """
        config = tv.VOGTLE_CONFIG['news_feed']
        self.VogtleDataGenerator.generate_news_feed(config['row_count'])

        validations.validate_csv(filename=config['filename'],
                                 header=config['header'],
                                 cols=config['col_count'],
                                 rows=config['row_count'])

    def test_generate_public_meetings(self):
        """ Test public meetings data generation
        """
        config = tv.VOGTLE_CONFIG['public_meetings']
        self.VogtleDataGenerator.generate_public_meetings(config['row_count'])

        validations.validate_csv(filename=config['filename'],
                                 header=config['header'],
                                 cols=config['col_count'],
                                 rows=config['row_count'])

    def test_generate_license_actions(self):
        """ Test inspection data generation
        """
        config = tv.VOGTLE_CONFIG['license_actions']
        self.VogtleDataGenerator.generate_license_actions(config['row_count'])

        validations.validate_csv(filename=config['filename'],
                                 header=config['header'],
                                 cols=config['col_count'],
                                 rows=config['row_count'])

    def test_generate_crop_findings(self):
        """ Test crop findings data generation
        """
        config = tv.VOGTLE_CONFIG['crop_findings']
        self.VogtleDataGenerator.generate_crop_findings(config['row_count'])

        validations.validate_csv(filename=config['filename'],
                                 header=config['header'],
                                 cols=config['col_count'],
                                 rows=config['row_count'])

    def test_generate_calendar(self):
        """ Test calendar data generation
        """
        config = tv.VOGTLE_CONFIG['calendar']
        self.VogtleDataGenerator.generate_calendar(config['start_year'],
                                                   config['end_year'])

        validations.validate_csv(filename=config['filename'],
                                 header=config['header'],
                                 cols=config['col_count'],
                                 rows=config['row_count'])

    def test_generate_default_no_dir(self):
        """ Test default dataset generation, with no directory parameter
        """
        with self.assertRaises(SystemExit):
            VogtleDataGenerator()

    def test_generate_default_bad_args(self):
        """ Test default dataset generation, with incorrect args
        """
        with self.assertRaises(SystemExit):
            vdg.generate_default(args=['-r', 'abc/'], config=None)

    @staticmethod
    def test_generate_default_w_args():
        """ Test default dataset generation, with args
        """
        config = {
            'inspections':
                tv.VOGTLE_CONFIG['inspections']['row_count'],
            'news_feed':
                tv.VOGTLE_CONFIG['news_feed']['row_count'],
            'public_meetings':
                tv.VOGTLE_CONFIG['public_meetings']['row_count'],
            'start_year':
                tv.VOGTLE_CONFIG['calendar']['start_year'],
            'end_year':
                tv.VOGTLE_CONFIG['calendar']['end_year'],
            'license_actions':
                tv.VOGTLE_CONFIG['license_actions']['row_count'],
            'crop_findings':
                tv.VOGTLE_CONFIG['crop_findings']['row_count'],
        }

        data_types = [
            'inspections',
            'news_feed',
            'public_meetings',
            'calendar',
            'license_actions',
            'crop_findings'
        ]
        vdg.generate_default(args=['-d', 'test_data/'], config=config)

        for key in data_types:
            cfg = tv.VOGTLE_CONFIG[key]
            validations.validate_csv(filename=cfg['filename'],
                                     header=cfg['header'],
                                     cols=cfg['col_count'],
                                     rows=cfg['row_count'])

    @staticmethod
    def test_generate_default():
        """ Test default dataset generation
        """
        test_config = {
            'inspections': 800,
            'news_feed': 100,
            'public_meetings': 100,
            'calendar': (365*5)+1,
            'license_actions': 100,
            'crop_findings': 100
        }

        testargs = ["vogtle_data_generator.py", "-d", "test_data/"]
        with mock.patch.object(sys, 'argv', testargs):
            vdg.generate_default()

            for key in test_config:
                cfg = tv.VOGTLE_CONFIG[key]
                validations.validate_csv(filename=cfg['filename'],
                                         header=cfg['header'],
                                         cols=cfg['col_count'],
                                         rows=test_config[key])

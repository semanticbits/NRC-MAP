"""PyTest Vogtle Data Generator File

Tests all Vogtle related synthetic data generator

"""
from vogtle_data_generator import VogtleDataGenerator
import vogtle_data_generator as vdg
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

    @staticmethod
    def test_generate_default():
        """ Test calendar data generation
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
        vdg.generate_default(args=['-d', 'data/'], config=config)

        for key in data_types:
            cfg = tv.VOGTLE_CONFIG[key]
            assert validations.validate_csv(filename=cfg['filename'],
                                            header=cfg['header'],
                                            cols=cfg['col_count'],
                                            rows=cfg['row_count'])

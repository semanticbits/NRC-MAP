"""Vogtle Data Generator

This script currently generates data for the following dashboard sections:
- Inspections
- News Feed
- Public Meetings
- General Calendar
- License Actions
- cROP Actions

"""
import logging
import os
import random
import sys
from argparse import ArgumentParser, ArgumentError
from datetime import date, datetime, timedelta
from faker import Faker
from common.faker_providers import ITAAC


__version__ = "0.1.0"

logging.basicConfig(
    level=logging.INFO,
    format='%(filename)s: %(asctime)s: %(levelname)s: %(message)s'
)

ARG_PARSER = ArgumentParser()
ARG_PARSER.add_argument('-d',
                        dest='directory',
                        type=str,
                        help='Set directory for synthetic data files.'
                        ' e.g. `./data/`')
ARG_PARSER.add_argument('--version',
                        action='version',
                        version="%(prog)s v" + __version__)


class VogtleDataGenerator(object):
    """
    This class holds all generator functions
    for Vogtle Dashboard Synthetic data
    """
    fake = None
    directory = None

    def __init__(self, directory=None):
        if not directory:
            logging.error("No directory provided, exiting..")
            sys.exit(1)

        os.makedirs(directory, exist_ok=True)

        self.fake = Faker()
        self.fake.add_provider(ITAAC)

        if directory:
            self.directory = directory

    @staticmethod
    def generate_itaac_effort_str(itaac_id, effort_id,
                                  effort_type, effort_range):
        """Generate string, bar separated value of itaac_effort entry

        :param itaac_id: ID of ITAAC for row of effort
        :param effort_id: The unique effort_id
        :param effort_type: The type of effort
        :param effort_range: Range of values to be used for actual and estimate
                             hour values
        """
        effort_range = list(effort_range)
        actual = random.choice(effort_range)
        estimate = random.choice(effort_range)

        return (
            f'\n{effort_id}|'
            f'{itaac_id}|'
            f'{effort_type}|'
            f'{actual}|'
            f'{estimated}'
        )

    def generate_itaac_efforts(self, itaac_ids):
        """Generate ITAAC Efforts

        :param itaac_ids: IDs of ITAACS to generate efforts
        """
        header = (
            'id|'
            'itaac_id|'
            'effort_type|'
            'actual|'
            'estimate'
        )
        effort_types = [
            "ITAAC",
            "Program",
            "Reactive/Allegations",
            "Technical",
            "Total",
        ]
        output = [header]

        with open(f'{self.directory}itaac_efforts.csv', 'w+') as output_file:

            for idx, itaac_id in enumerate(itaac_ids, 1):
                actual = 0
                estimated = 0

                for effort_type in effort_types:
                    if effort_type == 'Total':
                        output.append(f'\n{idx}|'
                                      f'{itaac_id}|'
                                      f'{effort_type}|'
                                      f'{actual}|'
                                      f'{estimated}')
                    else:
                        actual += random.randint(0, 120)
                        estimated += random.randint(0, 120)

            output_file.write(''.join(output))

    def generate_inspections(self, rows, generate_efforts_flag=False):
        """
        Generate synthetic data for Inspections

        :param rows: Number of rows to generate
        :param generate_efforts_flag: Boolean flag to generate effort hours
        """
        header = (
            'id|'
            'itaac_status|'
            'icn_status|'
            'est_completion_date|'
            'date_received|'
            'facility|'
            'targeted_flag'
        )
        itaac_ids = []
        output = [header]

        with open('{}inspections.csv'
                  .format(self.directory), 'w+') as output_file:

            for itaac_id in range(1, rows+1):
                if generate_efforts_flag:
                    itaac_ids.append(itaac_id)

                itaac_status = self.fake.format('itaac_status')
                icn_status = self.fake.format('icn_status')
                est_completion_date = random.choice(
                    [self.fake.format('future_date'),
                     None])
                date_received = self.fake.format(
                    'date_between_dates',
                    date_start=datetime.now() - timedelta(days=720),
                    date_end=datetime.now())
                facility = self.fake.format('facility')
                targeted_flag = self.fake.format('true_false_flag')

                output.append(f'\n{itaac_id}|'
                              f'{itaac_status}|'
                              f'{icn_status}|'
                              f'{est_completion_date}|'
                              f'{date_received}|'
                              f'{facility}|'
                              f'{targeted_flag}')

            output_file.write(''.join(output))

        if generate_efforts_flag:
            self.generate_itaac_efforts(itaac_ids)

    def generate_news_feed(self, rows):
        """
        Generate synthetic data for News Feed

        :param rows: Number of rows to generate
        """
        header = (
            'id|'
            'title|'
            'text|'
            'datetime|'
            'source_url'
        )
        output = [header]
        with open('{}news_feed.csv'.format(self.directory), 'w+') \
                as output_file:

            for feed_id in range(1, rows+1):

                title = self.fake.format('sentence',
                                         nb_words=5,
                                         variable_nb_words=False,
                                         ext_word_list=None)
                text = self.fake.format('sentence',
                                        nb_words=100,
                                        variable_nb_words=False,
                                        ext_word_list=None)
                news_datetime = self.fake.format('future_datetime',
                                                 tzinfo=None)
                source_url = "http://www.{}.com/{}".format(
                    self.fake.format('word'), self.fake.format('word'))

                output.append(f'\n{feed_id}|'
                              f'{title}|'
                              f'{text}|'
                              f'{news_datetime}|'
                              f'{source_url}')

            output_file.write(''.join(output))

    def generate_public_meetings(self, rows):
        """
        Generate synthetic data for Public Meetings

        :param rows: Number of rows to generate
        """
        header = (
            'id|'
            'purpose|'
            'date|'
            'time|l'
            'ocation|'
            'contact'
        )
        output = [header]

        with open('{}public_meetings.csv'.format(self.directory), 'w+') \
                as output_file:

            for meeting_id in range(1, rows+1):
                purpose = self.fake.format('sentence',
                                           nb_words=10,
                                           variable_nb_words=True,
                                           ext_word_list=None)
                meeting_date = str(self.fake.format('date_time_this_year',
                                                    before_now=True,
                                                    after_now=True,
                                                    tzinfo=None))[:10]
                time = self.fake.format('time', pattern='%H:%M')
                location = self.fake.format('address').replace("\n", " ")
                contact = "{} : {}".format(
                    self.fake.format('name'),
                    self.fake.format('phone_number'))

                output.append(f'\n{meeting_id}|'
                              f'{purpose}|'
                              f'{meeting_date}|'
                              f'{time}|'
                              f'{location}|'
                              f'{contact}')

            output_file.write(''.join(output))

    def generate_license_actions(self, rows):
        """
        Generate synthetic data for License Actions

        :param rows: Number of rows to generate
        """
        header = (
            'id|'
            'text|'
            'status|'
            'date'
        )
        output = [header]

        with open('{}license_actions.csv'.format(self.directory), 'w+') \
                as output_file:

            for license_action_id in range(1, rows+1):
                text = self.fake.format('sentence',
                                        nb_words=10,
                                        variable_nb_words=True,
                                        ext_word_list=None)
                license_action_date = self.fake.format('future_datetime',
                                                       tzinfo=None)
                status = random.choice(["Open", "Closed"])

                output.append(f'\n{license_action_id}|'
                              f'{text}|'
                              f'{status}|'
                              f'{license_action_date}')

            output_file.write(''.join(output))

    def generate_crop_findings(self, rows):
        """
        Generate synthetic data for License Actions

        :param rows: Number of rows to generate
        """
        header = (
            'id|'
            'description|'
            'status|'
            'date'
        )
        output = [header]

        with open('{}crop_findings.csv'.format(self.directory), 'w+') \
                as output_file:

            for crop_finding_id in range(1, rows+1):
                description = self.fake.format('sentence',
                                               nb_words=10,
                                               variable_nb_words=True,
                                               ext_word_list=None)
                crop_finding_datetime = self.fake.format('future_datetime',
                                                         tzinfo=None)
                status = random.choice(["Open", "Closed"])

                output.append(f'\n{crop_finding_id}|'
                              f'{description}|'
                              f'{status}|'
                              f'{crop_finding_datetime}')

            output_file.write(''.join(output))

    def generate_calendar(self, start_year, end_year):
        """
        Generate Calendar

        :param rows: Number of rows to generate
        """
        header = (
            'id|'
            'date'
        )
        output = [header]

        sdate = date(start_year, 1, 1)   # start date
        edate = date(end_year, 12, 31)   # end date

        delta = edate - sdate       # as timedelta

        with open('{}calendar.csv'.format(self.directory), 'w+') \
                as output_file:

            for i in range(1, delta.days + 2):
                day = sdate + timedelta(days=i)
                output.append(f'\n{i}|'
                              f'{day}')

            output_file.write(''.join(output))


def generate_default(args=None, config=None):
    """Generate the default set of synthetic data

    :param args: Command line args
    :param config: configuration fo generator
    """
    logging.info("Generating synthetic data...")
    options = {}
    try:
        if args:
            options = ARG_PARSER.parse_args(args)
        else:
            options = ARG_PARSER.parse_args()
    except ArgumentError:
        ARG_PARSER.exit()

    os.makedirs(options.directory, exist_ok=True)

    vogtle_generator = VogtleDataGenerator(directory=options.directory)

    if not config:
        config = {
            'inspections': 800,
            'news_feed': 100,
            'public_meetings': 100,
            'start_year': 2017,
            'end_year': 2021,
            'license_actions': 100,
            'crop_findings': 100
        }

    vogtle_generator.generate_inspections(config['inspections'], True)
    vogtle_generator.generate_news_feed(config['news_feed'])
    vogtle_generator.generate_public_meetings(config['public_meetings'])
    vogtle_generator.generate_calendar(config['start_year'],
                                       config['end_year'])
    vogtle_generator.generate_license_actions(config['license_actions'])
    vogtle_generator.generate_crop_findings(config['crop_findings'])

    logging.info("Synthetic data generation complete")


if __name__ == '__main__':
    generate_default()

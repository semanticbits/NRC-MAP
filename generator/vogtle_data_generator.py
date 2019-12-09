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
from os import path
import random
import sys
from argparse import ArgumentParser, ArgumentError
from datetime import date, timedelta
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

        self.fake = Faker()
        self.fake.add_provider(ITAAC)

        if directory:
            self.directory = directory

    def generate_inspections(self, rows):
        """
        Generate synthetic data for Inspections
        """
        header = "id|itaac_status|icn_status|est_completion_date|" \
                 "effort_required|facility|targeted_flag|target_amt\n"

        with open('{}inspections.csv'
                  .format(self.directory), 'w') as output_file:

            output_file.write(header)
            for itaac_id in range(rows):
                itaac_status = self.fake.format('itaac_status')
                icn_status = self.fake.format('icn_status')
                est_completion_date = self.fake.format('future_datetime',
                                                       tzinfo=None)

                effort_required = self.fake.format('effort_required')
                facility = self.fake.format('facility')
                targeted_flag = self.fake.format('true_false_flag')
                target_amt = self.fake.format('target_amt')

                output_file.write("%s|%s|%s|%s|%s|%s|%s|%s\n" %
                                  (itaac_id,
                                   itaac_status,
                                   icn_status,
                                   est_completion_date,
                                   effort_required,
                                   facility,
                                   targeted_flag,
                                   target_amt))

    def generate_news_feed(self, rows):
        """
        Generate synthetic data for News Feed
        """
        header = "id|title|text|datetime|source_url\n"

        with open('{}news_feed.csv'.format(self.directory), 'w') \
                as output_file:

            output_file.write(header)
            for feed_id in range(rows):

                title = self.fake.format('sentence',
                                         nb_words=5,
                                         variable_nb_words=False,
                                         ext_word_list=None)
                text = self.fake.format('sentence',
                                        nb_words=100,
                                        variable_nb_words=False,
                                        ext_word_list=None)
                datetime = self.fake.format('future_datetime',
                                            tzinfo=None)
                source_url = "http://www.{}.com/{}".format(
                    self.fake.format('word'), self.fake.format('word'))

                output_file.write("%s|%s|%s|%s|%s\n" %
                                  (feed_id,
                                   title,
                                   text,
                                   datetime,
                                   source_url))

    def generate_public_meetings(self, rows):
        """
        Generate synthetic data for Public Meetings

        """
        header = "id|purpose|date|time|location|contact\n"

        with open('{}public_meetings.csv'.format(self.directory), 'w') \
                as output_file:

            output_file.write(header)
            for meeting_id in range(rows):
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

                output_file.write("%s|%s|%s|%s|%s|%s\n" %
                                  (meeting_id,
                                   purpose,
                                   meeting_date,
                                   time,
                                   location,
                                   contact))

    def generate_license_actions(self, rows):
        """
        Generate synthetic data for License Actions

        """
        header = "id|text|status|date\n"

        with open('{}license_actions.csv'.format(self.directory), 'w') \
                as output_file:

            output_file.write(header)
            for license_action_id in range(rows):
                text = self.fake.format('sentence',
                                        nb_words=10,
                                        variable_nb_words=True,
                                        ext_word_list=None)
                license_action_date = self.fake.format('future_datetime',
                                                       tzinfo=None)
                status = random.choice(["Open", "Closed"])

                output_file.write("%s|%s|%s|%s\n" %
                                  (license_action_id,
                                   text,
                                   status,
                                   license_action_date))

    def generate_crop_findings(self, rows):
        """
        Generate synthetic data for License Actions

        """
        header = "id|description|status|date\n"

        with open('{}crop_findings.csv'.format(self.directory), 'w') \
                as output_file:

            output_file.write(header)
            for crop_finding_id in range(rows):
                description = self.fake.format('sentence',
                                               nb_words=10,
                                               variable_nb_words=True,
                                               ext_word_list=None)
                datetime = self.fake.format('future_datetime',
                                            tzinfo=None)
                status = random.choice(["Open", "Closed"])

                output_file.write("%s|%s|%s|%s\n" %
                                  (crop_finding_id,
                                   description,
                                   status,
                                   datetime))

    def generate_calendar(self, start_year, end_year):
        """
        Generate Calendar

        """
        header = "id|date\n"

        sdate = date(start_year, 1, 1)   # start date
        edate = date(end_year, 12, 31)   # end date

        delta = edate - sdate       # as timedelta

        with open('{}calendar.csv'.format(self.directory), 'w') \
                as output_file:

            output_file.write(header)
            for i in range(delta.days + 1):
                day = sdate + timedelta(days=i)
                output_file.write("%s|%s\n" % (i, day))


if __name__ == '__main__':
    logging.info("Generating synthetic data...")
    if not sys.argv[1:]:
        ARG_PARSER.print_help()
        ARG_PARSER.exit()

    OPTIONS = {}
    try:
        OPTIONS = ARG_PARSER.parse_args()
    except ArgumentError as err:
        ARG_PARSER.print_help()
        ARG_PARSER.exit()

    if not path.exists(OPTIONS.directory):
        os.mkdir(OPTIONS.directory)

    VOGTLE_GENERATOR = VogtleDataGenerator(directory=OPTIONS.directory)
    CONFIG = {
        'inspections': 800,
        'news': 100,
        'public_meetings': 100,
        'start_date': 2019,
        'end_date': 2021,
        'license_actions': 100,
        'crop_findings': 100
    }

    VOGTLE_GENERATOR.generate_inspections(CONFIG['inspections'])
    VOGTLE_GENERATOR.generate_news_feed(CONFIG['news'])
    VOGTLE_GENERATOR.generate_public_meetings(CONFIG['public_meetings'])
    VOGTLE_GENERATOR.generate_calendar(CONFIG['start_date'],
                                       CONFIG['end_date'])
    VOGTLE_GENERATOR.generate_license_actions(CONFIG['license_actions'])
    VOGTLE_GENERATOR.generate_crop_findings(CONFIG['crop_findings'])

    logging.info("Synthetic data generation complete")

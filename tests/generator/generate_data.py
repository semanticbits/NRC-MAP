from datetime import date, timedelta
import random
from faker import Faker
from common.faker_providers import ITAAC


fake = Faker()
fake.add_provider(ITAAC)

directory = './data'


def generate_inspections(rows):
    """
    Generate synthetic data for Inspections
    """
    header = "id|itaac_status|icn_status|effort_required|facility|targeted_flag|target_amt\n"
    data = [header]

    with open('{}/inspections.csv'.format(directory), 'w') as f:
        f.write(header)
        for itaac_id in range(rows):

            itaac_status = fake.itaac_status()
            icn_status = fake.icn_status()
            effort_required = fake.effort_required()
            facility = fake.facility()
            targeted_flag = fake.true_false_flag()
            target_amt = fake.target_amt()

            f.write("{}|{}|{}|{}|{}|{}|{}\n"
                    .format(itaac_id,
                            itaac_status,
                            icn_status,
                            effort_required,
                            facility,
                            targeted_flag,
                            target_amt))


def generate_news_feed(rows):
    """
    Generate synthetic data for News Feed
    """
    header = "id|title|text|datetime|source_url\n"
    data = [header]

    with open('{}/news_feed.csv'.format(directory), 'w') as f:
        f.write(header)
        for feed_id in range(rows):

            title = fake.sentence(
                nb_words=5, variable_nb_words=False, ext_word_list=None)
            text = fake.sentence(
                nb_words=12, variable_nb_words=False, ext_word_list=None)
            datetime = fake.date_time_this_year(
                before_now=True, after_now=True, tzinfo=None)
            source_url = "http://www.{}.com/{}".format(
                fake.word(), fake.word())

            f.write("{}|{}|{}|{}|{}\n"
                    .format(feed_id,
                            title,
                            text,
                            datetime,
                            source_url))


def generate_public_meetings(rows):
    """
    Generate synthetic data for Public Meetings

    """
    header = "id|purpose|date|time|location|contact\n"
    data = [header]

    with open('{}/public_meetings.csv'.format(directory), 'w') as f:
        f.write(header)
        for meeting_id in range(rows):
            phone_number = fake.phone_number()

            purpose = fake.sentence(
                nb_words=10, variable_nb_words=True, ext_word_list=None)
            date = str(fake.date_time_this_year(before_now=True,
                                                   after_now=True, tzinfo=None))[:10]
            time = fake.time(pattern='%H:%M')
            location = fake.address().replace("\n", " ")
            contact = "{} : {}".format(fake.name(), fake.phone_number())

            f.write("{}|{}|{}|{}|{}|{}\n"
                    .format(meeting_id,
                            purpose,
                            date,
                            time,
                            location,
                            contact))


def generate_calendar(start_year, end_year):
    """
    Generate Calendar

    """
    header = "id|date\n"
    data = [header]

    sdate = date(start_year, 1, 1)   # start date
    edate = date(end_year, 12, 31)   # end date

    delta = edate - sdate       # as timedelta

    with open('{}/calendar.csv'.format(directory), 'w') as f:
        f.write(header)
        for i in range(delta.days + 1):
            day = sdate + timedelta(days=i)
            f.write("{}|{}\n".format(i, day))


if __name__ == '__main__':
    generate_inspections(800)
    generate_news_feed(100)
    generate_public_meetings(100)
    generate_calendar(2019, 2021)

import random
from faker import Faker
from common.faker_providers import ITAAC

fake = Faker()
fake.add_provider(ITAAC)

def generate_inspections(rows):
    """
    Generate synthetic data for Inspections
    """
    header = "id|itaac_status|icn_status|effort_required|facility|targeted_flag|target_amt"
    data = [header]

    with open('../data/inspections.csv', 'w') as f:
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
    header = "id|text|datetime|source_url"
    data = [header]

    with open('../data/news_feed.csv', 'w') as f:
        for feed_id in range(rows):

            text = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
            datetime = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
            source_url = "http://www.{}.com/{}".format(fake.word(), fake.word())

            f.write("{}|{}|{}|{}\n"
                .format(feed_id, 
                        text, 
                        datetime, 
                        source_url))


def generate_public_meetings(rows):
    """
    Generate synthetic data for Public Meetings

    """
    header = "id|purpose|datetime|location|contact"
    data = [header]

    with open('../data/public_meetings.csv', 'w') as f:
        for meeting_id in range(rows):
            phone_number = fake.phone_number()

            purpose = fake.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None)
            datetime = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
            location = fake.address().replace("\n", " ")
            contact = "{} : {}".format(fake.name(), fake.phone_number())

            f.write("{}|{}|{}|{}|{}\n"
                .format(meeting_id, 
                        purpose, 
                        datetime, 
                        location, 
                        contact))

if __name__ == '__main__':
    generate_inspections(800)
    generate_news_feed(100)
    generate_public_meetings(100)

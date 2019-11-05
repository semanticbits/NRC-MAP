import random
from faker import Faker
from common.faker_providers import ITAAC

fake = Faker()
fake.add_provider(ITAAC)

def generate_inspections(rows):
    """
    Generate synthetic data for Inspections

    Data will be of the following format:
    id|itaac_status|icn_status|effort_required|facility|targeted_flag|target_amt
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

def generate_feed(rows):
    """
    Generate synthetic data for News Feed and Public Meetings

    Data will be of the following format:
    id|itaac_status|icn_status|effort_required|facility|targeted_flag|target_amt
    """
    header = "id|text|datetime|source_url|meeting_flag"
    data = [header]

    with open('../data/feeds.csv', 'w') as f:
        for feed_id in range(rows):

            text = fake.sentence(nb_words=6, variable_nb_words=True, ext_word_list=None)
            datetime = fake.date_time_this_year(before_now=True, after_now=False, tzinfo=None)
            source_url = "http://www.{}.com/{}".format(fake.word(), fake.word())
            meeting_flag = fake.true_false_flag()

            f.write("{}|{}|{}|{}|{}\n"
                .format(feed_id, 
                        text, 
                        datetime, 
                        source_url, 
                        meeting_flag))

if __name__ == '__main__':
    generate_inspections(800)
    generate_feed(100)

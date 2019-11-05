import random
from faker import Faker
from common.faker_providers import ITAAC

fake = Faker()
fake.add_provider(ITAAC)


def generate_inspections(number_of_inspections):
    """
    Generate synthetic data for Inspections

    Data will be of the following format:
    id|itaac_status|icn_status|effort_required|facility
    """
    header = "id|itaac_status|icn_status|effort_required|facility|targeted_flag|target_amt"
    data = [header]

    for itaac_id in range(number_of_inspections):

        itaac_status = fake.itaac_status()
        icn_status = fake.icn_status()
        effort_required = fake.effort_required()
        facility = fake.facility()
        targeted_flag = fake.targeted_flag()
        target_amt = fake.target_amt()

        data.append("{}|{}|{}|{}|{}|{}|{}"
            .format(itaac_id, 
                    itaac_status, 
                    icn_status, 
                    effort_required, 
                    facility,
                    targeted_flag,
                    target_amt))


    # write array to file
    with open('../data/inspections.csv', 'w') as f:
        for item in data:
            f.write("%s\n" % item)

if __name__ == '__main__':
    generate_inspections(800)

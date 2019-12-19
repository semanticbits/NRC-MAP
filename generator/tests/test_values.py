"""
Configuration values for tests
"""

VOGTLE_CONFIG = {
    'inspections': {
        'filename': "test_data/inspections.csv",
        'row_count': 20,
        'col_count': 6,
        'header': "id|itaac_status|icn_status|est_completion_date|"
                  "facility|targeted_flag"
    },
    'itaac_efforts': {
        'filename': "test_data/itaac_efforts.csv",
        'row_count': 20,
        'col_count': 5,
        'header': "id|itaac_id|effort_type|actual|estimate"
    },
    'news_feed': {
        'filename': "test_data/news_feed.csv",
        'row_count': 30,
        'col_count': 5,
        'header': "id|title|text|datetime|source_url"
    },
    'public_meetings': {
        'filename': "test_data/public_meetings.csv",
        'row_count': 40,
        'col_count': 6,
        'header': "id|purpose|date|time|location|contact"
    },
    'license_actions': {
        'filename': "test_data/license_actions.csv",
        'row_count': 20,
        'col_count': 4,
        'header': "id|text|status|date"
    },
    'crop_findings': {
        'filename': "test_data/crop_findings.csv",
        'row_count': 20,
        'col_count': 4,
        'header': "id|description|status|date"
    },
    'calendar': {
        'filename': "test_data/calendar.csv",
        'row_count': (365*2)+1,
        'col_count': 2,
        'start_year': 2019,
        'end_year': 2020,
        'header': "id|date"
    }
}

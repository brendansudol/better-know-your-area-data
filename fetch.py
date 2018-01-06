import json
import os
import requests

from util.metrics import GEOS, METRIC_FIELDS, OTHER_FIELDS
from util.misc import chunks


API_KEY = os.environ.get('CENSUS_API_KEY')


def make_url(fields, geo):
    base_url = 'https://api.census.gov/data/2016/acs/acs5/profile'

    return '{}?get={}&for={}:*&key={}'.format(
        base_url,
        ','.join(fields),
        geo,
        API_KEY
    )


def main():
    data_by_geoid = {}

    for geo in GEOS:
        print('{}...'.format(geo))

        for i, field_subset in enumerate(chunks(METRIC_FIELDS)):
            print('field chunk {}...'.format(i + 1))

            fields = field_subset + OTHER_FIELDS
            url = make_url(fields, geo)
            print(url)

            response = requests.get(url)
            results = response.json()

            header, rows = results[0], results[1:]
            for row in rows:
                entry = {key: val for key, val in zip(header, row) if key in fields}
                geoid = entry['GEO_ID']

                if geoid not in data_by_geoid:
                    data_by_geoid[geoid] = entry
                else:
                    data_by_geoid[geoid].update(entry)

    # save data locally
    entries = list(data_by_geoid.values())
    print('total entries: {}'.format(len(entries)))

    with open('data/acs.json', 'w') as f:
        json.dump(entries, f)


if __name__ == '__main__':
    main()

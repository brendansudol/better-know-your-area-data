import json

from util.metrics import METRICS, DESC_FIELDS, POP_FIELD


def main():
    # convert raw acs fields to metrics
    with open('data/acs.json') as f:
        acs = json.load(f)

    results = []

    for d in acs:
        if 'Puerto Rico' in d['NAME']:
            continue

        metric_data = {}
        for m in METRICS:

            exp = m.expression
            for field in m.acs_fields:
                exp = exp.replace(field, d[field])

            try:
                value = eval(exp)
            except:
                value = 'N/A'
                print('Could not compute {} for {} ({}); {} -> {}'.format(
                    m.name, d['GEOID'], d['NAME'], m.expression, exp
                ))

            metric_data[m.id] = value

        entry = {field.lower(): d[field] for field in DESC_FIELDS}
        entry.update({'population': d[POP_FIELD], 'metrics': metric_data})
        results.append(entry)

    # add geom info
    with open('data/geom.json') as f:
        geom = json.load(f)
        geom_by_id = {g['geoid']: g for g in geom}

    for d in results:
        g = geom_by_id[d['geoid']]
        d.update({'geom': g['geom'], 'related': g['related']})

    # print example entry
    print('\n{}'.format(results[100]))

    # save data locally
    with open('data/metrics.json', 'w') as f:
        json.dump(results, f)


if __name__ == '__main__':
    main()

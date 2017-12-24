import json

from collections import defaultdict

from scipy.stats import rankdata

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
                value = value / 100 if '%' in m.fmt else value
                value = round(value, 5)
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

    # add rank info
    geos, ranks = [], {}
    by_metric, by_geo = defaultdict(list), defaultdict(dict)

    for d in results:
        if d['sumlevel'] != '050':
            continue

        geos.append(d['geoid'])

        for k, v in d['metrics'].items():
            by_metric[k].append(v)

    for metric, values in by_metric.items():
        ranks[metric] = rankdata(values, method='min')

    for metric in by_metric.keys():
        for geoid, val, rank in zip(geos, by_metric[metric], ranks[metric]):
            by_geo[geoid][metric] = {'value': val, 'rank': int(rank)}

    for d in results:
        if d['sumlevel'] != '050':
            continue

        metrics_w_rank = by_geo[d['geoid']]

        # make sure things match
        ex = 'high_school_plus'
        if d['metrics'][ex] != metrics_w_rank[ex]['value']:
            raise ValueError('Metrics do not match for {}'.format(d['geoid']))

        # replace metrics dict with one containing value & rank
        d.update({'metrics': metrics_w_rank})

    # print example entry
    print('\n{}'.format(results[100]))

    # save data locally
    with open('data/metrics.json', 'w') as f:
        json.dump(results, f)


if __name__ == '__main__':
    main()

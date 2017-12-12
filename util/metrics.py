from util.misc import extract_fields, flatten


METRICS = [
    (
        'Family households (families) With own children of the householder under 18 years',
        'DP02_0003PE',
        'HOUSEHOLDS BY TYPE'
    ),
    (
        'Households with one or more people under 18 years',
        'DP02_0013PE',
        'HOUSEHOLDS BY TYPE'
    ),
    (
        'Households with one or more people 65 years and over',
        'DP02_0014PE',
        'HOUSEHOLDS BY TYPE'
    ),
    (
        'Average household size',
        'DP02_0015E',
        'HOUSEHOLDS BY TYPE'
    ),
    (
        'Average family size',
        'DP02_0016E',
        'HOUSEHOLDS BY TYPE'
    ),
    (
        'Percent married (male and female, 15 years and over)',
        '(DP02_0026E + DP02_0032E) / (DP02_0024E + DP02_0030E)',
        'MARITAL STATUS'
    ),
    (
        'Percent high school graduate or higher',
        'DP02_0066PE',
        'EDUCATIONAL ATTAINMENT'
    ),
    (
        "Percent bachelor's degree or higher",
        'DP02_0067PE',
        'EDUCATIONAL ATTAINMENT'
    ),
    (
        'Percent civilian veterans',
        'DP02_0069PE',
        'VETERAN STATUS'
    ),
    (
        '1 year ago, Same house',
        'DP02_0079PE',
        'RESIDENCE 1 YEAR AGO'
    ),
    (
        '1 year ago, Same house',
        'DP02_0079PE',
        'RESIDENCE 1 YEAR AGO'
    ),
    (
        '1 year ago, Different house, Same state',
        'DP02_0081PE + DP02_0083PE',
        'RESIDENCE 1 YEAR AGO'
    ),
    (
        '1 year ago, Different house, Different state or abroad',
        'DP02_0084PE + DP02_0085PE',
        'RESIDENCE 1 YEAR AGO'
    ),
    (
        'Native born (Born in US, PR, or abroad to American parent(s)',
        'DP02_0087PE',
        'PLACE OF BIRTH'
    ),
    (
        'Born in state of residence',
        'DP02_0089PE',
        'PLACE OF BIRTH'
    ),
    (
        'Foreign born',
        'DP02_0092PE',
        'PLACE OF BIRTH'
    ),
    (
        'English only',
        'DP02_0111PE',
        'LANGUAGE SPOKEN AT HOME'
    ),
    (
        'Language other than English',
        'DP02_0112PE',
        'LANGUAGE SPOKEN AT HOME'
    ),
    (
        'American Ancestry',
        'DP02_0123PE',
        'ANCESTRY'
    ),
    (
        'English Ancestry',
        'DP02_0128PE',
        'ANCESTRY'
    ),
    (
        'German Ancestry',
        'DP02_0131PE',
        'ANCESTRY'
    ),
    (
        'Irish Ancestry',
        'DP02_0134PE',
        'ANCESTRY'
    ),
    (
        'Italian Ancestry',
        'DP02_0135PE',
        'ANCESTRY'
    ),
    (
        'Unemployment Rate',
        'DP03_0009PE',
        'EMPLOYMENT STATUS'
    ),
    (
        'Commute to work via public transportation',
        'DP03_0021PE',
        'COMMUTING TO WORK'
    ),
    (
        'Work at home',
        'DP03_0024PE',
        'COMMUTING TO WORK'
    ),
    (
        'Mean travel time to work (minutes)',
        'DP03_0025E',
        'COMMUTING TO WORK'
    ),
    (
        'Industry - Educational services, and health care and social assistance',
        'DP03_0042PE',
        'INDUSTRY'
    ),
    (
        'Industry - Retail trade',
        'DP03_0037PE',
        'INDUSTRY'
    ),
    (
        'Industry - Professional, scientific, and management, and administrative and waste management services',
        'DP03_0041PE',
        'INDUSTRY'
    ),
    (
        'Industry - Manufacturing',
        'DP03_0035PE',
        'INDUSTRY'
    ),
    (
        'Industry - Arts, entertainment, and recreation, and accommodation and food services',
        'DP03_0043PE',
        'INDUSTRY'
    ),
    (
        'Industry - Other',
        '1 - (DP03_0042PE + DP03_0037PE + DP03_0041PE + DP03_0035PE + DP03_0043PE)',
        'INDUSTRY'
    ),
    (
        'Median household income (dollars)',
        'DP03_0062E',
        'INCOME AND BENEFITS'
    ),
    (
        'Mean household income (dollars)',
        'DP03_0063E',
        'INCOME AND BENEFITS'
    ),
    (
        'Median family income (dollars)',
        'DP03_0086E',
        'INCOME AND BENEFITS'
    ),
    (
        'Mean family income (dollars)',
        'DP03_0087E',
        'INCOME AND BENEFITS'
    ),
    (
        'With health insurance coverage',
        'DP03_0096PE',
        'HEALTH INSURANCE COVERAGE'
    ),
    (
        'Percent of families with income below poverty level',
        'DP03_0119PE',
        'PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL'
    ),
    (
        'Median rooms in housing unit',
        'DP04_0037E',
        'ROOMS'
    ),
    (
        'Owner-occupied housing unit',
        'DP04_0046PE',
        'HOUSING TENURE'
    ),
    (
        'Renter-occupied',
        'DP04_0047PE',
        'HOUSING TENURE'
    ),
    (
        'Median (dollars), Owner-occupied units, Value',
        'DP04_0089E',
        'VALUE'
    ),
    (
        'Percent $1M+ houses',
        'DP04_0088PE',
        'VALUE'
    ),
    (
        'Median (dollars), Monthly owner costs, With mortgage',
        'DP04_0101E',
        'SELECTED MONTHLY OWNER COSTS (SMOC)'
    ),
    (
        'Median (dollars), Occupied units paying rent',
        'DP04_0134E',
        'GROSS RENT'
    ),
    (
        'Total population',
        'DP05_0001E',
        'SEX AND AGE'
    ),
    (
        'Median age (years)',
        'DP05_0017E',
        'SEX AND AGE'
    ),
    (
        '21 years and over',
        'DP05_0019PE',
        'SEX AND AGE'
    ),
    (
        '65 years and over',
        'DP05_0021PE',
        'SEX AND AGE'
    ),
    (
        'White (percent)',
        'DP05_0059PE',
        'RACE'
    ),
    (
        'Black or African American (percent)',
        'DP05_0060PE',
        'RACE'
    ),
    (
        'Asian (percent)',
        'DP05_0062PE',
        'RACE'
    ),
    (
        'Some other race (percent)',
        '1 - (DP05_0059PE + DP05_0060PE + DP05_0062PE)',
        'RACE'
    ),
    (
        'Hispanic or Latino (of any race)',
        'DP05_0066PE',
        'HISPANIC OR LATINO AND RACE'
    ),
]

METRIC_FIELDS = sorted(list(set(flatten(
    extract_fields(exp) for _, exp, __ in METRICS
))))

OTHER_FIELDS = [
    'NAME',
    'GEOID',
    'SUMLEVEL',
]

GEOS = [
    'us',
    'state',
    'county',
]

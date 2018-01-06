import re

from util.misc import flatten


class Metric:
    ACS_FIELD_REGEX = re.compile('DP\d{2}_\d{4}[A-Z]{1,2}')

    def __init__(self, id, name, expression, category, acs_header, fmt='.1%'):
        self.id = id
        self.name = name
        self.expression = expression
        self.category = category
        self.acs_header = acs_header
        self.fmt = fmt

    def __repr__(self):
        return self.name

    @property
    def acs_fields(self):
        return self.ACS_FIELD_REGEX.findall(self.expression)

    def to_dict(self, detailed=False):
        datum = {
            'id': self.id,
            'name': self.name,
            'fmt': self.fmt,
            'category': self.category,
        }

        if detailed:
            datum.update({
                'expression': self.expression,
                'acs_fields': self.acs_fields,
                'acs_header': self.acs_header,
            })

        return datum


METRICS = [
    # Metric(
    #     'families_w_kids',
    #     'Families with children under 18 years',
    #     'DP02_0003PE',
    #     'Social',
    #     'HOUSEHOLDS BY TYPE'
    # ),
    Metric(
        'households_w_kids',
        'Households with 1+ people under 18 years',
        'DP02_0013PE',
        'Social',
        'HOUSEHOLDS BY TYPE'
    ),
    Metric(
        'households_w_elderly',
        'Households with 1+ people 65 years and over',
        'DP02_0014PE',
        'Social',
        'HOUSEHOLDS BY TYPE'
    ),
    Metric(
        'avg_household_size',
        'Average household size',
        'DP02_0015E',
        'Social',
        'HOUSEHOLDS BY TYPE',
        ',.1f',
    ),
    Metric(
        'avg_family_size',
        'Average family size',
        'DP02_0016E',
        'Social',
        'HOUSEHOLDS BY TYPE',
        ',.1f',
    ),
    Metric(
        'married',
        'Currently married (15 years and over)',
        'round((DP02_0026E + DP02_0032E) / (DP02_0024E + DP02_0030E) * 100, 1)',
        'Social',
        'MARITAL STATUS'
    ),
    Metric(
        'high_school_plus',
        'High school graduate or higher',
        'DP02_0066PE',
        'Social',
        'EDUCATIONAL ATTAINMENT'
    ),
    Metric(
        'bach_degree_plus',
        "Bachelor's degree or higher",
        'DP02_0067PE',
        'Social',
        'EDUCATIONAL ATTAINMENT'
    ),
    Metric(
        'vets',
        'Civilian veterans',
        'DP02_0069PE',
        'Social',
        'VETERAN STATUS'
    ),
    Metric(
        'last_yr_same_house',
        'Residence 1 year ago: same house',
        'DP02_0079PE',
        'Housing',
        'RESIDENCE 1 YEAR AGO'
    ),
    Metric(
        'last_yr_diff_house_same_state',
        'Residence 1 year ago: different house, same state',
        'round(DP02_0081PE + DP02_0083PE, 1)',
        'Housing',
        'RESIDENCE 1 YEAR AGO'
    ),
    Metric(
        'last_yr_diff_house_diff_state',
        'Residence 1 year ago: different house, different state',
        'round(DP02_0084PE + DP02_0085PE, 1)',
        'Housing',
        'RESIDENCE 1 YEAR AGO'
    ),
    Metric(
        'native_born',
        'Native born (US, PR, or abroad to American parents)',
        'DP02_0087PE',
        'Social',
        'PLACE OF BIRTH'
    ),
    Metric(
        'foreign_born',
        'Foreign born',
        'DP02_0092PE',
        'Social',
        'PLACE OF BIRTH'
    ),
    Metric(
        'born_in_state_of_residence',
        'Born in state of residence',
        'DP02_0089PE',
        'Social',
        'PLACE OF BIRTH'
    ),
    Metric(
        'language_english_only',
        'Language spoken at home: English only',
        'DP02_0111PE',
        'Social',
        'LANGUAGE SPOKEN AT HOME'
    ),
    Metric(
        'language_not_english',
        'Language spoken at home: Non-English language',
        'DP02_0112PE',
        'Social',
        'LANGUAGE SPOKEN AT HOME'
    ),
    Metric(
        'ancestry_american',
        'American',
        'DP02_0123PE',
        'Ancestry',
        'ANCESTRY'
    ),
    Metric(
        'ancestry_english',
        'English',
        'DP02_0128PE',
        'Ancestry',
        'ANCESTRY'
    ),
    Metric(
        'ancestry_german',
        'German',
        'DP02_0131PE',
        'Ancestry',
        'ANCESTRY'
    ),
    Metric(
        'ancestry_irish',
        'Irish',
        'DP02_0134PE',
        'Ancestry',
        'ANCESTRY'
    ),
    Metric(
        'ancestry_italian',
        'Italian',
        'DP02_0135PE',
        'Ancestry',
        'ANCESTRY'
    ),
    Metric(
        'ancestry_polish',
        'Polish',
        'DP02_0138PE',
        'Ancestry',
        'ANCESTRY'
    ),
    Metric(
        'ancestry_other',
        'Other ancestral origin',
        'round(100 - (DP02_0123PE + DP02_0128PE + DP02_0131PE + DP02_0134PE + DP02_0135PE + DP02_0138PE), 1)',
        'Ancestry',
        'ANCESTRY'
    ),
    Metric(
        'unemployment_rate',
        'Unemployment rate',
        'DP03_0009PE',
        'Economics',
        'EMPLOYMENT STATUS'
    ),
    Metric(
        'commute_via_public_transport',
        'Commute to work via public transportation',
        'DP03_0021PE',
        'Economics',
        'COMMUTING TO WORK'
    ),
    Metric(
        'work_at_home',
        'Work from home',
        'DP03_0024PE',
        'Economics',
        'COMMUTING TO WORK'
    ),
    Metric(
        'travel_time_to_work',
        'Mean travel time to work (in minutes)',
        'DP03_0025E',
        'Economics',
        'COMMUTING TO WORK',
        ',.0f',
    ),
    Metric(
        'industry_edu_healthcare_social',
        'Educational services, and health care and social assistance',
        'DP03_0042PE',
        'Business',
        'INDUSTRY'
    ),
    Metric(
        'industry_retail_trade',
        'Retail trade',
        'DP03_0037PE',
        'Business',
        'INDUSTRY'
    ),
    Metric(
        'industry_prof_science_manage',
        'Professional, scientific, and management, and administrative and waste management services',
        'DP03_0041PE',
        'Business',
        'INDUSTRY'
    ),
    Metric(
        'industry_manufacturing',
        'Manufacturing',
        'DP03_0035PE',
        'Business',
        'INDUSTRY'
    ),
    Metric(
        'industry_arts_rec_food',
        'Arts, entertainment, and recreation, and accommodation and food services',
        'DP03_0043PE',
        'Business',
        'INDUSTRY'
    ),
    Metric(
        'industry_other',
        'Other',
        'round(100 - (DP03_0042PE + DP03_0037PE + DP03_0041PE + DP03_0035PE + DP03_0043PE), 1)',
        'Business',
        'INDUSTRY'
    ),
    Metric(
        'median_household_income',
        'Median household income',
        'DP03_0062E',
        'Economics',
        'INCOME AND BENEFITS',
        '$,.0f',
    ),
    Metric(
        'mean_household_income',
        'Mean household income',
        'DP03_0063E',
        'Economics',
        'INCOME AND BENEFITS',
        '$,.0f',
    ),
    # Metric(
    #     'median_family_income',
    #     'Median family income',
    #     'DP03_0086E',
    #     'Economics',
    #     'INCOME AND BENEFITS',
    #     '$,.0f',
    # ),
    # Metric(
    #     'mean_family_income',
    #     'Mean family income',
    #     'DP03_0087E',
    #     'Economics',
    #     'INCOME AND BENEFITS',
    #     '$,.0f',
    # ),
    Metric(
        'per_capita_income',
        'Per capita income',
        'DP03_0088E',
        'Economics',
        'INCOME AND BENEFITS',
        '$,.0f',
    ),
    Metric(
        'health_coverage',
        'People with health insurance coverage',
        'DP03_0096PE',
        'Economics',
        'HEALTH INSURANCE COVERAGE'
    ),
    Metric(
        'families_poverty',
        'Families with income below poverty level',
        'DP03_0119PE',
        'Economics',
        'PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL'
    ),
    Metric(
        'median_rooms',
        'Median rooms',
        'DP04_0037E',
        'Housing',
        'ROOMS',
        ',.1f',
    ),
    Metric(
        'owner_occupied',
        'Owner-occupied',
        'DP04_0046PE',
        'Housing',
        'HOUSING TENURE'
    ),
    Metric(
        'renter_occupied',
        'Renter-occupied',
        'DP04_0047PE',
        'Housing',
        'HOUSING TENURE'
    ),
    Metric(
        'median_house_value',
        'Median value (owner-occupied units)',
        'DP04_0089E',
        'Housing',
        'VALUE',
        '$,.0f',
    ),
    Metric(
        'houses_million_plus',
        'Percent of houses valued at $1M+',
        'DP04_0088PE',
        'Housing',
        'VALUE'
    ),
    Metric(
        'mortgage_monthly_costs',
        'Median monthly owner costs (with mortgage)',
        'DP04_0101E',
        'Housing',
        'SELECTED MONTHLY OWNER COSTS (SMOC)',
        '$,.0f',
    ),
    Metric(
        'rent_monthly_costs',
        'Median monthly costs (occupied units paying rent)',
        'DP04_0134E',
        'Housing',
        'GROSS RENT',
        '$,.0f',
    ),
    Metric(
        'median_age',
        'Median age (in years)',
        'DP05_0017E',
        'Demographics',
        'SEX AND AGE',
        ',.0f',
    ),
    Metric(
        '_21_and_over',
        '21 years and over',
        'DP05_0019PE',
        'Demographics',
        'SEX AND AGE'
    ),
    Metric(
        '_65_and_over',
        '65 years and over',
        'DP05_0021PE',
        'Demographics',
        'SEX AND AGE'
    ),
    Metric(
        'white',
        'White',
        'DP05_0059PE',
        'Demographics',
        'RACE'
    ),
    Metric(
        'black',
        'Black or African American',
        'DP05_0060PE',
        'Demographics',
        'RACE'
    ),
    Metric(
        'asian',
        'Asian',
        'DP05_0062PE',
        'Demographics',
        'RACE'
    ),
    Metric(
        'american_indian',
        'American Indian and Alaska Native',
        'DP05_0061PE',
        'Demographics',
        'RACE'
    ),
    Metric(
        'other_race',
        'Some other race',
        'DP05_0063PE + DP05_0064PE',
        'Demographics',
        'RACE'
    ),
    Metric(
        'hispanic_latino',
        'Hispanic or Latino',
        'DP05_0066PE',
        'Demographics',
        'HISPANIC OR LATINO AND RACE'
    ),
]

METRIC_FIELDS = sorted(list(set(flatten(m.acs_fields for m in METRICS))))

DESC_FIELDS = [
    'GEO_ID',
    'NAME',
    'SUMLEVEL',
]

POP_FIELD = 'DP05_0001E'

OTHER_FIELDS = DESC_FIELDS + [POP_FIELD]

GEOS = [
    'us',
    'state',
    'county',
]

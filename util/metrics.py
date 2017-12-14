import re

from util.misc import flatten


class Metric:
    ACS_FIELD_REGEX = re.compile('DP\d{2}_\d{4}[A-Z]{1,2}')

    def __init__(self, id, name, expression, category=None):
        self.id = id
        self.name = name
        self.expression = expression
        self.category = category

    def __repr__(self):
        return self.name

    @property
    def acs_fields(self):
        return self.ACS_FIELD_REGEX.findall(self.expression)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'expression': self.expression,
            'acs_fields': self.acs_fields,
            'category': self.category,
        }


METRICS = [
    Metric(
        'families_w_kids',
        'Families with children under 18 years',
        'DP02_0003PE',
        'HOUSEHOLDS BY TYPE'
    ),
    Metric(
        'households_w_kids',
        'Households with 1+ people under 18 years',
        'DP02_0013PE',
        'HOUSEHOLDS BY TYPE'
    ),
    Metric(
        'households_w_elderly',
        'Households with 1+ people 65 years and over',
        'DP02_0014PE',
        'HOUSEHOLDS BY TYPE'
    ),
    Metric(
        'avg_household_size',
        'Average household size',
        'DP02_0015E',
        'HOUSEHOLDS BY TYPE'
    ),
    Metric(
        'avg_family_size',
        'Average family size',
        'DP02_0016E',
        'HOUSEHOLDS BY TYPE'
    ),
    Metric(
        'married',
        'Percent married, 15 years and over',
        'round((DP02_0026E + DP02_0032E) / (DP02_0024E + DP02_0030E) * 100, 1)',
        'MARITAL STATUS'
    ),
    Metric(
        'high_school_plus',
        'High school graduate or higher',
        'DP02_0066PE',
        'EDUCATIONAL ATTAINMENT'
    ),
    Metric(
        'bach_degree_plus',
        "Bachelor's degree or higher",
        'DP02_0067PE',
        'EDUCATIONAL ATTAINMENT'
    ),
    Metric(
        'vets',
        'Civilian veterans',
        'DP02_0069PE',
        'VETERAN STATUS'
    ),
    Metric(
        'last_yr_same_house',
        'Residence 1 year ago: same house',
        'DP02_0079PE',
        'RESIDENCE 1 YEAR AGO'
    ),
    Metric(
        'last_yr_diff_house_same_state',
        'Residence 1 year ago: different house, same state',
        'round(DP02_0081PE + DP02_0083PE, 1)',
        'RESIDENCE 1 YEAR AGO'
    ),
    Metric(
        'last_yr_diff_house_diff_state',
        'Residence 1 year ago: different house, different state',
        'round(DP02_0084PE + DP02_0085PE, 1)',
        'RESIDENCE 1 YEAR AGO'
    ),
    Metric(
        'native_born',
        'Native born (US, PR, or abroad to American parents)',
        'DP02_0087PE',
        'PLACE OF BIRTH'
    ),
    Metric(
        'foreign_born',
        'Foreign born',
        'DP02_0092PE',
        'PLACE OF BIRTH'
    ),
    Metric(
        'born_in_state_of_residence',
        'Born in state of residence',
        'DP02_0089PE',
        'PLACE OF BIRTH'
    ),
    Metric(
        'language_english_only',
        'Language spoken at home: English only',
        'DP02_0111PE',
        'LANGUAGE SPOKEN AT HOME'
    ),
    Metric(
        'language_not_english',
        'Language spoken at home: language other than English',
        'DP02_0112PE',
        'LANGUAGE SPOKEN AT HOME'
    ),
    Metric(
        'ancestry_american',
        'Ancestry: American',
        'DP02_0123PE',
        'ANCESTRY'
    ),
    Metric(
        'ancestry_english',
        'Ancestry: English',
        'DP02_0128PE',
        'ANCESTRY'
    ),
    Metric(
        'ancestry_german',
        'Ancestry: German',
        'DP02_0131PE',
        'ANCESTRY'
    ),
    Metric(
        'ancestry_irish',
        'Ancestry: Irish',
        'DP02_0134PE',
        'ANCESTRY'
    ),
    Metric(
        'ancestry_italian',
        'Ancestry: Italian',
        'DP02_0135PE',
        'ANCESTRY'
    ),
    Metric(
        'unemployment_rate',
        'Unemployment rate',
        'DP03_0009PE',
        'EMPLOYMENT STATUS'
    ),
    Metric(
        'commute_via_public_transport',
        'Commute to work via public transportation',
        'DP03_0021PE',
        'COMMUTING TO WORK'
    ),
    Metric(
        'work_at_home',
        'Work at home',
        'DP03_0024PE',
        'COMMUTING TO WORK'
    ),
    Metric(
        'travel_time_to_work',
        'Mean travel time to work (minutes)',
        'DP03_0025E',
        'COMMUTING TO WORK'
    ),
    Metric(
        'industry_edu_healthcare_social',
        'Industry: Educational services, and health care and social assistance',
        'DP03_0042PE',
        'INDUSTRY'
    ),
    Metric(
        'industry_retail_trade',
        'Industry: Retail trade',
        'DP03_0037PE',
        'INDUSTRY'
    ),
    Metric(
        'industry_prof_science_manage',
        'Industry: Professional, scientific, and management, and administrative and waste management services',
        'DP03_0041PE',
        'INDUSTRY'
    ),
    Metric(
        'industry_manufacturing',
        'Industry: Manufacturing',
        'DP03_0035PE',
        'INDUSTRY'
    ),
    Metric(
        'industry_arts_rec_food',
        'Industry: Arts, entertainment, and recreation, and accommodation and food services',
        'DP03_0043PE',
        'INDUSTRY'
    ),
    Metric(
        'industry_other',
        'Industry: Other',
        'round(100 - (DP03_0042PE + DP03_0037PE + DP03_0041PE + DP03_0035PE + DP03_0043PE), 1)',
        'INDUSTRY'
    ),
    Metric(
        'median_household_income',
        'Median household income',
        'DP03_0062E',
        'INCOME AND BENEFITS'
    ),
    Metric(
        'mean_household_income',
        'Mean household income',
        'DP03_0063E',
        'INCOME AND BENEFITS'
    ),
    Metric(
        'median_family_income',
        'Median family income',
        'DP03_0086E',
        'INCOME AND BENEFITS'
    ),
    Metric(
        'mean_family_income',
        'Mean family income',
        'DP03_0087E',
        'INCOME AND BENEFITS'
    ),
    Metric(
        'health_coverage',
        'People with health insurance coverage',
        'DP03_0096PE',
        'HEALTH INSURANCE COVERAGE'
    ),
    Metric(
        'families_poverty',
        'Families with income below poverty level',
        'DP03_0119PE',
        'PERCENTAGE OF FAMILIES AND PEOPLE WHOSE INCOME IN THE PAST 12 MONTHS IS BELOW THE POVERTY LEVEL'
    ),
    Metric(
        'median_rooms',
        'Median rooms',
        'DP04_0037E',
        'ROOMS'
    ),
    Metric(
        'owner_occupied',
        'Owner-occupied',
        'DP04_0046PE',
        'HOUSING TENURE'
    ),
    Metric(
        'renter_occupied',
        'Renter-occupied',
        'DP04_0047PE',
        'HOUSING TENURE'
    ),
    Metric(
        'median_house_value',
        'Median value, Owner-occupied units',
        'DP04_0089E',
        'VALUE'
    ),
    Metric(
        'houses_million_plus',
        'Percent of houses valued at $1M+',
        'DP04_0088PE',
        'VALUE'
    ),
    Metric(
        'mortgage_monthly_costs',
        'Median monthly owner costs (with mortgage)',
        'DP04_0101E',
        'SELECTED MONTHLY OWNER COSTS (SMOC)'
    ),
    Metric(
        'rent_monthly_costs',
        'Median cost, occupied units paying rent',
        'DP04_0134E',
        'GROSS RENT'
    ),
    Metric(
        'median_age',
        'Median age (years)',
        'DP05_0017E',
        'SEX AND AGE'
    ),
    Metric(
        '_21_and_over',
        '21 years and over',
        'DP05_0019PE',
        'SEX AND AGE'
    ),
    Metric(
        '_65_and_over',
        '65 years and over',
        'DP05_0021PE',
        'SEX AND AGE'
    ),
    Metric(
        'white',
        'Percent White',
        'DP05_0059PE',
        'RACE'
    ),
    Metric(
        'black',
        'Percent Black or African American',
        'DP05_0060PE',
        'RACE'
    ),
    Metric(
        'asian',
        'Percent Asian',
        'DP05_0062PE',
        'RACE'
    ),
    Metric(
        'other_race',
        'Percent some other race',
        'round(100 - (DP05_0059PE + DP05_0060PE + DP05_0062PE), 1)',
        'RACE'
    ),
    Metric(
        'hispanic_latino',
        'Hispanic or Latino',
        'DP05_0066PE',
        'HISPANIC OR LATINO AND RACE'
    ),
]

METRIC_FIELDS = sorted(list(set(flatten(m.acs_fields for m in METRICS))))

DESC_FIELDS = [
    'NAME',
    'GEOID',
    'SUMLEVEL',
]

POP_FIELD = 'DP05_0001E'

OTHER_FIELDS = DESC_FIELDS + [POP_FIELD]

GEOS = [
    'us',
    'state',
    'county',
]

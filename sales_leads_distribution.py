# TODO unit tests for shape of data
# NOTE assuming all leads start their day without any prior allocations


# DONE write test cases
"""
{'lead_id': 1, 'size': 600, 'HQ': "US"} => B, C, D
{'lead_id': 2, 'size': 1, 'HQ': "Any"} =>
{'lead_id': 3, 'size': 250, 'HQ': "Any"}
{'lead_id': 4, 'size': 1000, 'HQ': "US"}
{'lead_id': 5, 'size': 9500, 'HQ': "US"}
{'lead_id': 6, 'size': 33, 'HQ': "US"}
{'lead_id': 7, 'size': 200000, 'HQ': "Any"}

"""

import math

sales_team_config = {'A': {'company_size': {'min': 0,
                                            'max': 500},
                           'HQ_location': "US"},
                     'B': {'company_size': {'min': 0,
                                            'max': math.inf},
                           'HQ_location': "US"},
                     'C': {'company_size': {'min': 500,
                                            'max': math.inf},
                           'HQ_location': "Any"},
                     'D': {'company_size': {'min': 0,
                                            'max': math.inf},
                           'HQ_location': "Any"}
                     }


# print({k: v for k, v in sales_team_config.items() if v['company_size']['min'] > -math.inf})


# print(sales_team_config['B']['company_size']['max'])


def eligible_candidates_size(a_lead):
    size = a_lead['size']
    # TODO can be a separate function
    return {k: v for k, v in sales_team_config.items() if v['company_size']['min'] < size < v['company_size']['max']}


#
# print(eligible_candidates_size({'lead_id': 1, 'size': 600, 'HQ': "US"}))
# print(eligible_candidates_size({'lead_id': 2, 'size': 1, 'HQ': "Any"}))
# print(eligible_candidates_size({'lead_id': 3, 'size': 250, 'HQ': "Any"}))
# print(eligible_candidates_size({'lead_id': 4, 'size': 1000, 'HQ': "US"}))
# print(eligible_candidates_size({'lead_id': 5, 'size': 9500, 'HQ': "US"}))
# print(eligible_candidates_size({'lead_id': 6, 'size': 33, 'HQ': "US"}))
# print(eligible_candidates_size({'lead_id': 7, 'size': 200000, 'HQ': "Any"}))
#

def eligible_candidates_location(a_lead):
    hq = a_lead['HQ']
    return {k: v for k, v in sales_team_config.items() if v['HQ_location'] == hq}


# print(eligible_candidates_location({'lead_id': 1, 'size': 600, 'HQ': "US"}))
# print(eligible_candidates_location({'lead_id': 2, 'size': 1, 'HQ': "Any"}))
# print(eligible_candidates_location({'lead_id': 3, 'size': 250, 'HQ': "Any"}))


# print(eligible_candidates_location({'lead_id': 4, 'size': 1000, 'HQ': "US"}))
# print(eligible_candidates_location({'lead_id': 5, 'size': 9500, 'HQ': "US"}))
# print(eligible_candidates_location({'lead_id': 6, 'size': 33, 'HQ': "US"}))
# print(eligible_candidates_location({'lead_id': 7, 'size': 200000, 'HQ': "Any"}))

def eligible_candidates(a_lead):
    size = a_lead['size']
    hq = a_lead['HQ']
    print(a_lead)
    return {k: v for k, v in sales_team_config.items() if
            v['company_size']['min'] < size < v['company_size']['max'] and \
            v['HQ_location'] == hq}


print(eligible_candidates({'lead_id': 1, 'size': 600, 'HQ': "US"}))
print(eligible_candidates({'lead_id': 2, 'size': 1, 'HQ': "Any"}))
print(eligible_candidates({'lead_id': 3, 'size': 250, 'HQ': "Any"}))
print(eligible_candidates({'lead_id': 4, 'size': 1000, 'HQ': "US"}))
print(eligible_candidates({'lead_id': 5, 'size': 9500, 'HQ': "US"}))
print(eligible_candidates({'lead_id': 6, 'size': 33, 'HQ': "US"}))
print(eligible_candidates({'lead_id': 7, 'size': 200000, 'HQ': "Any"}))

# def allocate_a_lead(a_lead, config):
# mutating the config object

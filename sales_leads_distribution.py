import math


def get_eligible_candidates(a_lead, config):
    """
    This function computes the eligible sales_team member as per a specific company lead.

    It filters out the eligible candidates based on the `HQ` and `size` of a lead
    and the individual parameter for a sales team member such as `company_size` and `HQ_location`

    Parameters:
    leads (list of dict values): The data regarding the singular company lead
    config (dict): The config which encapsulates the state of sales_team

    Returns:
    (list of dict): Returns a list of eligible candidates

    """

    size = a_lead['size']
    hq = a_lead['HQ']
    eligible_candidates_dict = {}
    for k, v in config.items():
        if v['company_size']['min'] <= size <= v['company_size']['max'] and v['HQ_location'] == hq:
            eligible_candidates_dict[k] = v
    return eligible_candidates_dict


def allocate_a_lead(a_lead, config):
    """
    This is a helper function which works only with a single company lead dict and the state of the sales_team members


    Parameters:
    leads (list of dict values): The data regarding the singular company lead
    config (dict): The config which encapsulates the state of sales_team

    Returns:
    (dict): Returns the allocated sales_team member for a given lead

    """
    eligible_candidates = get_eligible_candidates(a_lead, config)
    sorted_by_leads = sorted(eligible_candidates.items(), key=lambda item: item[1]['leads_count'])
    candidate_name = sorted_by_leads[0][0]
    sales_team_config[candidate_name]['leads_count'] += 1
    return {'lead_id': a_lead['lead_id'], 'assigned_to': candidate_name}


def allocate_leads(leads, config):
    """
    This function is the main public API which allocates the given leads to the sales team members

    It works by relying on a helper function `allocate_a_lead` which is simply iterated over the input `leads`
    and generates the ideal sales_team member for that particular lead.

    Parameters:
    leads (list of dict): The data regarding the company leads
    config (dict): The config which encapsulates the state of sales_team

    Returns:
    (list of dict): Returns the allocated sales_team member per lead as per the configuration

    """
    allocated_leads = []
    for a_lead in leads:
        allocated_leads.append(allocate_a_lead(a_lead, config))
    return allocated_leads


# ======================
# Test cases
# ======================


sales_team_config = {'A': {'company_size': {'min': 0,
                                            'max': 500},
                           'HQ_location': "US",
                           'leads_count': 0},
                     'B': {'company_size': {'min': 0,
                                            'max': math.inf},
                           'HQ_location': "US",
                           'leads_count': 0},
                     'C': {'company_size': {'min': 500,
                                            'max': math.inf},
                           'HQ_location': "Any",
                           'leads_count': 0},
                     'D': {'company_size': {'min': 0,
                                            'max': math.inf},
                           'HQ_location': "Any",
                           'leads_count': 0}
                     }

leads = [
    {'lead_id': 1, 'size': 600, 'HQ': "US"},
    {'lead_id': 2, 'size': 1, 'HQ': "Any"},
    {'lead_id': 3, 'size': 250, 'HQ': "Any"},
    {'lead_id': 4, 'size': 1000, 'HQ': "US"},
    {'lead_id': 5, 'size': 9500, 'HQ': "US"},
    {'lead_id': 6, 'size': 33, 'HQ': "US"},
    {'lead_id': 7, 'size': 200000, 'HQ': "Any"},
    {'lead_id': 8, 'size': 500, 'HQ': "Any"}
]

print("allocate leads: ", allocate_leads(leads, sales_team_config))
print("sales_team_config: ", sales_team_config)

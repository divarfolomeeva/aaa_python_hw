from json_dict_processing import create_processor

config_prize = {
    'prize_amount': ['prizeAmount'],
    'prize_amount_adjusted': ['prizeAmountAdjusted'],
    'award_year': (['awardYear'], int),
    'category_en': ['category', 'en'],
    'prize_status': ['prizeStatus'],
}


def prize_processor():
    return create_processor(config_prize, list_processor=True)
import json
import random

f = open('quotes.json')

quotes_list = json.load(f)

def getQuote(quotes_list = quotes_list):
    """_summary_

    Args:
        quotes_list (_type_, optional): _description_. Defaults to quotes_list.

    Returns:
        _type_: _description_
    """
    # random_int = random.randint(0,len(quotes_list)-1)
    # selected_obj = quotes_list[random_int]
    # return selected_obj
    return random.choice(quotes_list)
import json
import random

f = open('quotes.json')

quotes_list = json.load(f)

def getQuote(quotes_list = quotes_list):
    """This functions takes dictionary of quotes as the input and selects and object/quote from the dictionary.

    Args:
        quotes_list (dictionary, optional): This is dictionary with quotes that we create. Defaults to quotes_list.

    Returns:
        dictionary: returned in the form of dictionary
    """
    # random_int = random.randint(0,len(quotes_list)-1)
    # selected_obj = quotes_list[random_int]
    # return selected_obj
    return random.choice(quotes_list)
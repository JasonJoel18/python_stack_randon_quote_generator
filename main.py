import read_json

if __name__ == '__main__':
    quote = read_json.getQuote()
    print(f'Quote of the day: {quote['quote']}')
    print(f'Author: {quote['author']}')
    print(f'Year: {quote['year']}')
    print(f'Source: {quote['source']}')
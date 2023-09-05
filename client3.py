"""
Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""

import json
import random
import urllib.request

def get_data_point(quote):
    """Produce all the needed values to generate a datapoint."""
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price

def get_ratio(price_a, price_b):
    """Get ratio of price_a and price_b. Return None if price_b is 0."""
    if price_b == 0:
        return None
    return price_a / price_b

def main(api_url, n_requests):
    """Query the price once every n_requests."""
    for _ in range(n_requests):
        quotes = json.loads(urllib.request.urlopen(api_url.format(random.random())).read())
        prices = {}

        for quote in quotes:
            stock, bid_price, ask_price, price = get_data_point(quote)
            prices[stock] = price
            print(f"Quoted {stock} at (bid:{bid_price}, ask:{ask_price}, price:{price})")

        print(f"Ratio {get_ratio(prices['ABC'], prices['DEF'])}")

if __name__ == "__main__":
    API_URL = "http://localhost:8080/query?id={}"
    N_REQUESTS = 500
    main(API_URL, N_REQUESTS)

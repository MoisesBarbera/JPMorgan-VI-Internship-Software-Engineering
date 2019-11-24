import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [

    # Consider if price_bid is smaller than Price_ask
            
        {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            
    # Consider if price_bid is greater than Price_ask
            
        {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 127.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'},
            
    # Consider if price_bid is equal to Price_ask
            
        {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.2, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
        {'top_ask': {'price': 119.2, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 119.2, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        
        # Check quotes
        
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    
    def test_getRatio_calculateRatio(self):
        prices = [
            
    # Consider if price_a is greater than Price_b
            
          {'price_a': 121.2, 'price_b': 120.48}, 
          {'price_a': 121.68, 'price_b': 117.87}, 
            
    # Consider if price_a is bigger than Price_b
            
          {'price_a': 119.2, 'price_b': 120.48}, 
          {'price_a': 121.68, 'price_b': 127.87}, 
            
     # Consider if price_a is equal to Price_b
        
          {'price_a': 121.2, 'price_b': 121.2}, 
          {'price_a': 119.2, 'price_b': 119.2}
        ]
        
        prices_0a = {'price_a': 0.0, 'price_b': 119.2}
            
        prices_0b = {'price_a': 119.2, 'price_b': 0.0} 
            
        prices_equal = {'price_a': 119.2, 'price_b': 119.2}
        
        # Check prices
        
        for price in prices:
            self.assertEqual(getRatio(price['price_a'], price['price_b']), (price['price_a'] / price['price_b'])) 

        # Check prices_0a
        
            self.assertEqual(getRatio(prices_0a['price_a'], prices_0a['price_b']), 0)  # 0 divided by any number equals 0
        # Check prices_0b
        
            self.assertIsNone(getRatio(prices_0b['price_a'], prices_0b['price_b']))    # Anything divide by 0 will generate a ZeroDivision error
        # Check prices_equal
        
            self.assertEqual(getRatio(prices_equal['price_a'], prices_equal['price_b']), 1)   # Any ratio result of dividing some number by itself will always return 0
                             
if __name__ == '__main__':
    unittest.main()

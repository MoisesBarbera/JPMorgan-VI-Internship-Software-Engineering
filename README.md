# JPMorgan-VI-Internship-Software-Engineering
Files produced during my remote VI internship for J.P. Morgan Chase as a Software Engineer 


### client3.py

Quick programme to process the data feed of stock A and stock B’s price to enable us to analyse when trading for the stock should occur.

getDataPoint function returns correct tuple of stock name, bid_price, ask_price and price. "Note: price of a stock = average of bid and ask".

getRatio function returns the ratio of the two stock prices

main function outputs correct stock info, prices and ratio

### client_test.py

Adds tests to the methods in the client application above so that developers are more confident. 
These methods work as expected with different inputs given to them.


### App.tsx and graph.tsx

Here I was tasked with fixing the client-side web application so that it displays a graph that automatically updates as it gets data from the server application.

My graph displayed in the client-side web application is a continuously updating line graph whose y axis is the stock’s top_ask_price and the x-axis is the timestamp of the stock. The continuous updates to the graph are the result of continuous requests and responses to and from the server for the stock data.

It is also able to aggregate duplicated data retrieved from the server.


### Graph3.tsx
Last part of my formal VI internship.

The purpose of this graph is to monitor and determine when a trading opportunity may arise as a result of the temporary weakening of a correlation between two stock prices. Given this graph, the trader should be able to quickly and easily notice when the ratio moves too far from the average historical correlation. After several trials I assumed a threshold of +/-5% of the 12 month historical average ratio.

Playground for SqliteDB with Python

actually, Dataset can be found here with a browser:
https://query2.finance.yahoo.com/v10/finance/quoteSummary/fb?modules=financialData,price,defaultKeyStatistics

Yahoo's older Financial API are no longer accessible yet their Yahoo Finance v10 API works.
https://stackoverflow.com/questions/44030983/yahoo-finance-url-not-working/44348197

This python script which generated this facebook file had data pulled from this site. The problem with this website is that
it required an account to pull historical data and generally not anything recent. One has to pay to pull live uptodate data.
https://www.quandl.com/api/v3/datasets/WIKI/FB.json?start_date=2017-12-01&end_date=2017-12-31&api_key=YOUR_OWN_KEY

Yahoo and a few other sites still support current stock data but not easy to understand their API.
https://query2.finance.yahoo.com/v10/finance/quoteSummary/aapl?formatted=true&lang=en-US&region=US&modules=summaryProfile,financialData,price,defaultkeystatistics

Another website which provided stock data.
https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=FB&interval=weekly&apikey=YOUR_API_KEY

Other possible website to acquire Stock information:
IEX, EOD Historical Data, Intrinio, Quandl, world trading data, Alpha Vantage

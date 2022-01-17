################################
# Download this file for MAC_OSX
# https://www.python.org/ftp/python/3.10.0/python-3.10.0post2-macos11.pkg 
################################

###############################
# install Python Software
###############################

###############################
# Install Certificates
# this is inside the Application folder of Python
# you have to click on a file to install a Cert.
###############################

##############################
# Update pip
/Library/Frameworks/Python.framework/Versions/3.10.0/bin/python3 -m pip install --upgrade pip
##############################

# ***NOTE***
# Python3 and pip3 are both installed in the /usr/local/bin location and not in /usr/bin
# probably not going to create an alias, since it might over write the native MacOS python software which is a bad thing. 

#############################
# install packages
#############################
/Library/Frameworks/Python.framework/Versions/3.10/bin/pip3 install --user wheel 
/Library/Frameworks/Python.framework/Versions/3.10/bin/pip3 install --user scrapy
/Library/Frameworks/Python.framework/Versions/3.10/bin/pip3 install --user pandas_datareader requests ta scipy numpy plotly
/Library/Frameworks/Python.framework/Versions/3.10/bin/pip3 install --user pandas matplotlib seaborn statsmodels QuantLib pyfinlab
/Library/Frameworks/Python.framework/Versions/3.10/bin/pip3 install --user yfinance PyAlgoTrade yahoo_fin 
/Library/Frameworks/Python.framework/Versions/3.10/bin/pip3 install --user Statistics-pyt backtrader scikit-learn pyfin
/Library/Frameworks/Python.framework/Versions/3.10/bin/pip3 install --user arrow prettypandas beautifier tabulate
/Library/Frameworks/Python.framework/Versions/3.10/bin/pip3 install --user keras BeautifulSoup4 pybrain
/Library/Frameworks/Python.framework/Versions/3.10/bin/pip3 install --user pydot pygal

##############################
# SKIP the FOLLOWING
# python3 -m pip install --user SOFTWARE
#/usr/local/bin/pip3 install --user pymc3 scikit-learn yfinance statsmodels zipline pyfolio
#/usr/local/bin/pip3 install --user pyfin vollib quantpy ffn tia pynance mplfinance plotly yahoo_fin 
# /usr/local/bin/pip3 install --user vaderSentiment xlsxwriter xlrd openpyxl
# /usr/local/bin/pip3 install --user quandl tqdm
##############################

#############################
# Creating directories
#############################
mkdir -p ~/finc3114/{labs,hws}
echo "DONE."

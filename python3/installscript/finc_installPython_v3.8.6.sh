# Go to this website to download this file
# Yet 3.8.6 is best
# Download this file for MAC_OSX
# https://www.python.org/ftp/python/3.8.6/python-3.8.6-macosx10.9.pkg

# install the Python Software

# Install Certificates
# this is inside the Application folder of Python, you have to click or something. yes there is.

# Update pip
/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8 -m pip install --upgrade pip

# NOTE
# Python3 and pip3 are both installed in the /usr/local/bin location and not in /usr/bin

# probably not going to create an alias, since it might over write the native MacOS python software which is a bad thing. 

# install packages
/usr/local/bin/pip3 install --user wheel requests ta
/usr/local/bin/pip3 install --user pandas matplotlib seaborn pillow pandas_datareader scipy numpy
/usr/local/bin/pip3 install --user pymc3 scikit-learn yfinance statsmodels zipline pyfolio
/usr/local/bin/pip3 install --user pyfin vollib quantpy ffn tia pynance mplfinance plotly yahoo_fin 
/usr/local/bin/pip3 install --user vaderSentiment xlsxwriter xlrd openpyxl
# /usr/local/bin/pip3 install --user quandl tqdm
# Creating directories
cd
mkdir -p ~/finc3984/{labs,hws}

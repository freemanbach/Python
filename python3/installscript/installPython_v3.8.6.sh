
# Go to this website to download this file
# Yet 3.8.6 is best
# https://www.python.org/ftp/python/3.8.6/python-3.8.6-macosx10.9.pkg
# Or (ONLY IF necessary) still not tested yet
# https://www.python.org/downloads/release/python-389/
# https://www.python.org/ftp/python/3.8.9/python-3.8.9-macosx10.9.pkg

# install the Python Software
# Dont know exactly where this python will install, need to check again.

# Install Certificates
# this is inside the Application folder of Python

# Update pip
/Library/Frameworks/Python.framework/Versions/3.8/bin/python3.8 -m pip install --upgrade pip

# NOTE
# Python3 and pip3 are both installed in the /usr/local/bin location and not in /usr/bin

# probably not going to create an alias, since it might over write the native MacOS python software which is a bad thing. 

# install packages
/usr/local/bin/pip3 install --user wheel 
/usr/local/bin/pip3 install --user requests tqdm pyfin vollib quantpy ffn tia pynance
/usr/local/bin/pip3 install --user pymc3 scipy numpy pandas matplotlib seaborn 
/usr/local/bin/pip3 install --user pillow pandas_datareader scikit-learn yfinance statsmodels quandl zipline pyfolio

# Homebrew is by far the easiest, but the question remained, do Finance majors 
# really need to know IT/CS/Sys_Engineering stuff ?!?!?!
# There is a fine line, i think i am drawing it here.

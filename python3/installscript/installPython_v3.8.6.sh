# Go to this website
# https://www.python.org/ftp/python/3.8.6/python-3.8.6-macosx10.9.pkg

# install the Python Software
# Dont know exactly where this python will install, need to check again.

# Update pip, i hope it is here, not sure.
/usr/bin/python3 -m pip install --upgrade pip

# probably not going to create an alias, since it might over write the
# native MacOS python software which is a bad thing. 

# install packages
~/Library/Python/3.8/bin/pip install --user wheel 
~/Library/Python/3.8/bin/pip install --user requests tqdm pyfin volib quantpy ffn tia pynance
~/Library/Python/3.8/bin/pip install --user pymc3 scipy numpy pandas matplotlib seaborn 
~/Library/Python/3.8/bin/pip install --user pillow pandas_datareader scikit-learn yfinance statsmodels quandl zipline pyfolio

# Homebrew is by far the easiest, but the question remained, do Finance majors 
# really need to know IT/CS/Sys_Engineering stuff ?!?!?!
# There is a fine line, i think i am drawing it here.
# FTPS Upload
Prepared by: Brian Cohn
[![Build Status](https://travis-ci.org/bc/ftpsconnector.svg?branch=master)](https://travis-ci.org/bc/ftpsconnector)
# Installation
```py
pip install ftpsconnector
```

# Installation from GitHub
```bash
git clone git@github.com:bc/ftpsconnector.git && cd ftpsconnector
pip install -r requirements.txt
pip install .
pytest #only for brian's test case
```

# Example usage:

### Bring in dependencies and set up user/pass
```py
from ftpsconnector.helper_functions import connect, tx_with_progress, receive
ftp = connect(user='brian', password='your_password_here')
```
You need to define a file called `password.txt` and include only one line with your password in plaintext. Do not commit this file, use a .gitignore.

You can view files on the server's home folder with `ftp.retrlines('LIST home')`.

### Upload big file
```py
input_filepath = "~/helper_functions.py" #use full path
destination_filepath = "home/brian_scratch/helper_functions_remote.py"
tx_with_progress(ftp, input_filepath, destination_filepath,
                 block_size_bytes=12500000)
```
### Download that file back to local
```py
filepath_pensieve = "home/brian_scratch/helper_functions_remote.py"
filepath_local = "~/Downloads/helper_functions_prime.py" #use full path
receive(ftp, filepath_pensieve, filepath_local,
	block_size_bytes=12500000)
```
### Close out the connection
```py
ftp.quit()
ftp = None
```

# Devnotes
```
python setup.py sdist upload -r pypitest
python setup.py sdist upload -r pypi
```
```
https://test.pypi.org/project/ftpsconnector/0.1/#description
https://pypi.org/manage/projects/
```
Make sure the `~/.pypirc` file has the correct info. See [Link](https://peterdowns.com/posts/first-time-with-pypi.html)

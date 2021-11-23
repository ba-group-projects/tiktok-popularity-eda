# SMM635 MTP
## How to start
1. install packages
```bash
pip install -r requirements.txt # install packages
```
2. run the code in the smm635.ipynb


## The structure of the code
The structure of the code is as follows:
- data
  - cleaned_data.csv
  - trending.json

- utils
  - \_\_init\_\_.py
  - clean.py
- figure(the figure we got)
- smm635.ipynb # main code
- requirements.txt
- README.md

## Known issues
1. google-translator has some environment issues needed to be care about. If the packages in requirements.txt cannot be installed successfully, you may not be able to reproduce the translator functions. But you can directly read the file frome the data folder.(Linux is suggested when using googletrans rather than Mac OS)


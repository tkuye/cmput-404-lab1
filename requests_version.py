import requests
print(requests.__version__)
source = requests.get('https://raw.githubusercontent.com/tkuye/cmput-404-lab1/main/requests_version.py')
print(source.text)

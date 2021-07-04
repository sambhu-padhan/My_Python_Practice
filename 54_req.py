import requests

re = requests.get("http://www.facebook.com")
print(re.text)


url = "www.google.com"
data = {"d1":23,
        "d2":12}
re2 = requests.post(url = url,data = data)

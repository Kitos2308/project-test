

import requests



headers = {
"User-Agent": "fgkjbfgvrbgtrbgv"

}

response = requests.post("https://httpbin.org/post",
                         headers=headers,
                         params={'a':'b', 'c':10})
print(response)

print(response.text)







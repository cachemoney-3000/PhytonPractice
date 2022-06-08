from urllib.parse import urlparse
import re

def domain_name(url):
    return url.split("www.")[-1].split("//")[-1].split(".")[0]

"""def domain_name(url):
    url = urlparse(url).netloc
    print(url)

    domain = ""
    for i in range(0, len(url)):
        if url[i] == '.':
            break

        else:
            domain = domain + url[i]

    return domain"""


print(domain_name("https://www.xakep.ru"))
print(domain_name("www.xakep.ru"))

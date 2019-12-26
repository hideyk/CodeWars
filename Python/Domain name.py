def domain_name(url):
    if "www" in url:
        return url.split("www.")[1].split(".")[0]
    elif "://" in url:
        return url.split("://")[1].split(".")[0]
    else:
        return url.split(".")[0]

def domain_name2(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

url_link = "http://github.com/carbonfive/raygun"
domain = domain_name(url_link)
print(domain)
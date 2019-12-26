def acronomyze(element):
    if len(element) > 30:
        ignored_words = ["the","of","in","from","by","with","and", "or", "for", "to", "at", "a"]
        untouched_words = [i[0].capitalize() for i in element.split("-") if i not in ignored_words]
        return "".join(untouched_words)
    else:
        return " ".join(element.split("-")).upper()


def generate_bc(url, separator):
    front_stuff = ["https://www.", "http://www.", "http://", "https://", "www."]
    for i in front_stuff:
        if i in url:
            url = url.replace(i, "")
    good_url = url.split("/index.")[0].split("?")[0].split("#")[0]

    trailing = good_url.split(".", 1)[1]
    if "/" not in trailing or (trailing.count("/") == 1 and trailing[-1] == "/"):
         return '<span class="active">HOME</span>'

    final_url = '<a href="/">HOME</a>'
    middle_elems = trailing.split("/")[1:-1]
    end_string = trailing.split("/")[-1]

    placeholder = ""
    for elem in middle_elems:
        placeholder += "/" + elem
        final_url += separator
        mid_string = '<a href="' + placeholder + '/">' + acronomyze(elem) + '</a>'
        final_url += mid_string

    end_elem = separator + '<span class="active">' + acronomyze(end_string.split(".")[0]) + '</span>'
    final_url += end_elem
    return final_url



webpage = "http://www.facebook.fr/profiles/wanted#info"
sep = " + "
final_bc = generate_bc(webpage, sep)
print(final_bc)

# https://www.codewars.com/pictures/the-meningitis-pippi-a-bed-surfer-diplomatic/secret-page.php
# https://www.pippi.pi/funny.php
# agcpartners.co.uk/profiles#info
# facebook.fr
# http://www.google.ca/biotechnology-by-eurasian-at-research-with-of-insider-skin/surfer-research-eurasian-at-paper-cauterization/or-surfer-cauterization-paper-in-kamehameha#offers?favourite=code
# http://www.facebook.fr/profiles/wanted#info
# https://www.pippi.pi#offers?rank=recent_first&hide=sol
# http://linkedin.it/index.asp#people?referral=CodeWars
# http://github.com
#
#

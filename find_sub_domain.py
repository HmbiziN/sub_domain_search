import requests

domain = input("domain name : ")
file = open("Subdomain.txt")
report = open("report.txt","w")
sub_domains = file.read().splitlines()
nbr = len(sub_domains)
counter = 0
for sub_domain in sub_domains:
    counter+=1
    if sub_domain.startswith("http://") or sub_domain.startswith("https://"):
        url = f"{sub_domain}.{domain}"
    else:
        url = f"http://{sub_domain}.{domain}"
    try:
        requests.get(url,timeout=10)
    except requests.ConnectionError:
        
        print("[-]", counter,"/",nbr,"sub domain not found",url)
        pass
    else:
        print("[-]", counter,"/",nbr,"sub domain found",url)
        report.write(url + "\n")
file.close()
report.close()
import whois
domain=input("enter domain:")
info =whois.whois(domain)
print(info)

from datetime import datetime

today_date = datetime.now().strftime("%Y-%m-%d")
with open(f"domain_values_2024-04-24.txt", "r") as file:
    lines = file.readlines()

domains = {}
for line in lines:
    parts = line.strip().split(": ")
    domain = parts[0]
    score = float(parts[1])
    domains[domain] = score

sorted_domains = sorted(domains.items(), key=lambda x: x[1])

for domain, score in sorted_domains:
    print(f"{domain}: {score}")

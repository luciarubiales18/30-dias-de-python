it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
print(len(it_companies))
it_companies.add("Twiitter")

it_companies.update(["Instagram", "TikTok", "Telegram"])
print(it_companies)

it_companies.remove("Telegram")
print(it_companies)






A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print(A.union(B))

print(B.intersection(A))
print(A.issubset(B))
print(A.difference(B))
empty_list = list()

more_than_5 = [1, 2, 3, 4, 5, 6]

print(len(more_than_5))

print(more_than_5[0] , more_than_5[len(more_than_5) // 2], more_than_5[-1]) 

mixed_data_types = ["Lucia", "16", "1,76", "casada", "Calle Santa Jesusa Nº6"]

it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

print(it_companies)

print(len(it_companies))

print(it_companies[0], it_companies[1], it_companies [-1])

it_companies[5] = "Stradivarius"
print(it_companies)

it_companies.append("Google")
print(it_companies)

it_companies.insert(4,"Breshka")
print(it_companies)

it_companies[3] = it_companies[3].upper()
print(it_companies)

it_companies_hast = "#" .join(it_companies)
print(it_companies_hast)

print("Stradivarius" in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies [0:3])
print(it_companies[6:9])

print(it_companies)




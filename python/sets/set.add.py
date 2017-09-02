n = int(input())
countries_set = set()

for i in range(n):
    country_name = input()
    countries_set.add(country_name)

print(len(countries_set))

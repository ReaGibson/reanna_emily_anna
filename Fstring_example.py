#Dictionary of the top four countries by population
countries = {"India" : 1450935791, "China" : 1419321278, "United States" : 345426571, "Indonesia" : 283487931}

print(f"{" ": <5s} {"Country":<15s} {"Polulation":<15s} ")

for index, country_name in enumerate(countries.keys(), start=1):
    print(f"{index:<5d} {country_name:<15s} {countries[country_name]:<15,}")






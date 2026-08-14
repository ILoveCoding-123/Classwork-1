country_code = {'Usa' : '001',
'India' : '0091',
 'Argentina' : '0054'}

print("The country of the USA is -")
print(country_code.get('Usa', 'Not Found'))


print("The country code of Canada is -")
print(country_code.get('Canada', 'Not Found'))
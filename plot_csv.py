import csv

with open('cars.csv', 'r') as f:
  reader = csv.DictReader(f)
  your_list = list(reader)

print(your_list[:5])

price_list = []
age_list = []
miles_list = []
ID_list = []

for item in your_list:
    price_list.append(item['Price'])
    age_list.append(item['Age'])
    miles_list.append(item['Miles'])
    ID_list.append(item['ID'])


import matplotlib.pyplot as plt

x = miles_list
y = price_list
colours = age_list
sizes = 1

plt.figure()
plt.scatter(x, y,
         marker = 'o',
         c = colours,
         cmap = 'plasma',
         alpha = 0.5,
         s = 100
        )

plt.xlim(0, 150000)
plt.ylim(0, 15000)

plt.xlabel('Mileage')
plt.ylabel('Price')
plt.title('Mini cooper prices, age and mileage')

#plt.xticks(range(150000))
#plt.yticks(range(5000))

plt.colorbar(orientation = 'horizontal', shrink = 1.0).set_label("Model year")

plt.show()

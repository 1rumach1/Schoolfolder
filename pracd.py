# cars = {
#     "Civic":"red",
#     "Lambo":"green",
#     "UMBW":"pink",
#     "Ferrari":"black",
# }
# for brand in cars:
#     print(brand, cars[brand], sep=", ")

weapons = [
    {"type": "sword", "damage": "strong", "range": "moderate", "element": "fire"},
    {"type": "knife", "damage": "weak", "range": "short", "element": "poison"},
    {"type": "spear", "damage": "moderate", "range": "long", "element": "lightning"},
    {"type": "shield", "damage": "zero", "range": "close", "element": "earth"},
]

for stat in weapons:
    print(f"weapon: {stat['type']}| damage: {stat['damage']}| range: {stat['range']}| element: {stat['element']}")

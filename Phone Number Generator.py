
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num = get_phone(country=44, area=975, first=123, last=456)
print(phone_num)
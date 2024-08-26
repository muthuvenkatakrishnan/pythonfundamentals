def convert_to_1nf(table):
    result = []
    for row in table:
        id = row['id']
        name = row['name']
        phone_numbers = row.get('phone_numbers', [])
        for phone_number in phone_numbers:
            result.append({'id': id, 'name': name, 'phone_number': phone_number})
    return result

table_0nf = [
    {'id': 1, 'name': 'Bill Gate', 'phone_numbers': [12345, 34567, 45678]},
    {'id': 2, 'name': 'Elon Musk', 'phone_numbers': [56782, 78454]}
]

table_1nf = convert_to_1nf(table_0nf)

print('ID'+ " "*8, 'NAME'+" "*8, " "*6+'CONTACT')
for muthu in table_1nf:
    for sasndesh, rakesh in muthu.items():
            print(rakesh, end = " "*10)
    print()
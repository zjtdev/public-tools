import sys

if len(sys.argv) < 2:
    print('Please run this script with cookie')
    exit(1)

cookie_text = sys.argv[1]
print('{:=^50s}'.format('Cookie'))
print(cookie_text)
print('{:=^50s}'.format('Cookie Splited'))
cookie_text_splited = cookie_text.split(';')
for index in range(len(cookie_text_splited)):
    cookie_item = cookie_text_splited[index]
    cookie_splited = cookie_item.split('=', 1)
    cookie_key = cookie_splited[0].strip()
    cookie_value = cookie_splited[1].strip()
    print('{index}: {cookie_key} = {cookie_value}'.format_map(locals()))
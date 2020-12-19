with open('./app.log', 'w', encoding='utf-8') as f:
    f.write('my first file\n')
    f.write('This file\n')
    f.write('contains three lines\n')

with open('./app.log', 'r', encoding='ascii') as f:
    content = f.readlines()
for line in content:
    print(line)

with open('./app.log', 'r', encoding='utf-8') as f:
    content = f.readlines()
for line in content:
    print(line)



csv = open('csv_to_html_res.csv')
lines = csv.readlines()
cells = [[x.replace('\"','').strip() for x in line.split(',')] for line in lines]

#print(cells)
csv.close()

html = open('home.html', 'w')
html.write('''<html>
    <body>
        <table>\n''')

html.write('            <tr>')
for cell in cells[0]:
    html.write(f'<th>{cell}</th>')
html.write('</tr>\n')

for line in cells[1:]:
    html.write('            <tr>')
    for cell in line:
        html.write(f'<td>{cell}</td>')
    html.write('</tr>\n')

html.write('''        </table>
    </body>
</html>
''')
html.close()

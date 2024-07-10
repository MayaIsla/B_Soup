from bs4 import BeautifulSoup

html = """<tbody>
    <table>
  <tbody>
    <tr>
      <td>Lorem ipsum</td>
      <td>Lorem ipsum</td>
      <td>Lorem ipsum</td>
      <td>Lorem ipsum</td>
      <td></td>
      <td>Lorem ipsum</td>
      <td>Lorem ipsum</td>
      <td>Lorem ipsum</td>
      <td>Lorem ipsum</td>
    </tr>
  </tbody>
</table>
    </tbody>"""

b_xmlParse = BeautifulSoup(html, 'lxml')
for tr in b_xmlParse.find_all('tr'):
    data = tr.find_all('td')
    role = data[2].text.split()[0]
    UN = data[2].text.split()[1]
    print(role, UN)
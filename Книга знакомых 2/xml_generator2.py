from add2 import add_telefon as at
from add2 import add_person as ap
from add2 import add_status as ast
from add2 import add_birthday as ab

def create():
    xml = '<xml>\n'
    xml += '    <Telefon: >{}</telefon\n'\
        .format(at())
    xml += '    <Person: >{}</person\n' \
        .format(ap())
    xml += '    <Status: >{}</status\n' \
        .format(ast())
    xml += '    <Birthday: >{}</birthday\n' \
        .format(ab())
    xml += '</xml>'

    with open('data.xml', 'w') as page:
        page.write(xml)

    return xml
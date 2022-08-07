from add2 import add_telefon as at
from add2 import add_person as ap
from add2 import add_status as ast
from add2 import add_birthday as ab
def create():
    style = 'style="font-size:30px;"'
    html = '<html>\n <head></head>\n <body>\n'
    html += '    <p {}>Telefon: {} </p>\n'\
        .format(style, at())
    html += '    <p {}>Person: {} </p>\n' \
        .format(style, ap())
    html += '    <p {}>Status: {} </p>\n' \
        .format(style, ast())
    html += '    <p {}>Birthday: {} </p>\n' \
        .format(style, ab())
    html += '   </body>\n</html>'

    with open('index.html', 'w') as page:
        page.write(html)

    return html
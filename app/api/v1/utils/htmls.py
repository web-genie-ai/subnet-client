from bs4 import BeautifulSoup
from lxml import etree

def is_valid_html(html_code: str):
    try:
        parser = etree.XMLParser(recover=False)
        etree.fromstring(html_code, parser)
        return True
    except etree.XMLSyntaxError as e:
        return False
def seperate_html_css(html_content: str):
    soup = BeautifulSoup(html_content, 'lxml')
    css = ''
    for style_tag in soup.find_all('style'):
        css += style_tag.get_text()
    for style_tag in soup.find_all('style'):
        style_tag.decompose()
    head = soup.head
    if not head:
        head = soup.new_tag('head')
        soup.html.insert(0, head)
    link_tag = soup.new_tag('link', rel='stylesheet', href='styles.css')
    head.append(link_tag)
    cleaned_html = str(soup)
    return cleaned_html, css
def beautify_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    return soup.prettify()
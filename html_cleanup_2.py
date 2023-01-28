from argparse import ArgumentParser
from bs4 import BeautifulSoup

def get_soup(filename):
    with open(filename) as fp:
        return BeautifulSoup(fp, 'html.parser')
    
def delete_elements(soup, *tag_names):
    for tag_name in tag_names:
        for elt in soup.find_all(tag_name):
            elt.extract()

def has_class(tag):
    return tag.has_attr('class')

def is_empty(tag):
    if tag.string:
        return len(tag.string.strip()) == 0
    return False

def delete_empty_tags(soup):
    for tag in soup.find_all(is_empty):
        tag.extract()

def write_soup(soup, dest_file_name):
    pretty = soup.prettify(formatter='html5')
    with open(dest_file_name, mode='w') as fp:
        fp.write(pretty)

def setup_args():
    parser = ArgumentParser()
    parser.add_argument('input')
    parser.add_argument('-o', '--output', help='name of the output file')
    parser.add_argument('--rewrite', help='rewrite input file',
                        action='store_true')
    return parser.parse_args()

def main():
    args = setup_args()
    input_ = args.input
    
    if not args.rewrite and args.output:
        print('You cannot rewrite the file and '
              'write the result to another file. Aborting.')
        return 1
    else:
        rewrite = args.rewrite
        output = args.output if args.output else input_

    soup = get_soup(input_)

    delete_elements(soup, 'script', 'style', 'link', 'meta', 'img', 'section',
                          'header', 'footer')

    # delete the class attribute from all elements
    for tag in all_elements_with_class_attr:
        del tag['class']

    # delete all the empty attributes
    delete_empty_tags(soup)

    write_soup(output)


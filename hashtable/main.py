import operator

from hashtable_api import StringHashTable, GuidHashTable, ImageHashTable

def chomped_lines(it):
    return map(operator.methodcaller('rstrip', '\r\n'), it)

def main():

    # Hashtable for strings.txt
    strings = StringHashTable()

    with open('strings.txt', 'r') as file:
        for line in chomped_lines(file):
            strings.set(line.lower(), line)

    print('String hash table:')
    strings.debug_print()
    print('\nString lookups:')
    print(strings.get('indian meal moth'))
    print(strings.get('orb-weaving spiders (banded garden spider)'))

    guids = GuidHashTable()
    with open('guids.txt', 'r') as file:
        for line in chomped_lines(file):
            guids.set(line.lower(), line)

    print('\nGuid hash table:')
    guids.debug_print()
    print('\nGuid lookups:')
    print(guids.get('00000158691797bd77464883000a001800388ccf'))
    print(guids.get('00000158691797bd7746488c000a001991ef0003'))

    images = ImageHashTable()

    with open('images.txt', 'r') as file:
        for line in chomped_lines(file):
            images.set(line, line)

    print('\nImage hash table:')
    images.debug_print()
    print('\nImage lookups:')
    print(images.get('document.png'))
    print(images.get('security_keyandlock.png'))


if __name__ == '__main__':
    main()

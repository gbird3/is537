import inspect


################################################
###   Serialization to JSON

TAB = '\t'

def json_encode(st):
    return st.replace('\\', '\\\\').replace('"', '\\"')

def to_json(obj, level=0):
    '''Serializes the given object to JSON, printing to the console as it goes.'''
    d = obj.__dict__
    tab = TAB * level
    result = []
    for key in sorted(d.keys()):
        value = d[key]

        if isinstance(value, bool):
            result.append('\n\t{}"{}": {}'.format(tab, json_encode(key), 'true' if value else 'false'))
        elif isinstance(value, int):
            result.append('\n\t{}"{}": {}'.format(tab, json_encode(key), value))
        elif isinstance(value, float):
            result.append('\n\t{}"{}": {}'.format(tab, json_encode(key), value))
        elif isinstance(value, str):
            result.append('\n\t{}"{}": "{}"'.format(tab, json_encode(key), json_encode(value)))
        elif value is None:
            result.append('\n\t{}"{}": null'.format(tab, json_encode(key)))
        else:
            result.append('\n\t{}"{}": {}'.format(tab, json_encode(key), to_json(value, level+1)))

    return '{' + ','.join(result) + '\n' + tab + '}'

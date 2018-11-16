# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513180785.0295758
_enable_loop = True
_template_filename = '/Users/gregbird/school/is537/ColorShift/homepage/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        color_tiles = context.get('color_tiles', UNDEFINED)
        color_tiles2 = context.get('color_tiles2', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n<html>\n    <meta charset="UTF-8">\n    <head>\n\n        <title>homepage</title>\n        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/jquery-3.2.1.min.js"></script>\n        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/popper.js"></script>\n        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/tooltip.js"></script>\n        <script src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap.min.js"></script>\n        <link rel="stylesheet" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('homepage/media/bootstrap.min.css">\n\n')
        __M_writer('        <script src="/django_mako_plus/dmp-common.min.js"></script>\n        ')
        __M_writer(str( django_mako_plus.links(self) ))
        __M_writer('\n\n    </head>\n    <body>\n        <header>\n            <h1>Color Shift<h1>\n        </header>\n        <main>\n            <div>\n                <form id="form" method="POST" class="form-inline">\n                    ')
        __M_writer(str( form ))
        __M_writer('\n                    <button id="submit_button" type="submit" class="btn btn-primary">Submit</button>\n                </form>\n            </div>\n            \n            <h2>Unsorted</h2>\n            <div id="color_tile_container">\n')
        for i, tile in enumerate(color_tiles):
            if i % 7 == 0:
                __M_writer('                        <br/>\n')
            __M_writer('                    ')
            __M_writer(str( tile.render() ))
            __M_writer('\n')
        __M_writer('            </div>\n\n            <h2>Sorted</h2>\n            <div id="color_tile_container">\n')
        for i, tile in enumerate(color_tiles2):
            if i % 7 == 0:
                __M_writer('                        <br/>\n')
            __M_writer('                    ')
            __M_writer(str( tile.render() ))
            __M_writer('\n')
        __M_writer('            </div>\n\n        </main>\n    </body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/gregbird/school/is537/ColorShift/homepage/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"17": 0, "28": 2, "29": 8, "30": 8, "31": 9, "32": 9, "33": 10, "34": 10, "35": 11, "36": 11, "37": 12, "38": 12, "39": 15, "40": 16, "41": 16, "42": 26, "43": 26, "44": 33, "45": 34, "46": 35, "47": 37, "48": 37, "49": 37, "50": 39, "51": 43, "52": 44, "53": 45, "54": 47, "55": 47, "56": 47, "57": 49, "63": 57}}
__M_END_METADATA
"""

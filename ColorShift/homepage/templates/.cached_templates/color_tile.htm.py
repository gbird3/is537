# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1513180792.650673
_enable_loop = True
_template_filename = '/Users/gregbird/school/is537/ColorShift/homepage/templates/color_tile.htm'
_template_uri = 'color_tile.htm'
_source_encoding = 'utf-8'
import django_mako_plus
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        tile = context.get('tile', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('<div class="color_tile">\n    <div class="color_circle" style="background-color: #')
        __M_writer(str( tile.color ))
        __M_writer('"></div>\n    <div class="color_text">')
        __M_writer(str( tile.title ))
        __M_writer('</div>\n    <div class="color_text">#')
        __M_writer(str( tile.color ))
        __M_writer('</div>\n    <div class="color_text">')
        __M_writer(str( tile.luma ))
        __M_writer('</div>\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/gregbird/school/is537/ColorShift/homepage/templates/color_tile.htm", "uri": "color_tile.htm", "source_encoding": "utf-8", "line_map": {"17": 0, "23": 2, "24": 3, "25": 3, "26": 4, "27": 4, "28": 5, "29": 5, "30": 6, "31": 6, "37": 31}}
__M_END_METADATA
"""

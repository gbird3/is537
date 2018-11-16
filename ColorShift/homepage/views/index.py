from django.conf import settings
from django import forms
from django_mako_plus import view_function, jscontext

# see the /homepage/lib/ directory for the following
from ..lib.widgets import ColorTile
from ..lib.num_bases import hex_to_num, num_to_hex
from ..lib.color_sort import luma_sort
from ..lib.color_utils import separate_rgb, combine_rgb, adjust_color, calc_luma


OPERATIONS = [
      # title             Red   Green Blue
    [ 'Original',         0,    0,    0    ],
    [ 'Less Red - 10%',   -0.1, 0,    0    ],
    [ 'More Red - 10%',   0.1,  0,    0    ],
    [ 'Less Green - 10%', 0,    -0.1, 0    ],
    [ 'More Green - 10%', 0,    0.1,  0    ],
    [ 'Less Blue - 10%',  0,    0,    -0.1 ],
    [ 'More Blue - 10%',  0,    0,    0.1  ],
    [ 'Original',         0,    0,    0    ],
    [ 'Less Red - 30%',   -0.3, 0,    0    ],
    [ 'More Red - 30%',   0.3,  0,    0    ],
    [ 'Less Green - 30%', 0,    -0.3, 0    ],
    [ 'More Green - 30%', 0,    0.3,  0    ],
    [ 'Less Blue - 30%',  0,    0,    -0.3 ],
    [ 'More Blue - 30%',  0,    0,    0.3  ],
    [ 'Original',         0,    0,    0    ],
    [ 'Less Red - 50%',   -0.5, 0,    0    ],
    [ 'More Red - 50%',   0.5,  0,    0    ],
    [ 'Less Green - 50%', 0,    -0.5, 0    ],
    [ 'More Green - 50%', 0,    0.5,  0    ],
    [ 'Less Blue - 50%',  0,    0,    -0.5 ],
    [ 'More Blue - 50%',  0,    0,    0.5  ],
    [ 'Original',         0,    0,    0    ],
    [ 'Darker - 10%',     -0.1, -0.1, -0.1 ],
    [ 'Lighter - 10%',     0.1,  0.1,  0.1 ],
    [ 'Darker - 30%',     -0.3, -0.3, -0.3 ],
    [ 'Lighter - 30%',     0.3,  0.3,  0.3 ],
    [ 'Darker - 50%',     -0.5, -0.5, -0.5 ],
    [ 'Lighter - 50%',     0.5,  0.5,  0.5 ],
]


@view_function
def process_request(request):
    '''Main view function'''
    color_tiles = []
    
    # process the form
    form = ColorForm()
    if request.method == 'POST':
        form = ColorForm(request.POST)
        if form.is_valid():
            # get the color as an integer and split RGB integers
            source = hex_to_num(form.cleaned_data.get('source_color'))
            red, green, blue = separate_rgb(source)
            
            # create a tile for each operation
            for title, red_perc, green_perc, blue_perc in OPERATIONS:
                # adjust the color to a new integer
                color_num = combine_rgb(
                    adjust_color(red, red_perc),
                    adjust_color(green, green_perc),
                    adjust_color(blue, blue_perc),
                )
                # add a tile for this adjusted color
                # see /homepage/lib/widgets.py for the ColorTile class
                color_tiles.append(ColorTile( 
                    title, 
                    calc_luma(color_num),
                    num_to_hex(color_num)
                ))
    
    # create color_tiles2 by sorting color_tiles on the luma value
    color_tiles2 = luma_sort(color_tiles)
    
    # render the template
    context = {
        'form': form,
        'color_tiles': color_tiles,
        'color_tiles2': color_tiles2,
    }
    return request.dmp_render('index.html', context)
    
    
    
class ColorForm(forms.Form):
    '''The color form to process'''
    source_color = forms.CharField(label='Enter a color in hex format', widget=forms.TextInput(attrs={ 'placeholder': '112233', 'class': 'form-control' }))


 
"""
PyCatcher defalut configuration file

Define configuration variables that need to be different from defaults here to override them.
"""

config = {
	
	# Path to define where to save images. Relative to where the script is run.
	# 'filename_path' : 'images/',

	# Filenames are saved as prefix%n.png where %n is the number in the sequence.
	# 'filename_prefix' : 'img-',

	# Delay in seconds between each shot
	#'delay' : 60,

	# List of filters to apply to the image
	'filters' : ['webcam'],

    # Overridable filter specific config
    'filters_config' :
       {
         'webcam' : {
           #'width' : 100,
           #'height' : 100
           #'coordinates' : (10,10),
           #'border_colour' : "#fff"
         }
    }
    
}

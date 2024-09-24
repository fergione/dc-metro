from adafruit_bitmap_font import bitmap_font

config = {
	#########################
	# Network Configuration #
	#########################

	# WIFI Network SSID
	'wifi_ssid': 'Based Bussin Boomers',

	# WIFI Password
	'wifi_password': 'doe6-reedy-hut',

	#########################
	# Metro Configuration   #
	#########################

	# Metro Station Code
	'metro_station_code': 'F05',
	'metro_station_code_secondary': 'D05',

	# Metro Train Groups
    # If you only want 1 group to show up, use that code for both train_group_1 and train_group_2
	'train_group_1': '1',
    'train_group_2': '2',

	# API Key for WMATA
	'metro_api_key': 'ce2cd5cd5d0b4ccfb6203f7c25f93e2d',

	#########################
	# Other Values You      #
	# Probably Shouldn't    #
	# Touch                 #
	#########################
	'metro_api_url': 'https://api.wmata.com/StationPrediction.svc/json/GetPrediction/',
	'metro_api_retries': 5,
	'refresh_interval': 5, # 5 seconds is a good middle ground for updates, as the processor takes its sweet ol time
	
	# Display Settings
	'matrix_width': 64,
	'num_trains': 3,
	'font': bitmap_font.load_font('lib/5x7.bdf'),

	'character_width': 5,
	'character_height': 7,
	'text_padding': 1,
	'text_color': 0xFF7500,

	'loading_destination_text': 'Loading',
	'loading_min_text': '---',
	'loading_line_color': 0xFF00FF, # Something something Purple Line joke

	'heading_text': 'LN DEST   MIN',
	'heading_color': 0xFF0000,

	'train_line_height': 6,
	'train_line_width': 2,

	'min_label_characters': 3,
	'destination_max_characters': 8,
}

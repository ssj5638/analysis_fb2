import os


CONFIG = {
    'items': [{'pagename': 'jtbcnews', 'since': '2017-01-01', 'until': '2017-12-31'},
             {'pagename': 'chosun', 'since': '2017-01-01', 'until': '2017-12-31'}],
    'result_directory_v': '__results__/visualization',
    'common':{
        'base_url':'https://graph.facebook.com/v3.0',
        'access_token': "EAACEdEose0cBAIQaAPd002gPHZAK7ZCxQcIipfSeUjxN4IA5WpZAz08JWwfB9klILRT14kfydHvjCPsh2b0Dk13qDCv1CmsRnl6Y7b0jZAzGs3QZA3lAUYZBYo56s3vBR6UfQFpHreH18oGFxZAA9AJsi5ZBrEZBhp10WXGnM8ec0ZCJySjT1MKaztJZBSJiWonZCzAZD",
        'fetch':False,
        'result_directory_c': '__results__/crawling'
    }
}

if os.path.exists(CONFIG['common']['result_directory_c']) is False:
    os.makedirs(CONFIG['common']['result_directory_c'])


if os.path.exists(CONFIG['result_directory_v']) is False:
    os.mkdir(CONFIG['result_directory_v'])
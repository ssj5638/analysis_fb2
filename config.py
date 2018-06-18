import os


CONFIG = {
    'items': [{'pagename': 'jtbcnews', 'since': '2017-01-01', 'until': '2017-12-31'},
             {'pagename': 'chosun', 'since': '2017-01-01', 'until': '2017-12-31'}],
    'result_directory_v': '__results__/visualization',
    'common':{
        'base_url':'https://graph.facebook.com/v3.0',
        'access_token': "EAACEdEose0cBAH2TpS3buZAlHBfW47PCIKYmZAqL1SLWmGsfC29dAT61I50jPPV2G4mqwzBDTHM84ZBo3yeeAQIAEuf8OojhZAkrzINzoo4g8JHaPyMMRhBR7zaZBC5Eg5R18bsqd7QwzKRBzDuMXBWNuRjxZCdxAvsraLlT2lAZCQEdC4YqpJV5ExTYipvzf4ZD",
        'fetch':True,
        'result_directory_c': '__results__/crawling'
    }
}

if os.path.exists(CONFIG['common']['result_directory_c']) is False:
    os.makedirs(CONFIG['common']['result_directory_c'])


if os.path.exists(CONFIG['result_directory_v']) is False:
    os.mkdir(CONFIG['result_directory_v'])
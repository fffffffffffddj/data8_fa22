OK_FORMAT = True
test = {   'name': 'q3_3',
    'points': [0, 0, 0, 0, 0],
    'suites': [   {   'cases': [   {'code': '>>> type(null_statement_number) == int\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> type(alternative_statement_number) == int\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> any(null_statement_number == x for x in np.arange(1,7))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> any(alternative_statement_number == x for x in np.arange(1,7))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> null_statement_number != alternative_statement_number\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}

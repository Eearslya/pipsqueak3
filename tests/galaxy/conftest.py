"""
galaxy/conftest.py - Testing fixtures for the Galaxy module.

Copyright (c) 2018 The Fuel Rats Mischief,
All rights reserved.

Licensed under the BSD 3-Clause License.

See LICENSE.
"""

import re
import pytest
from aioresponses import aioresponses

from Modules.galaxy import Galaxy


@pytest.fixture()
def mock_system_api_server_fx():
    """
    Returns a mock HTTP server with pre-built data resembling the Fuel Rats Systems API.
    """

    with aioresponses() as api:
        # System Data
        # - Fuelum
        api.get('http://mock.api/api/systems'
                '?filter[name:eq]=FUELUM',
                payload={
                    'data': [
                        {
                            'id': '1464',
                            'attributes': {
                                'name': 'FUELUM',
                                'id64': 5031721931482,
                                'coords': {'x': 52, 'y': -52.65625, 'z': 49.8125}
                            }
                        }
                    ],
                    'meta': {'results': {'available': 1}}
                })

        # - Beagle Point
        api.get('http://mock.api/api/systems'
                '?filter[name:eq]=BEAGLE+POINT',
                payload={
                    'data': [
                        {
                            'id': '124406',
                            'attributes': {
                                'name': 'BEAGLE POINT',
                                'id64': 81973396946,
                                'coords': {'x': -1111.5625, 'y': -134.21875, 'z': 65269.75}
                            }
                        }
                    ],
                    'meta': {'results': {'available': 1}}
                })

        # - EORLD PRI QI-Z D1-4302
        api.get('http://mock.api/api/systems'
                '?filter[name:eq]=EORLD+PRI+QI-Z+D1-4302',
                payload={
                    'data': [
                        {
                            'id': '10189923',
                            'attributes': {
                                'name': 'EORLD PRI QI-Z D1-4302',
                                'id64': 147826004709651,
                                'coords': {'x': -320, 'y': -49.46875, 'z': 19636.6875}
                            }
                        }
                    ],
                    'meta': {'results': {'available': 1}}
                })

        # - PRAE FLYI RO-I B29-113
        api.get('http://mock.api/api/systems'
                '?filter[name:eq]=PRAE+FLYI+RO-I+B29-113',
                payload={
                    'data': [
                        {
                            'id': '14576787',
                            'attributes': {
                                'name': 'PRAE FLYI RO-I B29-113',
                                'id64': 249152528933625,
                                'coords': {'x': -586.125, 'y': -112.0625, 'z': 39248.5}
                            }
                        }
                    ],
                    'meta': {'results': {'available': 1}}
                })

        # - CHUA EOHN CT-F D12-2
        api.get('http://mock.api/api/systems'
                '?filter[name:eq]=CHUA+EOHN+CT-F+D12-2',
                payload={
                    'data': [
                        {
                            'id': '11814429',
                            'attributes': {
                                'name': 'CHUA EOHN CT-F D12-2',
                                'id64': 78995497067,
                                'coords': {'x': -995.5, 'y': -162.59375, 'z': 58857}
                            }
                        }
                    ],
                    'meta': {'results': {'available': 1}}
                })

        # - ANGRBONII
        api.get('http://mock.api/api/systems'
                '?filter[name:eq]=ANGRBONII',
                payload={
                    'data': [
                        {
                            'id': '6337',
                            'attributes': {
                                'name': 'ANGRBONII',
                                'id64': 40557912804216,
                                'coords': {'x': 61.65625, 'y': -42.4375, 'z': 53.59375}
                            }
                        }
                    ],
                    'meta': {'results': {'available': 1}}
                })

        # - Fallthrough for failed searches
        api.get(re.compile(r"http://mock\.api/api/systems.*"),
                payload={
                    'data': [],
                    'meta': {'results': {'available': 0}}
                })

        # Star Data
        # - Fuelum
        api.get('http://mock.api/api/stars'
                '?filter[systemId64:eq]=5031721931482&filter[isMainStar:eq]=1',
                payload={
                    'data': [
                        {
                            'id': '3206960',
                            'attributes': {
                                'id64': 36033828740895450,
                                'name': 'Fuelum',
                                'subType': 'K (Yellow-Orange} Star',
                                'isMainStar': True
                            }
                        }
                    ],
                    'meta': {'results': {'available': 1}}
                })

        # - Fallthrough for failed searches
        api.get(re.compile(r"http://mock\.api/api/stars.*"),
                payload={
                    'data': [],
                    'meta': {'results': {'available': 0}}
                })

        # Fuzzy Searches
        # - Fualun
        api.get('http://mock.api/search'
                '?name=FUALUN&type=dmeta&limit=5',
                payload={
                    'data': [
                        {'name': 'FOLNA'},
                        {'name': 'FEI LIN'},
                        {'name': 'FEI LIAN'}
                    ]
                })

        # - Fallthrough for failed searches
        api.get(re.compile(r"http://mock\.api/search.*"),
                payload={
                    'data': []
                })

        # Nearest Star Systems
        # - Fuelum to Beagle Point Waypoint 1
        api.get('http://mock.api/nearest'
                '?x=-297.61975614106245&y=-77.16362400032693&z=19646.678714135756&aggressive=1&limit=10&cubesize=50',
                payload={
                    'data': [{'name': 'EORLD PRI QI-Z D1-4302'}]
                })

        # - Fuelum to Beagle Point Waypoint 2
        api.get('http://mock.api/nearest'
                '?x=-659.9347713269128&y=-85.86445074372631&z=39233.70563297652'
                '&aggressive=1&limit=10&cubesize=50',
                payload={
                    'data': [{'name': 'PRAE FLYI RO-I B29-113'}]
                })

        # - Fuelum to Beagle Point Waypoint 3
        api.get('http://mock.api/nearest'
                '?x=-981.8197621017766&y=-128.7478566272249&z=58844.498245920506'
                '&aggressive=1&limit=10&cubesize=50',
                payload={
                    'data': [{'name': 'CHUA EOHN CT-F D12-2'}]
                })

        # - Fallthrough for failed searches
        api.get(re.compile(r"http://mock\.api/nearest.*"),
                payload={
                    'data': []
                })

        # Fallthrough request to ensure everything stays contained
        api.get(re.compile(r".*"), status=404)

        yield api


@pytest.fixture()
def galaxy_fx(mock_system_api_server_fx) -> Galaxy: # pylint: disable=redefined-outer-name,unused-argument
    """
    Test fixture for Galaxy. Includes a mock API server with pre-made calls.
    """

    return Galaxy('http://mock.api/')

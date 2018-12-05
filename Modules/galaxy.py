"""
galaxy.py - Star system and celestial body lookups

Provides functionality to search for star systems and retrieve
related information.

Copyright (c) 2018 The Fuel Rat Mischief,
All rights reserved.

Licensed under the BSD 3-Clause License.

See LICENSE.md
"""

import aiohttp
import json

from typing import Dict
from html import escape

from utils.ratlib import Singleton

from logging import getLogger
log = getLogger(f"mecha.{__name__}")


class Galaxy(Singleton):
    """
    A set of helper methods to communicate with the EDDB Systems API.
    """

    def __init__(self):
        self._api_handler = GalaxyAPIHandler()

    async def find_system_by_name(self, name: str):
        data = await self._api_handler.call("systems", {"filter[name:like]": name.upper()})
        return data['data'][0]['attributes']

class GalaxyAPIHandler(Singleton):
    """
    Handle the actual HTTP connections between us and the EDDB API.
    """

    async def call(self, endpoint: str, params: Dict[str, str]):
        """
        Build an HTTP URL to the specified endpoint with included params.
        Returns a JSON data object containing the response.

        Args:
            endpoint (str): The API endpoint to query.
            params (Dict[str, str]): A dictionary of HTTP key/value parameters to include in the URI.
        """
        base_url = "http://system.api.fuelrats.com/"
        param_string = "?"
        if len(params) > 0:
            for k, v in params.items():
                param_string += f"{k}={escape(v)}"
        url = f"{base_url}{endpoint}{param_string}"
        log.info(f"Making HTTP GET request to {url}")
        body = await(self._get(url))
        data = json.loads(body)
        log.debug(body)
        return data

    async def _get(self, uri):
        session = aiohttp.ClientSession()
        async with session.get(uri) as response:
            return await response.text()

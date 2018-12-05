"""
test_galaxy.py - tests the Galaxy API handler

Copyright (c) 2018 The Fuel Rats Mischief,
All rights reserved.

Licensed under the BSD 3-Clause License.

See LICENSE.md
"""

from logging import getLogger
log = getLogger(f"mecha.{__name__}")

import pytest

from tests.mock_callables import AsyncCallableMock
from Modules.galaxy import Galaxy

pytestmark = pytest.mark.galaxy


@pytest.mark.asyncio
async def test_find_system_by_name(galaxy_fx, monkeypatch, async_callable_fx):
    """
    Assert that we can find a system by its name and retrieve relevant information.
    """
    async_callable_fx.return_value = """
{"data": [{"id": "4878", "type": "systems", "attributes": {"edsm_id": 1464, "name": "FUELUM", "x": 52.0, "y": -52.65625, "z": 49.8125, "population": 47775720, "is_populated": 1, "government_id": 80, "government": "Cooperative", "allegiance_id": 4, "allegiance": "Independent", "state_id": 16, "state": "Boom", "security_id": 48, "security": "High", "primary_economy_id": 4, "primary_economy": "Industrial", "power": "Zemina Torval", "power_state": "Exploited", "power_state_id": 32, "needs_permit": 0, "updated_at": 1505178741, "simbad_ref": "HIP 108162", "controlling_minor_faction_id": 7483, "controlling_minor_faction": "The Fuel Rats Mischief", "reserve_type_id": 3, "reserve_type": "Common"}, "links": {"self": "https://system.api.fuelrats.com/systems/4878"}, "related": {}, "relationships": {"bodies": {"data": [{"type": "bodies", "id": "999"}, {"type": "bodies", "id": "3274797"}, {"type": "bodies", "id": "3274953"}, {"type": "bodies", "id": "7400395"}, {"type": "bodies", "id": "7401135"}, {"type": "bodies", "id": "7401219"}, {"type": "bodies", "id": "7401611"}, {"type": "bodies", "id": "7401851"}, {"type": "bodies", "id": "7402039"}], "links": {"self": "https://system.api.fuelrats.com/systems/4878/relationships/bodies", "related": "https://system.api.fuelrats.com/systems/4878/bodies"}, "meta": {"direction": "ONETOMANY", "results": {"limit": 10, "available": 9, "returned": 9}}}}, "meta": {}}], "included": [], "links": {"first": "https://system.api.fuelrats.com/systems?sort=id&filter%5Bname%3Alike%5D=FUELUM&page%5Boffset%5D=0", "last": "https://system.api.fuelrats.com/systems?sort=id&filter%5Bname%3Alike%5D=FUELUM&page%5Boffset%5D=0", "self": "https://system.api.fuelrats.com/systems?filter[name:like]=FUELUM"}, "meta": {"results": {"available": 1, "limit": 10, "offset": 0, "returned": 1}}}"""
    monkeypatch.setattr(galaxy_fx._api_handler, '_get', async_callable_fx)

    system = await galaxy_fx.find_system_by_name("Fuelum")

    assert system['name'] == "FUELUM"


def test_singletion():
    """
    Verifies galaxy acts as a singleton
    """
    alpha = Galaxy()
    beta = Galaxy()
    assert alpha is beta

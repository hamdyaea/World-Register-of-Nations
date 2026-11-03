#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
# SPDX-License-Identifier: GPL-3.0-or-later
"""Offline REST Countries parser and Tkinter model tests."""
from unittest.mock import Mock, patch
import pytest

from World_Register_GUI import Country, parse_countries, fetch_countries


SAMPLE = [
    {"name": {"common": "Switzerland"}, "cca2": "CH", "capital": ["Bern"],
     "region": "Europe", "subregion": "Western Europe", "population": 9000000,
     "area": 41285, "languages": {"deu": "German", "fra": "French"},
     "currencies": {"CHF": {"name": "Swiss franc"}}, "borders": ["DEU", "FRA"]},
    {"name": {"common": "France"}, "cca2": "FR", "capital": ["Paris"],
     "region": "Europe", "population": 68000000, "area": 551695},
]


def test_country_parsing():
    countries = parse_countries(SAMPLE)
    assert [c.name for c in countries] == ["France", "Switzerland"]
    swiss = countries[1]
    assert swiss.code == "CH"
    assert swiss.capital == "Bern"
    assert swiss.languages == ("French", "German")
    assert swiss.currencies == ("CHF",)
    assert "9,000,000" in swiss.describe()


def test_invalid_payload():
    for value in ({}, [], "invalid"):
        with pytest.raises(ValueError):
            parse_countries(value)


def test_network_is_mocked():
    response = Mock()
    response.content = b"[]"
    response.json.return_value = SAMPLE
    with patch("World_Register_GUI.requests.get", return_value=response) as getter:
        assert len(fetch_countries()) == 2
    assert getter.call_args.kwargs["timeout"] == 15


def test_reject_oversized_payload():
    response = Mock()
    response.content = b"x" * 5_000_001
    with patch("World_Register_GUI.requests.get", return_value=response):
        with pytest.raises(ValueError, match="5 MB"):
            fetch_countries()

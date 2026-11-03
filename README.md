# World Register of Nations — Python Desktop Browser

Developer: Hamdy Abou El Anein
Contact: hamdy.aea@protonmail.com
Application license: GNU GPL v3 (see LICENSE).

A modern Tkinter country browser showing country names, capitals,
populations, areas, languages, currencies and bordering countries.

The original 880-line EasyGUI program depended on the retired
`restcountries.eu` API, downloaded SVGs to the current directory,
deleted existing images and invoked ImageMagick through `os.system`.
The new version has no shell execution and never overwrites images.

## Install and run

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python World_Register_GUI.py
```

The application fetches a country-data snapshot only when opened or
when Refresh is selected, with a 15-second timeout. It displays 250
country entries in the currently available source.

## Data attribution

Country information is retrieved from the open dataset
[world countries](https://github.com/mledoze/countries) maintained by
mledoze and contributors, under the **Open Database License (ODbL)**.
The database is **not included in this repository** and is not
relicensed under the application's GPL. See the upstream data source
for provenance, updates and ODbL obligations. Values may be historical
or incomplete; they are not guaranteed to be real-time statistics.

The historical Trading Economics GDP lookup has been omitted because
its guest endpoint is not a dependable free public data source.

## Tests

```sh
python3 -m pytest -q
```

Four offline parser tests passed, the GUI opened on Manjaro, and a
live read-only request retrieved 250 countries including Switzerland.

The original implementation is preserved on branch `old`.

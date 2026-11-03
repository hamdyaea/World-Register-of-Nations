#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
# SPDX-License-Identifier: GPL-3.0-or-later
"""World Register of Nations: Tkinter browser for ODbL open country data."""
from __future__ import annotations

from dataclasses import dataclass
import threading
import tkinter as tk
from tkinter import ttk

import requests

API_URL = "https://raw.githubusercontent.com/mledoze/countries/master/countries.json"
MAX_RESPONSE_BYTES = 5_000_000


@dataclass(frozen=True)
class Country:
    name: str
    code: str
    capital: str
    region: str
    subregion: str
    population: int
    area: float
    languages: tuple[str, ...]
    currencies: tuple[str, ...]
    borders: tuple[str, ...]

    @property
    def flag(self) -> str:
        if len(self.code) != 2 or not self.code.isalpha():
            return ""
        return "".join(chr(0x1F1E6 + ord(letter) - ord("A")) for letter in self.code.upper())

    def describe(self) -> str:
        return "\n".join([
            f"{self.flag}  {self.name} ({self.code})",
            f"Capital: {self.capital}",
            f"Region: {self.region} / {self.subregion}",
            f"Population: {self.population:,}",
            f"Area: {self.area:,.2f} km²",
            f"Languages: {', '.join(self.languages) or 'Not available'}",
            f"Currencies: {', '.join(self.currencies) or 'Not available'}",
            f"Bordering countries (codes): {', '.join(self.borders) or 'None'}",
        ])


def parse_countries(payload: object) -> list[Country]:
    if not isinstance(payload, list):
        raise ValueError("REST Countries response must be a list.")
    countries = []
    for row in payload:
        if not isinstance(row, dict) or not isinstance(row.get("name"), dict):
            continue
        name = row["name"].get("common")
        code = row.get("cca2")
        if not isinstance(name, str) or not isinstance(code, str):
            continue
        capitals = row.get("capital") or []
        languages = row.get("languages") or {}
        currencies = row.get("currencies") or {}
        countries.append(Country(
            name=name,
            code=code,
            capital=", ".join(str(x) for x in capitals) if isinstance(capitals, list) else "Unknown",
            region=str(row.get("region") or "Unknown"),
            subregion=str(row.get("subregion") or "Unknown"),
            population=int(row.get("population") or 0),
            area=float(row.get("area") or 0),
            languages=tuple(sorted(str(x) for x in languages.values())) if isinstance(languages, dict) else (),
            currencies=tuple(sorted(str(x) for x in currencies)) if isinstance(currencies, dict) else (),
            borders=tuple(str(x) for x in (row.get("borders") or [])),
        ))
    if not countries:
        raise ValueError("No usable countries in the API response.")
    return sorted(countries, key=lambda country: country.name.casefold())


def fetch_countries() -> list[Country]:
    response = requests.get(API_URL, timeout=15)
    response.raise_for_status()
    if len(response.content) > MAX_RESPONSE_BYTES:
        raise ValueError("Country data exceeds the 5 MB limit.")
    return parse_countries(response.json())


class CountriesWindow(tk.Tk):
    def __init__(self, autoload: bool = True):
        super().__init__()
        self.title("World Register of Nations")
        self.geometry("940x640")
        self.minsize(700, 450)
        self.countries: list[Country] = []
        self.filtered: list[Country] = []
        self._build()
        if autoload:
            self.after(100, self.refresh)

    def _build(self):
        outer = ttk.Frame(self, padding=18)
        outer.pack(fill="both", expand=True)
        ttk.Label(outer, text="World Register of Nations",
                  font=("Sans", 21, "bold")).pack(anchor="w")
        ttk.Label(outer, text="Explore countries, capitals, populations, languages and borders.").pack(
            anchor="w", pady=(4, 12)
        )
        self.query = tk.StringVar()
        search = ttk.Entry(outer, textvariable=self.query)
        search.pack(fill="x", pady=6)
        self.query.trace_add("write", lambda *_: self.filter_countries())
        columns = ttk.Frame(outer)
        columns.pack(fill="both", expand=True)
        self.listbox = tk.Listbox(columns, exportselection=False, width=32)
        self.listbox.pack(side="left", fill="y", padx=(0, 14))
        self.listbox.bind("<<ListboxSelect>>", self.show_selection)
        self.details = tk.Text(columns, wrap="word", font=("Sans", 12), state="disabled")
        self.details.pack(side="left", fill="both", expand=True)
        controls = ttk.Frame(outer)
        controls.pack(fill="x", pady=8)
        self.reload_button = ttk.Button(controls, text="Refresh country data", command=self.refresh)
        self.reload_button.pack(side="left")
        self.status = ttk.Label(controls, text="No data loaded")
        self.status.pack(side="left", padx=16)

    def refresh(self):
        self.reload_button.configure(state="disabled")
        self.status.configure(text="Loading...")
        threading.Thread(target=self._worker, daemon=True).start()

    def _worker(self):
        try:
            result = fetch_countries()
        except (requests.RequestException, ValueError, TypeError) as exc:
            self.after(0, lambda: self._error(str(exc)))
            return
        self.after(0, lambda: self._loaded(result))

    def _error(self, message):
        self.status.configure(text=f"Unable to load: {message}")
        self.reload_button.configure(state="normal")

    def _loaded(self, result):
        self.countries = result
        self.filter_countries()
        self.status.configure(text=f"{len(result)} countries loaded")
        self.reload_button.configure(state="normal")

    def filter_countries(self):
        term = self.query.get().strip().casefold()
        self.filtered = [
            country for country in self.countries
            if term in country.name.casefold() or term == country.code.casefold()
        ]
        self.listbox.delete(0, "end")
        for country in self.filtered:
            self.listbox.insert("end", country.name)
        if self.filtered:
            self.listbox.selection_set(0)
            self.show_selection()
        else:
            self._display("No matching country.")

    def _display(self, content):
        self.details.configure(state="normal")
        self.details.delete("1.0", "end")
        self.details.insert("1.0", content)
        self.details.configure(state="disabled")

    def show_selection(self, _event=None):
        selected = self.listbox.curselection()
        if selected and selected[0] < len(self.filtered):
            self._display(self.filtered[selected[0]].describe())


if __name__ == "__main__":
    CountriesWindow().mainloop()

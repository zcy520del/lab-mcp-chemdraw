r"""ChemDraw automation helper (Windows COM; self-contained release copy).

Verified on ChemDraw 2023 x64 (ProgID ChemDraw_x64.Application):
- MakeAtom() takes no args and lands at (0,0); Position returns a COPY --
  mutate it, then write back: p = a.Position; p.X/p.Y = ...; a.Position = p.
- Heteroatom auto-H labels are buggy (O renders as OH2): set a.LabelText
  explicitly ('OH', 'NO2', ...) instead of relying on ElementNumber.
- SaveAs(path[, fmt, dpi]): format driven by extension (.cdxml/.mol/.png ok).
- Typed makepy wrapper chemdraw2023.py is required for VARIANT-safe calls.
"""
import os
import sys

TMP = os.path.dirname(os.path.abspath(__file__))
if TMP not in sys.path:
    sys.path.insert(0, TMP)

import pythoncom
pythoncom.CoInitialize()

import win32com.client as wc
import chemdraw2023 as cdns

ELEMENTS = {"H": 1, "C": 6, "N": 7, "O": 8, "F": 9, "S": 16, "Cl": 17, "Br": 35, "I": 53, "P": 15}


def connect(visible=True):
    """Attach to or cold-start ChemDraw; returns typed IChemDrawApplication."""
    app = wc.Dispatch("ChemDraw_x64.Application")
    if visible:
        try:
            app.Visible = True
        except Exception:
            pass
    return cdns.IChemDrawApplication(
        app._oleobj_.QueryInterface(cdns.IChemDrawApplication.CLSID, pythoncom.IID_IDispatch))


def _typed(doc):
    return cdns.IChemDrawDocument(
        doc._oleobj_.QueryInterface(cdns.IChemDrawDocument.CLSID, pythoncom.IID_IDispatch))


def new_document(atyp):
    return _typed(atyp.Documents.Add())


def open_document(atyp, path):
    return _typed(atyp.Documents.Open(path))


def atom(dt, x, y, elem="C", label=None):
    a = dt.MakeAtom()
    p = a.Position          # Position returns a copy; write back below
    p.X = float(x)
    p.Y = float(y)
    a.Position = p
    if label:               # explicit label bypasses auto-H bug
        a.LabelText = label
    else:
        a.ElementNumber = ELEMENTS[elem] if isinstance(elem, str) else elem
    return a


def bond(dt, a1, a2, order=1):
    b = dt.MakeBond(a1, a2)
    b.BondOrder = order
    return b


def benzene(dt, cx=150.0, cy=150.0, r=40.0):
    """Build a Kekule benzene ring (alternating single/double); returns 6 atoms."""
    import math
    atoms = [atom(dt, cx + r * math.cos(math.radians(60 * i - 90)),
                  cy + r * math.sin(math.radians(60 * i - 90))) for i in range(6)]
    for i in range(6):
        bond(dt, atoms[i], atoms[(i + 1) % 6], 2 if i % 2 == 0 else 1)
    return atoms


def save(dt, path, dpi=None):
    """Export by extension (.cdxml/.mol/.png all verified)."""
    if dpi:
        dt.SaveAs(path, 0, dpi)
    else:
        dt.SaveAs(path)
    return os.path.exists(path)


__all__ = ["connect", "new_document", "open_document", "atom", "bond", "benzene", "save",
           "ELEMENTS", "wc", "cdns"]

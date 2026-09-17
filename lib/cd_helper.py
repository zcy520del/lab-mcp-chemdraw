r"""ChemDraw 自动化公共模块：连接 + 原子/键封装 + 文件导出（经验固化版）。

本机: ChemDraw 2023，ProgID ChemDraw_x64.Application，类型库 ChemDrawBase.dll → .pip-tmp\chemdraw2023.py。

已验证语义（务必遵守）:
- MakeAtom() 无参，默认落在 (0,0)！Position 返回 IChemDrawPoint **副本**——必须显式回写：
      p = a.Position; p.X = x; p.Y = y; a.Position = p
- 元素用 atom.ElementNumber（C=6, O=8, N=7...）。杂原子自动氢计数有 bug（OH 会显示成 OH2），
  含 H 的杂原子标签一律显式设：a.LabelText = "OH" / "NH2" 等。
- MakeBond(a1, a2) 只收两原子；键级 bond.BondOrder = 1/2/3。
- SaveAs(path[, fmt, dpi])：格式由扩展名驱动（.cdxml/.mol/.png），fmt 传 0 即可，dpi 可给 300。
- Open 回来的文档同样走 IChemDrawDocument 类型化包装。

批量画图推荐路线: SMILES → RDKit 生成 .mol（V2000）→ cd.Open + SaveAs(.png/.cdxml)。
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
    """附着或冷启动 ChemDraw，返回类型化 (IChemDrawApplication)。"""
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
    p = a.Position          # 副本！改完必须回写
    p.X = float(x)
    p.Y = float(y)
    a.Position = p
    if label:               # 杂原子含 H 时用显式标签绕开自动氢计数 bug
        a.LabelText = label
    else:
        a.ElementNumber = ELEMENTS[elem] if isinstance(elem, str) else elem
    return a


def bond(dt, a1, a2, order=1):
    b = dt.MakeBond(a1, a2)
    b.BondOrder = order
    return b


def benzene(dt, cx=150.0, cy=150.0, r=40.0):
    """画苯环（凯库勒式单双键交替），返回 6 个原子。"""
    import math
    atoms = [atom(dt, cx + r * math.cos(math.radians(60 * i - 90)),
                  cy + r * math.sin(math.radians(60 * i - 90))) for i in range(6)]
    for i in range(6):
        bond(dt, atoms[i], atoms[(i + 1) % 6], 2 if i % 2 == 0 else 1)
    return atoms


def save(dt, path, dpi=None):
    """按扩展名导出（.cdxml/.mol/.png 均验证过）。"""
    if dpi:
        dt.SaveAs(path, 0, dpi)
    else:
        dt.SaveAs(path)
    return os.path.exists(path)


__all__ = ["connect", "new_document", "open_document", "atom", "bond", "benzene", "save",
           "ELEMENTS", "wc", "cdns"]

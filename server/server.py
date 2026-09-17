"""stdio MCP server for ChemDraw COM automation (arbitrary atom/bond structures and
benzene derivatives; png/cdxml/mol export). Tools: mcp__chemdraw__chemdraw_structure,
mcp__chemdraw__chemdraw_benzene. Requires Windows, pywin32, ChemDraw installed."""
import json
import os
import sys
import traceback

LIB = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "lib")
if LIB not in sys.path:
    sys.path.insert(0, LIB)

os.environ.setdefault("PYTHONDONTWRITEBYTECODE", "1")

# Windows 控制台默认 GBK：强制 UTF-8，否则中文报错文本会炸掉 JSON-RPC。
try:
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")
except Exception:
    pass


def _out(sub=""):
    """输出目录：LAB_OUT_DIR > <cwd>/lab-out（不可写则逐级回退，跨工作区只读 cwd 不崩溃）。"""
    def _try(base):
        d = os.path.join(base, sub) if sub else base
        try:
            os.makedirs(d, exist_ok=True)
            probe = os.path.join(d, ".write-test")
            open(probe, "w").close()
            os.remove(probe)
            return d
        except OSError:
            return None

    env = os.environ.get("LAB_OUT_DIR")
    for cand in ([env] if env else []) + [os.path.join(os.getcwd(), "lab-out"),
                                          os.path.expandvars(r"%LOCALAPPDATA%\lab-out"),
                                          os.path.join(os.path.expanduser("~"), "Desktop", "ds", "lab-out")]:
        d = _try(cand)
        if d:
            return d
    import tempfile
    return tempfile.mkdtemp(prefix="lab-out-")


def tool_chemdraw_structure(args):
    """ChemDraw 任意结构: atoms/bonds/labels/save/name"""
    from cd_helper import connect, new_document, atom, bond, save
    atyp = connect()
    dt = new_document(atyp)
    objs = []
    for i, spec in enumerate(args["atoms"]):
        x, y, elem = spec[0], spec[1], spec[2] if len(spec) > 2 else "C"
        label = (args.get("labels") or {}).get(str(i))
        objs.append(atom(dt, float(x), float(y), elem, label=label))
    for bi, bj, order in args.get("bonds", []):
        bond(dt, objs[int(bi)], objs[int(bj)], int(order))
    out = {"atoms": int(dt.Atoms.Count), "bonds": int(dt.Bonds.Count)}
    for fmt in args.get("save", ["png"]):
        path = os.path.join(_out("chemdraw"), f"{args.get('name','structure')}.{fmt}")
        save(dt, path, dpi=300 if fmt == "png" else None)
        out[fmt] = path
    return out



def tool_chemdraw_benzene(args):
    """快捷苯环衍生物: substituents=[{pos:'top'|'bottom',label:'OH'}]"""
    from cd_helper import connect, new_document, atom, bond, benzene, save
    atyp = connect()
    dt = new_document(atyp)
    cx, cy, r = args.get("cx", 150), args.get("cy", 150), args.get("r", 40)
    ring = benzene(dt, float(cx), float(cy), float(r))
    top = min(ring, key=lambda a: a.Position.Y)
    bot = max(ring, key=lambda a: a.Position.Y)
    for sub in args.get("substituents", []):
        anchor = top if sub.get("pos") == "top" else bot
        dy = -35 if sub.get("pos") == "top" else 35
        a = atom(dt, anchor.Position.X, anchor.Position.Y + dy, label=sub["label"])
        bond(dt, anchor, a, 1)
    out = {"atoms": int(dt.Atoms.Count), "bonds": int(dt.Bonds.Count)}
    for fmt in args.get("save", ["png"]):
        path = os.path.join(_out("chemdraw"), f"{args.get('name','benzene')}.{fmt}")
        save(dt, path, dpi=300 if fmt == "png" else None)
        out[fmt] = path
    return out



TOOL_SPECS = {
"chemdraw_structure": {
        "description": ("Build an arbitrary structure in ChemDraw from explicit atoms/bonds "
                        "(coords in pt). Args: atoms=[[x,y,'C'],...], bonds=[[i,j,order],...], "
                        "labels={'0':'OH'} for heteroatom H-labels, save=['png','cdxml','mol'], name."),
        "inputSchema": {
            "type": "object",
            "properties": {
                "atoms": {"type": "array", "items": {"type": "array"}},
                "bonds": {"type": "array", "items": {"type": "array"}},
                "labels": {"type": "object"},
                "save": {"type": "array", "items": {"type": "string"}},
                "name": {"type": "string"},
            },
            "required": ["atoms"],
        },
        "fn": tool_chemdraw_structure,
    },
"chemdraw_benzene": {
        "description": ("Quick benzene ring (Kekule) with optional top/bottom substituents in ChemDraw, "
                        "export png/cdxml/mol. Args: cx,cy,r, substituents=[{pos:'top'|'bottom',label:'OH'}], save, name."),
        "inputSchema": {
            "type": "object",
            "properties": {
                "cx": {"type": "number"}, "cy": {"type": "number"}, "r": {"type": "number"},
                "substituents": {"type": "array", "items": {"type": "object"}},
                "save": {"type": "array", "items": {"type": "string"}},
                "name": {"type": "string"},
            },
        },
        "fn": tool_chemdraw_benzene,
    }
}


# ---------------------------------------------------------------- stdio ----
def _send(msg):
    body = json.dumps(msg, ensure_ascii=False)
    sys.stdout.write(body + "\n")
    sys.stdout.flush()


def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except json.JSONDecodeError:
            continue
        rid = req.get("id")
        method = req.get("method", "")
        params = req.get("params") or {}

        if method == "initialize":
            _send({"jsonrpc": "2.0", "id": rid, "result": {
                "protocolVersion": params.get("protocolVersion", "2024-11-05"),
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "chemdraw", "version": "1.0.0"},
            }})
        elif method.startswith("notifications/"):
            continue
        elif method == "ping":
            _send({"jsonrpc": "2.0", "id": rid, "result": {}})
        elif method == "tools/list":
            tools = [{"name": n, "description": s["description"], "inputSchema": s["inputSchema"]}
                     for n, s in TOOL_SPECS.items()]
            _send({"jsonrpc": "2.0", "id": rid, "result": {"tools": tools}})
        elif method == "tools/call":
            name = params.get("name")
            spec = TOOL_SPECS.get(name)
            if spec is None:
                _send({"jsonrpc": "2.0", "id": rid, "result": {
                    "isError": True, "content": [{"type": "text", "text": f"unknown tool {name}"}]}})
                continue
            try:
                out = spec["fn"](params.get("arguments") or {})
                _send({"jsonrpc": "2.0", "id": rid, "result": {
                    "content": [{"type": "text", "text": json.dumps(out, ensure_ascii=False)}]}})
            except Exception as exc:
                tb = traceback.format_exc(limit=4)
                _send({"jsonrpc": "2.0", "id": rid, "result": {
                    "isError": True, "content": [{"type": "text", "text": f"{exc}\n{tb}"}]}})
        else:
            _send({"jsonrpc": "2.0", "id": rid,
                   "error": {"code": -32601, "message": f"method not found: {method}"}})


if __name__ == "__main__":
    main()

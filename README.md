# ChemDraw MCP Server (DSH plugin)

Build chemical structures in ChemDraw via COM: arbitrary atoms/bonds or quick benzene derivatives, export PNG/CDXML/MOL. DSH plugin wrapping a stdio MCP server.

**Windows only.** These servers drive the real commercial applications through COM
automation — the target software must be installed and licensed on the machine.

## Verified on

ChemDraw 2023 (x64 ProgID ChemDraw_x64.Application). lib/chemdraw2023.py wraps ChemDrawBase.dll v22 typelib.

## Tools

- `chemdraw_structure` — atoms [[x,y,'C']...], bonds [[i,j,order]...], labels {'0':'OH'}, save formats
- `chemdraw_benzene` — ring + top/bottom substituents shorthand

Outputs are written to `{cwd}/lab-out/` (override with env `LAB_OUT_DIR`).
First call cold-starts the application and can take 30–120 s.

## Requirements

- Windows + Python 3.10+ with `pywin32` (`pip install pywin32`)
- The target application installed and COM-registered

## Install as a DSH plugin

```bash
dsh plugin --profile web add <path-or-git-url>
```

The bundled `cordis.patch.yml` registers the server through
`@deepseek-ai/dsh-mcp-client`; tools appear as `mcp__chemdraw__*`.

### Manual MCP client config (Claude Desktop etc.)

```json
{
  "mcpServers": {
    "chemdraw": {
      "command": "python",
      "args": ["<abs-path>/server/server.py"]
    }
  }
}
```

Point `command` at your real interpreter (on Windows avoid the Microsoft Store
`python.exe` stub).

## Layout

```
server/server.py     stdio MCP server (JSON-RPC 2.0)
lib/*.py             helper module + makepy typelib wrappers (self-contained)
cordis.patch.yml     DSH bundle patch
```

## Regenerating makepy wrappers

If your app version differs, rebuild the typed wrapper and drop it into `lib/`:

```bash
python -m win32com.client.makepy -o lib/<wrapper>.py "<path-to-tlb-or-dll>"
```

(See each repo's README notes for the exact typelib location.)

## Caveats learned the hard way (already handled in code)

- COM points must be `VT_ARRAY|VT_R8` VARIANTs; some methods need the typed wrapper.
- ChemDraw `Position` returns a copy — writeback required (handled in cd_helper).
- AutoCAD modal dialogs freeze the COM pump; cad_helper ships `close_modal_dialogs()`.
- stdout is forced UTF-8 (GBK consoles corrupt JSON-RPC frames otherwise).

## License

MIT

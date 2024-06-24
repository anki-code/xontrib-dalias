"""
Library of xonsh subprocess specification modifiers e.g. ``$(@json echo '{}')``.
"""
from xonsh.built_ins import XSH
from xonsh.procs.specs import SpecAttrModifierAlias as _mod

__all__ = ()

imp = type('ImpCl', (object,), {'__getattr__':lambda self, name: __import__(name) })()  # Sugar for inline import

XSH.aliases['@lines'] = _mod({"output_format": 'list_lines'}, "Set `list_lines` output format.")
XSH.aliases['@json'] = _mod({"output_format": lambda lines: imp.json.loads('\n'.join(lines))}, "Set `json` output format.")
XSH.aliases['@path'] = _mod({"output_format": lambda lines: imp.pathlib.Path(':'.join(lines))}, "Set `path` output format.")
XSH.aliases['@yaml'] = _mod({"output_format": lambda lines: imp.yaml.safe_load('\n'.join(lines))}, "Set `yaml` output format.")
XSH.aliases['@noerr'] = _mod({"raise_subproc_error": False}, "Set `raise_subproc_error` to False.")

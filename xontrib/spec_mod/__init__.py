"""
Library of xonsh subprocess specification modifiers e.g. ``$(@json echo '{}')``.
"""
from xonsh.built_ins import XSH
from xonsh.procs.specs import SpecAttrModifierAlias as _mod
from xontrib.spec_mod.to_dict import load_as_dict

__all__ = ()

_imp = type('ImpCl', (object,), {'__getattr__':lambda self, name: __import__(name)})()  # Sugar for inline import

XSH.aliases['@lines'] = _mod({"output_format": 'list_lines'}, "Set `list_lines` output format.")
XSH.aliases['@json'] = _mod({"output_format": lambda lines: _imp.json.loads('\n'.join(lines))}, "Return `json` output format.")
XSH.aliases['@dict'] = _mod({"output_format": lambda lines: load_as_dict('\n'.join(lines))['dict']}, "Return `dict` output format.")
XSH.aliases['@path'] = _mod({"output_format": lambda lines: _imp.pathlib.Path(':'.join(lines))}, "Return `path` output format.")
XSH.aliases['@yaml'] = _mod({"output_format": lambda lines: _imp.yaml.safe_load('\n'.join(lines))}, "Return `yaml` output format.")

XSH.aliases['@err'] = _mod({"raise_subproc_error": True}, "Set `raise_subproc_error` to True.")
XSH.aliases['@noerr'] = _mod({"raise_subproc_error": False}, "Set `raise_subproc_error` to False.")

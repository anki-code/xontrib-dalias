"""
Library of xonsh subprocess specification modifiers e.g. ``$(@json echo '{}')``.
"""
from xonsh.built_ins import XSH

try:
    # xonsh > 0.17.0
    from xonsh.procs.specs import SpecAttrDecoratorAlias as _mod
except:
    # xonsh == 0.17.0
    from xonsh.procs.specs import SpecAttrModifierAlias as _mod
    
from xontrib.spec_mod.to_dict import load_as_dict

__all__ = ()


#
# Format output
#

XSH.aliases['@lines'] = _mod({"output_format": 'list_lines'}, "Set `list_lines` output format.")

def _split_output(output_lines):
    """Split lines by whitespaces using xonsh lexer.
    The source code is from `xonsh.built_ins.subproc_captured_inject` (it's `@$()` operator logic).
    """
    toks = []
    for line in output_lines:
        line = line.rstrip(os.linesep)
        toks.extend(__xonsh__.execer.parser.lexer.split(line))
    return toks

XSH.aliases['@parts'] = _mod({"output_format": _split_output}, "Output format: list of parts like in `@$()`.")


#
# Return object
#

XSH.aliases['@json'] = _mod({"output_format": lambda lines: XSH.imp.json.loads('\n'.join(lines))}, "Return `json` output format.")
XSH.aliases['@dict'] = _mod({"output_format": lambda lines: load_as_dict('\n'.join(lines))['dict']}, "Return `dict` output format.")
XSH.aliases['@path'] = _mod({"output_format": lambda lines: XSH.imp.pathlib.Path(':'.join(lines))}, "Return `path` output format.")
XSH.aliases['@yaml'] = _mod({"output_format": lambda lines: XSH.imp.yaml.safe_load('\n'.join(lines))}, "Return `yaml` output format.")

#
# Error handling
#

XSH.aliases['@err'] = _mod({"raise_subproc_error": True}, "Set `raise_subproc_error` to True.")
XSH.aliases['@noerr'] = _mod({"raise_subproc_error": False}, "Set `raise_subproc_error` to False.")



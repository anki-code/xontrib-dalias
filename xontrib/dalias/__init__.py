"""
Library of xonsh subprocess specification modifiers e.g. ``$(@json echo '{}')``.
"""
import os
from xonsh.built_ins import XSH

try:
    # xonsh > 0.17.0
    from xonsh.procs.specs import SpecAttrDecoratorAlias as _mod
except:
    # xonsh == 0.17.0
    from xonsh.procs.specs import SpecAttrModifierAlias as _mod

from xontrib.dalias.to_dict import load_as_dict

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

XSH.aliases['@parts'] = _mod({"output_format": _split_output}, "Alias decorator. Output format: list of parts like in `@$()`.")


#
# Return object
#
def _output_to_path(lines):
    """Transform list of lines to Path object or list of Paths.
    If the path is empty the result will be None or excluded from the list.
    """
    if len(lines) == 0:
        return None
    elif len(lines) == 1:
        line = lines[0].strip()
        if not line:
            return None
        return XSH.imp.pathlib.Path(line)
    else:
        return [XSH.imp.pathlib.Path(l.strip()) for l in lines if l.strip()]
XSH.aliases['@path'] = _mod({"output_format": _output_to_path}, "Alias decorator. Returns Path object or list of Paths. Empty line excluded.")

XSH.aliases['@json'] = _mod({"output_format": lambda lines: XSH.imp.json.loads('\n'.join(lines))}, "Alias decorator. Parses json and returns json object.")
XSH.aliases['@dict'] = _mod({"output_format": lambda lines: load_as_dict('\n'.join(lines))['dict']}, "Alias decorator. Returns dict object.")
XSH.aliases['@yaml'] = _mod({"output_format": lambda lines: XSH.imp.yaml.safe_load('\n'.join(lines))}, "Alias decorator. Parses yaml and returns dict.")

#
# Error handling
#

XSH.aliases['@err'] = _mod({"raise_subproc_error": True}, "Alias decorator. Set `raise_subproc_error` to True.")
XSH.aliases['@noerr'] = _mod({"raise_subproc_error": False}, "Alias decorator. Set `raise_subproc_error` to False.")



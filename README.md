<p align="center">
Library of xonsh subprocess specification modifiers.
</p>

<p align="center">
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/anki-code/xontrib-spec-mod" target="_blank">tweet</a>.
</p>


## Installation

To install use pip:

```xsh
xpip install xontrib-spec-mod
xpip install 'xontrib-spec-mod[dict,yaml]'  # Additional modifiers.
```
Load:
```xsh
xontrib load spec_mod
```

## Usage

### Transform output to object

Modifiers:

* `@lines` - return list of lines.
* `@json` - json to Python `dict`.
* `@dict` - dict-like object (json, JavaScript object, Python dict) to Python `dict`. 
  Install extra support via `xpip install 'xontrib-spec-mod[dict]'`.
* `@path` - string to `pathlib.Path`.
* `@yaml` - YAML to Python `dict`. Install `xpip install 'xontrib-spec-mod[yaml]'`.

Examples:
```xsh
$(@lines ls /)
# ['/bin', '/etc', '/home']

$(@json echo '{"a":1}')  # Try with `curl` ;)
# dict({"a":1})

$(@path which xonsh)
# Path('/path/to/xonsh')

$(@path which xonsh).parent
# Path('/path/to')


aliases['ydig'] = '@yaml dig +yaml'  # Update `dig` via `brew install bind` to have `+yaml`.
y = $(ydig google.com)
y[0]['type']
# 'MESSAGE'
```

### Error handling

Modifiers:
* `@err` - set `$RAISE_SUBPROC_ERROR=True` for the command.
* `@noerr` - set `$RAISE_SUBPROC_ERROR=False` for the command.

Examples:
```xsh
$RAISE_SUBPROC_ERROR = True  # General environment.
if ![@noerr ls nononofile]:  # Do not raise exception in case of error.
    echo file 
```

## Development

```sh
# install pre-commit plugins and activate the commit hook
pre-commit install
pre-commit autoupdate
```

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template).

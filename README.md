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
xpip install 'xontrib-spec-mod[yaml]'
xpip install 'xontrib-spec-mod[dict]'
```

## Usage

```xsh
xontrib load spec_mod
```
### Transform output to object
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

```xsh
$RAISE_SUBPROC_ERROR = True
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

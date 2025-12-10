<p align="center">
Library of decorator aliases (daliases) for the xonsh shell.
</p>

<p align="center">
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/anki-code/xontrib-dalias" target="_blank">tweet</a>.
</p>


## Installation

To install use pip:

```xsh
xpip install xontrib-dalias
# or
xpip install 'xontrib-dalias[dict,yaml]'  # With extra decorators.
```
Load:
```xsh
xontrib load dalias
```

## Usage

### Transform output to object

Decorators:

XSH.aliases['@split'] = _mod({"output_format": _split_output}, "Alias decorator. Output format: list of parts.")
XSH.aliases['@split-lines'] = _mod({"output_format": _split_lines_output}, "Alias decorator. Output format: list of splitted lines.")
XSH.aliases['@split-lexer'] = _mod({"output_format": _lexer_split_output}, "Alias decorator. Output format: list of parts by xonsh lexer (same as `@$()`).")
XSH.aliases['@split-lexer-lines'] = _mod({"output_format": _lexer_split_lines_output}, "Alias decorator. Output format: list of splitted lines by xonsh lexer (same as `@$()`).")


* Default:
    * `@lines` - return list of lines.
    * `@json` - json to Python `dict`.
    * `@jsonl` - json lines to Python `list` with `dict` objects.
    * `@path` - string to [`pathlib.Path`](https://docs.python.org/3/library/pathlib.html).
    * `@split` - split output by whitespaces.
    * `@split-lines` - split output lines by whitespaces.
    * `@split-lexer` - split output into parts using xonsh lexer. It's the same as [builtin `@$()` operator](https://xon.sh/tutorial.html#command-substitution-with).
    * `@split-lexer-lines` - split output lines into parts using xonsh lexer. It's the same as [builtin `@$()` operator](https://xon.sh/tutorial.html#command-substitution-with).
* Extra (`xpip install 'xontrib-dalias[dict,yaml]'`):
    * `@dict` - dict-like object (json, JavaScript object, Python dict) to Python `dict`.
    * `@dictl` - dict-like objects (json, JavaScript object, Python dict) to Python `list` with `dict` objects.
    * `@yaml` - YAML to Python `dict`.

#### Examples
```xsh
$(@lines ls /)
# ['/bin', '/etc', '/home']

$(@json echo '{"a":1}')  # Try with `curl` ;)
# dict({"a":1})

$(@jsonl echo '{"a":1}\n{"b":2}')
# [{'a': 1}, {'b': 2}]

docker inspect @($(@json docker ps --format json)['ID'])
# Container info


$(@path which -s xonsh)
# Path('/path/to/xonsh')

$(@path which -s xonsh).parent
# Path('/path/to')

$(@path echo '/tmp1\n/tmp2')
# [Path('/tmp1'), Path('/tmp2')]

$(@path echo ' ')  # Safe
# None

$(@path echo ' \n\n/tmp1')  # Safe
# [Path('/tmp1')]


aliases['ydig'] = '@yaml dig +yaml'  # Update `dig` via `brew install bind` to have `+yaml`.
y = $(ydig google.com)
y[0]['type']
# 'MESSAGE'
```

Piping into decorated alias to get object:

```xsh
$(echo '{"a":1}' | @json cat)
# dict({"a":1})
```

```xsh
aliases['@j'] = '@json cat'
$(echo '{"a":1}' | @j)
# dict({"a":1})
```


### Error handling

Default decorators:
* `@err` - set `$RAISE_SUBPROC_ERROR=True` for the command.
* `@noerr` - set `$RAISE_SUBPROC_ERROR=False` for the command.

Examples:
```xsh
$RAISE_SUBPROC_ERROR = True  # General environment.
if ![@noerr ls nononofile]:  # Do not raise exception in case of error.
    echo file 
```

## Credits

This package was created with [xontrib template](https://github.com/xonsh/xontrib-template).

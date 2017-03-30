# pants-ensime-plugins

A plugin to generate an .ensime from a pants config.

Current Plugins:

* ensime.pants - An updated ensime generator

## Installation

It's intended for these to be distributed via pypi.

Change your pants.ini

```
[GLOBAL]
plugin_version: 1.1.1

plugins: +[
    "ensime.pants.==%(plugin_version)s",
  ]

backend_packages: +[
    "ensime.pants",
  ]
```

## Usage

```
./pants ensime
```

## History

Originally a plugin in the pants repo written by lahosken and contributed to by several pants authors, it was rewritten by anatolydwnld, extracted from the pants repo with the intention of pushing it under the ensime repository to better keep up with ensime file format changes.

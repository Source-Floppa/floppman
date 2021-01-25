## Floppman

`floppman` or `flp` is the package manager for the Source Floppa distribution.\
It uses the `flopbuild` package format (heavily inspired by CRUX's Pkgfiles)

### Usage (not finished yet)

`floppman` will be used like this:
```
install   - find and install a package from the local source tree 
sync      - sync the local source tree with the nearest/fastest mirror 
update    - update a package / preform a system update
uninstall - remove a package
list	  - list all installed packages
find	  - find a package in the local source tree (reports name, path and description)
config    - opens a TUI interface that helps you configure floppman
```

### Building

`floppman` is built using a pre-configured Makefile \
It is installable by doing:
```
$ sudo make install
```
Or, if you don't have `sudo` installed, just do it as `root`.

### Bugs

If you notice any bugs, you can either report them in the Github issues menu, or contact us on `matrix`\
Zenithium matrix: `@zenithium_:matrix.org`\
avcado's matrix: `@avc1d0:matrix.org`\
Source Floppa will eventually have an IRC channel and this `README` will be updated 

### Description
Use keycodes instead of keysyms. This way, input is independent from keyboard layout (you can use the keys.h file to customize, or get the keycodes with `wev` or `xkbcli interactive-wayland` (x11-libs/libxkbcommon[tools] in gentoo)).

### Download
- [git branch](https://codeberg.org/sevz/dwl/src/branch/keycodes)
- [2023-11-25](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/keycodes/keycodes.patch)

### Config after patching 
(run in DWL source directory)
```
export XKB_DEFAULT_VARIANT=yourbestkeyboardlayout
cc -lxkbcommon -o generate-keys generate-keys.c
./generate-keys
sudo make install
```

### Authors
- [sevz](https://codeberg.org/sevz)

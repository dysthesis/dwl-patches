### Description
This patch adds an extra layout to dwl called `mastercol` in which the windows in the master area are arranged in columns of equal size. The number of columns is always nmaster + 1, and the last column is a stack of leftover windows just like the normal tile layout. It effectively acts like the default tiling mode, except provides for vertical instead of horizontal master windows.

For gaps, apply `mastercolumn-gaps.patch` on top of `mastercolumn.patch` and `gaps.patch`.

### Download
##### `mastercolumn.patch`
- [git branch](https://codeberg.org/dsst/dwl/src/branch/mastercolumn)
- [2024-07-13](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/mastercolumn/mastercolumn.patch)

##### `mastercolumn-gaps.patch`
- [git branch](https://codeberg.org/dsst/dwl/src/branch/mastercolumn-gaps)
- [2024-07-16](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/mastercolumn/mastercolumn-gaps.patch)

### Authors
- [dsst](https://codeberg.org/dsst)

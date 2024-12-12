### Description
This patch is a modified version of [vanitygaps][vanitygaps] that adds gaps
around clients regardless of a layout. It means you can apply any layout patch
and the gaps will be shown properly as long as the layout does not add any gaps
on its own.

This works by allowing a layout to place clients normally without gaps,
and then correcting positions and dimensions of clients afterwards to add gaps around them.
This approach is very flexible but the downside is that you will always have
"outer" gaps (between monitor edge and a window) if "inner" gaps are non-zero.
But for me, personally, it is not a problem because I always want "outer" gaps
to be as big or bigger than "inner" gaps.

[vanitygaps]: https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/vanitygaps

### Download
- [0.7](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/genericgaps/genericgaps.patch)
- [git branch](https://codeberg.org/NikitaIvanov/dwl/src/branch/genericgaps)

### Authors
- [Nikita Ivanov](https://github.com/NikitaIvanovV)

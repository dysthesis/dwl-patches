### Description
Add the meson build system.

This is useful for people who do not want to self-manage a wlroots installation.

To enable Xwayland support, you will need to enable it in the wlroots subproject:
```sh
meson setup -Dwlroots:xwayland=enabled build
```

### Download
- [git branch](/sewn/dwl/src/branch/meson)
- [2024-08-27](/dwl/dwl-patches/raw/branch/main/patches/meson/meson.patch)

### Authors
- [sewn](/sewn)


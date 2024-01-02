### Description

This patch adds `menu` command, which allows dwl to interface with dmenu-like programs.

By default, two menus are available:
- focusing a window by its title by pressing `Alt+o`
- selecting a layout from a list by pressing `Alt+Shift+o`

Edit `menus` array and `MENU` macro in `config.h` to add/change menus and use a different dmenu program.

### Download
- [2023-07-15](https://github.com/djpohly/dwl/compare/main...NikitaIvanovV:menu.patch)

### Authors
- [Nikita Ivanov](https://github.com/NikitaIvanovV)
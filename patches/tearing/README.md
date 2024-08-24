### Description
This patch adds support for tearing protocol. To get it working `export WLR_DRM_NO_ATOMIC=1` is probably required.
Setting `ForceTearingRule` is also probably required since surfaces always receive presentation hint 0 (VSYNC) as far as i can tell.

Set rules in the config.h (exact string match):
```
static const ForceTearingRule force_tearing[] = {
	{.title = "", .appid = "oni.exe"},
	{.title = "", .appid = "hl_linux"},
	{.title = "", .appid = "steam_app_210970"},
};
```
### Download
- [git branch](https://codeberg.org/korei999/dwl/src/branch/tearing)
- [2024-08-15](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/tearing/tearing.patch)
### Authors
- [korei999](https://codeberg.org/korei999)

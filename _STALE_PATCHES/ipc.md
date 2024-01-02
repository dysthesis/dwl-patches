### Description
Largely based on [raphi](https://sr.ht/~raphi/)'s [somebar](https://sr.ht/~raphi/somebar/), this patch provides an ipc for wayland clients to get and set dwl state. The ipc is intended for status bars, but can also be scripted with [dwlmsg](https://codeberg.org/notchoc/dwlmsg).

### Download
 - [2023-10-28](https://gist.githubusercontent.com/fbushstone/b116c44340eb7a7878de1119dd931ca5/raw/ee66ac9e2a5dddd9b528df553e21080c2811e974/ipc-v2-fixed.patch) Updated version of 2023-04-29, prevents ipc from freezing the compositor in printstatus.
 - [2023-04-29](https://github.com/djpohly/dwl/compare/main...madcowog:ipc-v2.patch) Use this for dwl-ipc-unstable-v2. If you are using commit [9d68554](https://github.com/djpohly/dwl/commit/9d68554c59a886b641d27a364884fb461af2d4f1) or later, use this. For status bars this protocol is supported by dwlb, Waybar and dwl-bar.
 - [2023-04-29](https://github.com/djpohly/dwl/compare/main...madcowog:ipc-bbdf2.patch) Use this for dwl-ipc-unstable-v1. If you are using commit [bbdaf2a9](https://github.com/djpohly/dwl/commit/bbdf2a913b72e7a308ee0dfde6518a4285d4a775), [release 0.4](https://github.com/djpohly/dwl/releases/tag/v0.4) or earlier, use this. For status bars, this protocol is supported by dwl-bar.
 - [2023-02-20](https://lists.sr.ht/~raphi/public-inbox/patches/39166) Use this for net-tapesoftware-dwl-wm-unstable-v1. If you are using commit [c69a2bec](https://github.com/djpohly/dwl/commit/c69a2bec3ff417fbc4ea8fec0a49096773e01e7d) or later, use this. For status bars this protocol is supported by somebar.

### Authors
 - [MadcowOG](https://github.com/MadcowOG)

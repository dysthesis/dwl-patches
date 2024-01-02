## Submitting patches
As with dwm, community patch contributions are heartily welcomed! If you have a customization that others may appreciate, or a useful enhancement which doesn't quite fit into the trim-and-tidy philosophy of dwl, please post it here! Implement your modifications as a public GitHub branch (multiple commits are OK), then create a new page on the wiki using this example (you can add or remove sections as you like):
```markdown
### Description
Insert a short summary of changes that your patch implements.

### Download
- [yyyy-mm-dd](https://codeberg.org/dwl/dwl/compare/main...YOURUSERNAME:BRANCH.patch)

### Authors
- [Your Name](https://github.com/YOURUSERNAME)
```
Then add your patch to the appropriate section in the list below and to the sidebar like so: 
```markdown
* [PATCHNAME](https://codeberg.org/dwl/dwl/wiki/PATCHNAME)
``` 
Please ensure that the only changes in that branch are those needed for the patch; do not include multiple patches, personal changes to config.h, etc.

### Layouts
* [bottomstack](https://codeberg.org/dwl/dwl/wiki/bottomstack)
* [centeredmaster](https://codeberg.org/dwl/dwl/wiki/centeredmaster)
* [column](https://codeberg.org/dwl/dwl/wiki/column-layout)
* [cyclelayouts](https://codeberg.org/dwl/dwl/wiki/cyclelayouts)
* [deck](https://codeberg.org/dwl/dwl/wiki/deck)
* [fibonacci](https://codeberg.org/dwl/dwl/wiki/fibonacci)
* [gaplessgrid](https://codeberg.org/dwl/dwl/wiki/gaplessgrid)
* [gridmode](https://codeberg.org/dwl/dwl/wiki/gridmode)
* [vertile](https://codeberg.org/dwl/dwl/wiki/vertile)

### Clients placement
* [alwayscenter](https://codeberg.org/dwl/dwl/wiki/alwayscenter)
* [attachabove](https://codeberg.org/dwl/dwl/wiki/attachabove)
* [attachbottom](https://codeberg.org/dwl/dwl/wiki/attachbottom)
* [attachtop](https://codeberg.org/dwl/dwl/wiki/attachtop)
* [restoretiling](https://codeberg.org/dwl/dwl/wiki/restoretiling)

### Clients & tags manipulation
* [centerterminal](https://codeberg.org/dwl/dwl/wiki/centerterminal)
* [cfacts](https://codeberg.org/dwl/dwl/wiki/cfacts)
* [focusmaster](https://codeberg.org/dwl/dwl/wiki/focusmaster)
* [focusdir](https://codeberg.org/dwl/dwl/wiki/focusdir)
* [movestack](https://codeberg.org/dwl/dwl/wiki/movestack)
* [movecenter](https://codeberg.org/dwl/dwl/wiki/movecenter)
* [moveresizekb](https://codeberg.org/dwl/dwl/wiki/moveresizekb)
* [move-stack-top](https://codeberg.org/dwl/dwl/wiki/move-stack-top)
* [pertag](https://codeberg.org/dwl/dwl/wiki/pertag)
* [push](https://codeberg.org/dwl/dwl/wiki/push)
* [rotatetags](https://codeberg.org/dwl/dwl/wiki/rotatetags)
* [shiftview](https://codeberg.org/dwl/dwl/wiki/shiftview)
* [singletagset](https://codeberg.org/dwl/dwl/wiki/singletagset)
* [sticky](https://codeberg.org/dwl/dwl/wiki/sticky)
* [swapandfocusdir](https://codeberg.org/dwl/dwl/wiki/swapandfocusdir)
* [title-change-urgent](https://codeberg.org/dwl/dwl/wiki/title%E2%80%90change%E2%80%90urgent)
* [zoomswap](https://codeberg.org/dwl/dwl/wiki/zoomswap)

### Rules
* [center](https://codeberg.org/dwl/dwl/wiki/center)
* [customfloat](https://codeberg.org/dwl/dwl/wiki/customfloat)
* [namedscratchpads](https://codeberg.org/dwl/dwl/wiki/namedscratchpads)
* [stickyrule](https://codeberg.org/dwl/dwl/wiki/stickyrule)
* [swallow](https://codeberg.org/dwl/dwl/wiki/swallow)
* [switchtotag](https://codeberg.org/dwl/dwl/wiki/switchtotag)
* [regexrules](https://codeberg.org/dwl/dwl/wiki/regexrules)

### Input
* [chainkeys](https://codeberg.org/dwl/dwl/wiki/chainkeys)
* [kblayout](https://codeberg.org/dwl/dwl/wiki/kblayout)
* [keychord](https://codeberg.org/dwl/dwl/wiki/keychord)
* [lockedkeys](https://codeberg.org/dwl/dwl/wiki/lockedkeys)
* [naturalscrolltrackpad](https://codeberg.org/dwl/dwl/wiki/naturalscrolltrackpad)
* [primary-sel-off](https://codeberg.org/dwl/dwl/wiki/Primary-Selection)
* [sway-pointer-constraints](https://codeberg.org/dwl/dwl/wiki/Sway-pointer-constraints)
* [toggleKbLayout](https://codeberg.org/dwl/dwl/wiki/toggleKbLayout)
* [toggleLayoutImmediately](https://codeberg.org/dwl/dwl/wiki/toggleLayoutImmediately)
* [virtualpointer](https://codeberg.org/dwl/dwl/wiki/virtualpointer)
* [XF86keysym](https://codeberg.org/dwl/dwl/wiki/XF86keysym)
* [pointerGesturesUnstableV1](https://codeberg.org/dwl/dwl/wiki/pointerGesturesUnstableV1)
* [modes](https://codeberg.org/dwl/dwl/wiki/modes)

### Cursor
* [cursortheme](https://codeberg.org/dwl/dwl/wiki/cursortheme)
* [cursorwarp](https://codeberg.org/dwl/dwl/wiki/cursorwarp)
* [dragmfact](https://codeberg.org/dwl/dwl/wiki/dragmfact)
* [hidecursor](https://codeberg.org/dwl/dwl/wiki/hidecursor)
* [mouse-follows-focus](https://codeberg.org/dwl/dwl/wiki/mouse-follows-focus)
* [nomousefocus](https://codeberg.org/dwl/dwl/wiki/nomousefocus)
* [relativemouseresize](https://codeberg.org/dwl/dwl/wiki/relativemouseresize)
* [unclutter](https://codeberg.org/dwl/dwl/wiki/unclutter)
* [xcursor](https://codeberg.org/dwl/dwl/wiki/xcursor)

### Monitor
* [autorotation](https://codeberg.org/dwl/dwl/wiki/autorotation)
* [focusMonPointer](https://codeberg.org/dwl/dwl/wiki/focusMonPointer)
* [monitorconfig](https://codeberg.org/dwl/dwl/wiki/monitorconfig)

### Other
* [alphafocus](https://codeberg.org/dwl/dwl/wiki/alphafocus)
* [clipboardipc](https://codeberg.org/dwl/dwl/wiki/clipboardipc)
* [clipboardManager](https://codeberg.org/dwl/dwl/wiki/clipboardManager)
* [drmLeaseManager](https://codeberg.org/dwl/dwl/wiki/DRMLeaseManager)
* [floatBorderColor](https://codeberg.org/dwl/dwl/wiki/floatBorderColor)
* [genericgaps](https://codeberg.org/dwl/dwl/wiki/genericgaps)
* [ipc](https://codeberg.org/dwl/dwl/wiki/ipc)
* [keyboardshortcutsinhibit](https://codeberg.org/dwl/dwl/wiki/keyboardshortcutsinhibit)
* [keymap](https://codeberg.org/dwl/dwl/wiki/keymap)
* [menu](https://codeberg.org/dwl/dwl/wiki/menu)
* [onlyquitonempty](https://codeberg.org/dwl/dwl/wiki/onlyquitonempty)
* [outputPowerManagement](https://codeberg.org/dwl/dwl/wiki/outputPowerManagement)
* [pointerConstraints](https://codeberg.org/dwl/dwl/wiki/pointerConstraints)
* [privilegeDrop](https://codeberg.org/dwl/dwl/wiki/privilegeDrop)
* [restartdwl](https://codeberg.org/dwl/dwl/wiki/restartdwl)
* [swaycompat](https://codeberg.org/dwl/dwl/wiki/swaycompat)
* [touchscreen](https://codeberg.org/dwl/dwl/wiki/touchscreen)
* [uselessgaps](https://codeberg.org/dwl/dwl/wiki/uselessgaps)
* [gestures](https://codeberg.org/dwl/dwl/wiki/gestures)


### Description
Add swipe gestures to trigger functions, similar to [libinput-gestures](https://github.com/bulletmark/libinput-gestures/tree/master). It supports the following gestures: `SWIPE_UP`, `SWIPE_DOWN`, `SWIPE_LEFT` and `SWIPE_RIGHT`

```c
static const Gesture gestures[] = {
  { SWIPE_LEFT, shiftview, { .i = 1 } },
  { SWIPE_RIGHT, shiftview, { .i = -1 } },
};
```

**NOTE:** the example above requires the following patch https://github.com/djpohly/dwl/wiki/shiftview

### Download
Apply on top of [pointerGesturesUnstableV1 patch](https://github.com/djpohly/dwl/wiki/pointerGesturesUnstableV1).

- [2023-09-09](https://github.com/wochap/dwl/compare/pointer-gestures-unstable-v1...wochap:gestures.patch)

### Authors
- [wochap](https://github.com/wochap)
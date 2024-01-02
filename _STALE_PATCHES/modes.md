### Description
Implement modes, default mode is `NORMAL`

### Example

In the example below, you declare a mode: `BROWSER`, which is activated when you press <kbd>modkey</kbd> + <kbd>b</kbd>. Then, you can press <kbd>f</kbd> to launch `Firefox` and return to the default `NORMAL` mode.

```c
enum {
  BROWSER,
};
const char *modes_labels[] = {
  "browser",
};

static const Key keys[] = {
  // ...
  { MODKEY, XKB_KEY_b, entermode, {.i = BROWSER} },
  // ...
};

static const Modekey modekeys[] = {
  /* mode      modifier                  key                 function        argument */
  { BROWSER, { 0, XKB_KEY_f, spawn, SHCMD("firefox") } },
  { BROWSER, { 0, XKB_KEY_f, entermode, {.i = NORMAL} } },
  { BROWSER, { 0, XKB_KEY_Escape, entermode, {.i = NORMAL} } },
};
```

### Download
- [2023-09-11](https://github.com/djpohly/dwl/compare/main...wochap:modes.patch)

### Authors
- [wochap](https://github.com/wochap)
### Description

This is a port of centeredmaster patch for dwm: <https://dwm.suckless.org/patches/centeredmaster>

centeredmaster centers the nmaster area on screen, using mfact * monitor
width & height, with the stacked windows distributed to the left and
right. It can be selected with `Alt+c`.

With one and two clients in master respectively this results in:

```
+------------------------------+       +------------------------------+
|+--------++--------++--------+|       |+--------++--------++--------+|
||        ||        ||        ||       ||        ||        ||        ||
||        ||        ||        ||       ||        ||   M1   ||        ||
||        ||        ||        ||       ||        ||        ||        ||
||  S2    ||   M    ||   S1   ||       ||        |+--------+|        ||
||        ||        ||        ||       ||        |+--------+|        ||
||        ||        ||        ||       ||        ||        ||        ||
||        ||        ||        ||       ||        ||   M2   ||        ||
||        ||        ||        ||       ||        ||        ||        ||
|+--------++--------++--------+|       |+--------++--------++--------+|
+------------------------------+       +------------------------------+
```

### Download
- [2023-05-20](https://github.com/djpohly/dwl/compare/main...NikitaIvanovV:centeredmaster.patch)

### Authors
- [Nikita Ivanov](https://github.com/NikitaIvanovV)
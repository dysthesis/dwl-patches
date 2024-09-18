# accessnthmon

### Description
Port of dwm's accessnthmon. Adds functions to tag and focus monitor by index.

### Download
- [git branch](https://codeberg.org/Rutherther/dwl/src/branch/patch/accessnthmonitor)
- [2024-05-10](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/accessnthmon/accessnthmon.patch)
### Authors
- [Rutherther](https://codeberg.org/Rutherther)
- [Palanix](https://codeberg.org/Palanix)

---
# alwayscenter

### Description
Automatically center floating windows.

### Download
- [git branch](https://codeberg.org/guidocella/dwl/src/branch/alwayscenter)
- [2024-06-05](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/alwayscenter/alwayscenter.patch)

### Authors
- [Guido Cella](https://codeberg.org/guidocella)

---
# attachbottom

### Description
Newly created windows are placed at the bottom of the client tile stack.

### Download
- [git branch](https://codeberg.org/bencc/dwl/src/branch/attachbottom)
- [2024-05-16](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/attachbottom/attachbottom.patch)

### Authors
- [Ben Collerson](https://codeberg.org/bencc)
- [Aurel Weinhold](https://github.com/AurelWeinhold)

---
# attachtop

### Description
This is a port of attachtop patch for dwm: https://dwm.suckless.org/patches/attachtop

New client attaches below the last master/on top of the stack.

Behavior feels very intuitive as it doesn't disrupt existing masters no matter the amount of them, it only pushes the clients in stack down.

### Download
- [git branch](https://codeberg.org/nikitaivanov/dwl/src/branch/attachtop)
- [2024-04-23](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/attachtop/attachtop.patch)

### Authors
- [Nikita Ivanov](https://codeberg.org/nikitaivanov)

---
# autostart

### Description
Allow dwl to execute commands from autostart array in your config.h file. And when you exit dwl all processes from autostart array will be killed.

Note: Commands from array are executed using execvp(). So if you need to execute shell command you need to prefix it with "sh", "-c" (change sh to any shell you like).

### Download
- [git branch](https://codeberg.org/sevz/dwl/src/branch/autostart)
- [2024-06-07](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/autostart/autostart.patch)
- [0.7](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/autostart/autostart-0.7.patch)

### Authors
- [sevz](https://codeberg.org/sevz)
- [Rayan Nakib](https://nakibrayan2.pages.dev/)
- [NFVblog](https://github.com/nf02)

---
# bar

### Description

Add a bar identical to dwm's bar.

To use a status-bar, you can pass in status text via stdin:
```
slstatus -s | dwl
```

### Dependencies
* tllist (build dependency, required & pulled automatically by fcft)
* fcft
* pixman

### Download
- [0.7](/dwl/dwl-patches/raw/branch/main/patches/bar/bar-0.7.patch))
- [0.6](/dwl/dwl-patches/raw/branch/main/patches/bar/bar-0.6.patch))

Below is a preview of the patch.

![bar patch preview](bar.png)

For colors, they are in `RRRR, GGGG, BBBB, AAAA` format due to inheriting the `pixman_color_t` type, an example for the color `0x282a36` would be `0x2828, 0x2a2a, 0x3636, 0xffff`

### Authors
- [sewn](https://codeberg.org/sewn)

### Credits
- [MadcowOG](https://github.com/MadcowOG)
- [kolumni](https://github.com/kolunmi/dwlb)


---
# bar-systray

### Description
Add a system tray next to the [bar](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/bar). Heed the warning, this is far from suckless ^^

![preview](systray.png)

### Dependencies
- GTK4
- [bar.patch](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/bar) as mentioned.
- [gtk4-layer-shell](https://github.com/wmww/gtk4-layer-shell)
- [statusnotifier-systray-gtk4](https://codeberg.org/janetski/statusnotifier-systray-gtk4) built as a static library.

### Applying the patch
The patch applies on top of the bar patch. That needs to be applied first.

The patch creates subdirectories `lib` and `include`. After patching, but before `make`, install
`libstatusnotifier-systray-gtk4.a` and `snsystray.h` from statusnotifier-systray-gtk4 in the
directories. One possible way to do that:

1. Clone [https://codeberg.org/janetski/statusnotifier-systray-gtk4](https://codeberg.org/janetski/statusnotifier-systray-gtk4). Can clone to any location.
2. From statusnotifier-systray-gtk4 root:
    1. `$ meson setup --default-library=static --prefix=/ -Dgir=false -Dvala=false -Ddocs=false build`
    2. `$ meson compile -C build`
    3. `$ DESTDIR=$DWLDIR meson install -C build`, where $DWLDIR is the path to dwl root.
3. Finally, from dwl root, run `make`.

### Download
- [git branch](/janetski/dwl/src/branch/0.7-systray)
- [0.7](/dwl/dwl-patches/raw/branch/main/patches/bar-systray/bar-systray-0.7.patch)

### Authors
- [janetski](https://codeberg.org/janetski) ([.vetu](https://discordapp.com/users/355488216469471242) on discord)

---
# barborder

### Description

Add a border around the [bar](/dwl/dwl-patches/wiki/bar) similar to how a client is given a border.

### Download
- [0.7](/dwl/dwl-patches/raw/branch/main/patches/barborder/barborder.patch)

### Authors
- [sewn](https://codeberg.org/sewn)


---
# barcolors

### Description
Add support for colored status text to the [bar](/dwl/dwl-patches/src/branch/main/patches/bar). Text can be colored in the same manner as with dwlb, namely by wrapping it between `^fg(color)` and `^fg()` or `^bg(color)` and `^bg()`, where `color` is a 6-digit hexadecimal value.

### Download
- [git branch](/kerberoge/dwl/src/branch/barcolors)
- [0.7](/dwl/dwl-patches/raw/branch/main/patches/barcolors/barcolors.patch)

### Authors
- [kerberoge](https://codeberg.org/kerberoge)

---
# barheight

### Description

Adds the ability to change the [bar's](https://codeberg.org/dwl/dwl-patches/wiki/bar) height.

### Download
- [0.7](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/barheight/barheight.patch) (bar 0.7)
- [git branch](https://codeberg.org/Oak/dwl/src/branch/barheight)

### Authors
- [Oak](https://codeberg.org/oak)


---
# barpadding

### Description

Add vertical and horizontal space between the [bar](/dwl/dwl-patches/wiki/bar) and the edge of the screen.

### Download
- [0.7](/dwl/dwl-patches/raw/branch/main/patches/barpadding/barpadding.patch)

### Authors
- [sewn](https://codeberg.org/sewn)


---
# borders

### Description
Adds 2 more borders to each side (top, bottom, left, right) of every window.



<details>
<summary>Preview</summary>
<pre>
With the following config:

```c
static const unsigned int borderpx         = 9;  /* border pixel of windows */
static const unsigned int borderspx        = 3;  /* width of the border that start from outside the windows */
static const unsigned int borderepx        = 3;  /* width of the border that start from inside the windows */
```

and `border_color_type` set to `BrdOriginal`:
<img src="https://i.imgur.com/msead2K.png"/>

and `border_color_type` set to `BrdStart`:
<img src="https://i.imgur.com/ssgPG36.png"/>

and `border_color_type` set to `BrdEnd`:
<img src="https://i.imgur.com/i2Xtjy6.png"/>

and `border_color_type` set to `BrdStartEnd`:
<img src="https://i.imgur.com/fnkitdR.png"/>
</pre>
</details>

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/borders)
- [2024-06-04](https://codeberg.org/dwl/dwl-patches/raw/commit/1a6825f2b8cd23044312c8040d0bf63ee7f85bc5/patches/borders/borders.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/borders/borders.patch)

### Authors
- [wochap](https://codeberg.org/wochap)

---
# bottomstack

### Description
bstack and bstackhoriz are two stack layouts for dwl.
### Scheme
```
bstack        (TTT)       bstackhoriz   (===)
+-----------------+       +-----------------+
|                 |       |                 |
|                 |       |                 |
|                 |       |                 |
+-----+-----+-----+       +-----------------+
|     |     |     |       +-----------------+
|     |     |     |       +-----------------+
+-----+-----+-----+       +-----------------+
```


### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.6-b/bottomstack)
- [2024-07-09](https://codeberg.org/dwl/dwl-patches/raw/commit/20de07dc8759200c8a4c9651475acb331d245890/patches/bottomstack/bottomstack.patch)
- [2024-04-11](https://codeberg.org/dwl/dwl-patches/raw/commit/0f4e40fee49d1b8b430778e241b29496ae3b3b70/bottomstack/bottomstack.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/5368aa392c7ebf8d7d24c232b80cfae1be457d41/bottomstack/bottomstack.patch)

### Authors
- [wochap](https://codeberg.org/wochap)
- [DanielMowitz](https://github.com/DanielMowitz)
- [Abanoub8](https://github.com/Abanoub8)


---
# buttonbystate

### Description
Adds "state" (`enum wlr_button_state`) to configure a button action on either press or release.
This basically enables release to be used for button actions.

### Download
- [git branch](https://codeberg.org/nullsystem/dwl/src/branch/main_buttonbystate)
- [2024-04-06](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/buttonbystate/buttonbystate.patch)

### Authors
- [nullsystem](https://codeberg.org/nullsystem)

---
# center-terminal

### Description
Add a keybinding that toggles centering the terminally horizontally when
it's the only window, while still tiling multiple windows.

This limits the width of long text making it easier to read, and avoids
covering the wallpaper more than necessary.

### Download
- [git branch](https://codeberg.org/guidocella/dwl/src/branch/center-terminal)
- [2024-02-06](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/center-terminal/center-terminal.patch)

### Authors
- [Guido Cella](https://codeberg.org/guidocella)

---
# centeredmaster

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
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/centeredmaster)
- [2024-04-11](https://codeberg.org/dwl/dwl-patches/raw/commit/b104a580a80ebaf9f7e8917fe574e3e97ddd019a/centeredmaster/centeredmaster.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/0f4e40fee49d1b8b430778e241b29496ae3b3b70/centeredmaster/centeredmaster.patch)

### Authors
- [wochap](https://codeberg.org/wochap)
- [Nikita Ivanov](https://github.com/NikitaIvanovV)

---
# cfact

### Description
A port of the [dwm cfacts patch](https://dwm.suckless.org/patches/cfacts/) (with the limits removed)

Clients with higher weight are allocated more space!
```
+---------------------+
|          |   0.5    |
|   1.0    +----------+
+----------+          |
|          |   1.0    |
|          +----------+
|   2.0    |          |
|          |   1.0    |
+----------+----------+`
```
### Download
- [git branch](https://codeberg.org/Palanix/dwl/src/branch/cfact)
- [v0.7](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/cfact/cfact-v0.7.patch)
- [v0.6](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/cfact/cfact-v0.6.patch)
- [2024-02-15](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/cfact/cfact.patch)

### Authors
- [Palanix](https://codeberg.org/Palanix)

---
# cfact-centeredmaster

### Description
Port of the cfact patch for the centeredmaster layout. 

Inspired by the original patch for dwm (https://dwm.suckless.org/patches/cfacts/)

This patch requires both [cfact](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/cfact) and [centeredmaster](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/centeredmaster) patches.

### Download

 - [2024-06-26](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/cfact-centeredmaster/cfact-centeredmaster.patch)

### Authors
- [acadmendes](https://codeberg.org/acadmendes)

---
# chainkeys

### Description
Implements chained keybindings (like the dwm
[keychain](https://dwm.suckless.org/patches/keychain/) patch).

Bindings can share a leading chain key. This chain key will be triggered when
Mod+chain is pressed. A subsequent keypress will be matched against bindings
for that chain key. If it is configured the action will be triggered, otherwise
the keypress will be ignored.

### Download
- [git branch](https://codeberg.org/bencc/dwl/src/branch/chainkeys)
- [2024-05-20](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/chainkeys/chainkeys.patch)

### Authors
- [Ben Collerson](https://codeberg.org/bencc)

---
# client-opacity

### Description
This patch adds default transparency parameters to config.h which specify the starting transparencies of all windows.

It also adds opacities to the ruleset, enabling override of the opacities on a per client basis.

Additionally, it adds some shortcuts:
```
[MODKEY]+[o]         -> increase focus opacity of currently focused window
[MODKEY]+[Shift]+[o] -> decrease focus opacity of currently focused window
```


### Download
- [git branch](https://codeberg.org/sevz/dwl/src/branch/client-opacity)
- [2024-06-07](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/client-opacity/client-opacity.patch)

### Authors
- [sevz](https://codeberg.org/sevz)

---
# column

### Description
A column layout patch. This patch just puts the visible clients into equal-width columns on the screen.

### Download
- [git branch](https://codeberg.org/bencc/dwl/src/branch/column)
- [2024-01-02](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/column/column.patch)

### Authors
- [Ben Collerson](https://codeberg.org/bencc)
---
# coredump

### Description
Generate a coredump if dwl exited abnormally (to be more usefull you need to
compile dwl and wlroots with debug symbols)

### Download
- [git branch](https://codeberg.org/sevz/dwl/src/branch/coredump)
- [main 2024-09-01](/dwl/dwl-patches/raw/branch/main/patches/coredump/coredump.patch)
- [coredump-0.7.patch](/dwl/dwl-patches/raw/branch/main/patches/coredump/coredump-0.7.patch)

### Authors
- [sevz](https://codeberg.org/sevz)

---
# cursortheme

### Description
Adds ability to change cursor's theme and size.

```c
static const char *cursor_theme            = NULL;
static const char cursor_size[]            = "24"; /* Make sure it's a valid integer, otherwise things will break */
```

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/cursortheme)
- [2024-07-09](https://codeberg.org/dwl/dwl-patches/raw/commit/13d96b51b54500dd24544cf3a73c61b7a1414bc6/patches/cursortheme/cursortheme.patch)
- [2024-04-11](https://codeberg.org/dwl/dwl-patches/raw/commit/b828e21717fa584affeb3245359c3ab615759fa4/cursortheme/cursortheme.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/c676de59d51e613bd52ac46c77a24b1cac9a61a1/cursortheme/cursortheme.patch)

### Authors
- [wochap](https://codeberg.org/wochap)
- [egorguslyan](https://github.com/egorguslyan)

---
# customfloat

### Description
Rules for floating windows support default x, y, width, height. Defaults to the center of the screen and the client size.

If the width or height is less than or equal to 1, then the value will be interpreted as a percentage. For example, 0.5 represents 50%, 0.25 represents 25%, and 1 represents 100%. **NOTE**: Some clients, like Thunar, have minimum width/height

The variable `center_relative_to_monitor` allows the user to choose whether to center relative to the monitor or relative to the window area.

<details>
<summary>Explanation of center_relative_to_monitor:</summary>
<pre>
The "Monitor area" refers to the space enclosed by the green rectangle, while the "Window area" refers to the space enclosed by the red rectangle.
<img src="https://i.imgur.com/xhejzPh.png"/>
</pre>
</details>

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/customfloat)
- [2024-07-09](https://codeberg.org/dwl/dwl-patches/raw/commit/13d96b51b54500dd24544cf3a73c61b7a1414bc6/patches/customfloat/customfloat.patch)
- [2024-04-11](https://codeberg.org/dwl/dwl-patches/raw/commit/98cba933c9f4099202e54f39acbf17e05bde828a/customfloat/customfloat.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/bf098459219e7a473d8edb4c0435aeb6a4b82e38/customfloat/customfloat.patch)

### Authors
- [wochap](https://codeberg.org/wochap)
- [Stivvo](https://github.com/Stivvo)

---
# deck

### Description
Adds a layout with a monocle layout for clients in the stack (port of the [deck layout for dwm](https://dwm.suckless.org/patches/deck/)); stacked clients are like a deck of cards (see below)

```
Tile:
+-----------------+--------+
|                 |        |
|                 |  S1    |
|                 |        |
|        M        +--------+
|                 |        |
|                 |   S2   |
|                 |        |
+-----------------+--------+

Deck:
+-----------------+--------+
|                 |        |
|                 |        |
|                 |        |
|        M        |   S1   |
|                 |        |
|                 |        |
|                 |        |
+-----------------+--------+
```

### Download
- [git branch](https://codeberg.org/anabasis/dwl/src/branch/deck)
- [2024-05-10](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/deck/deck.patch)

### Authors
- [anabasis](https://codeberg.org/anabasis)
- [Palanix](https://codeberg.org/Palanix)

---
# define-modkey-with-make-argument

### Description
This patch adds the ability to define the modkey with a make argument like so:

```
make MODKEY=WLR_MODIFIER_ALT
make MODKEY=WLR_MODIFIER_LOGO
make MODKEY=WLR_MODIFIER_CTRL
make MODKEY=WLR_MODIFIER_SHIFT
```

It can be used to compile multiple times quickly, you can also have a main session and sub session with different modkeys.

### Download
- [git branch](https://codeberg.org/Abanoub/dwl/src/branch/define-modkey-patch)
- [2024-02-14](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/define-modkey-with-make-argument/define-modkey-with-make-argument.patch)

### Authors
- [Abanoub](https://codeberg.org/Abanoub)

---
# dim-unfocused

### Description
Implements dimming of clients which are unfocused.

The code also allows any color dimming. There is also an additional option in `Rule`, which allows you to keep the client `neverdim`, that is, as if it is focused.

There are also two functions that can be bound to a `Key` or `Button`, 
1. `toggledimming`: Which toggles dimming for all windows (except for `Rule`s)
2. `toggledimmingclient`: Which toggles dimming for the focused window, as if the client had `neverdim` applied to it. This overwrites an applied `Rule`.

### Download
- [2024-09-03](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/dim-unfocused/dim-unfocused.patch)
- [2024-07-14](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/dim-unfocused/dim-unfocused-20240714.patch)
- [2024-05-16](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/dim-unfocused/dim-unfocused-20240516.patch)
- [2024-04-16](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/dim-unfocused/dim-unfocused-20240416.patch)
- [git branch](https://codeberg.org/dhruva_sambrani/dwl/src/branch/dim-unfocused)

### Authors
- [Dhruva Sambrani](https://codeberg.org/dhruva_sambrani)

---
# dragmfact

### Description
Change mfact by dragging the mouse.

### Download
- [git branch](https://codeberg.org/Palanix/dwl/src/branch/dragmfact)
- [v0.7](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/dragmfact/dragmfact-v0.7.patch)
- [v0.6](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/dragmfact/dragmfact-v0.6.patch)
- [2024-02-16](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/dragmfact/dragmfact.patch)

### Authors
- [Palanix](https://codeberg.org/Palanix)

---
# dragresize

### Description
implement rio-like window resizing

select window to resize (mod+middleclick by default) then drag out an area for it to occupy

### Download
- [git branch](https://codeberg.org/notchoc/dwl/src/branch/dragresize)
- [2024-07-10](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/dragresize/dragresize.patch)
- [2024-06-19](https://codeberg.org/dwl/dwl-patches/raw/commit/8c75e6dbc1728bf70d42547222464f496d9ea613/patches/dragresize/dragresize.patch)

### Authors
- [notchoc](https://codeberg.org/notchoc)

---
# en-keycodes

### Description
Always use the English keymap to get keycodes, so key bindings work even when using a non-English keyboard layout.

### Download
- [git branch](https://codeberg.org/ForzCross/dwl/src/branch/en-keycodes.patch)
- [2024-01-11](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/en-keycodes/en-keycodes.patch)

### Authors
- [ForzCross](https://codeberg.org/ForzCross)
- [Nikita Ivanov](https://github.com/NikitaIvanovV)
- [dimkr](https://codeberg.org/dimkr) (<dima@dimakrasner.com>)

---
# envcfg

### Description
Input device configuration (click method, tap-and-drag, acceleration, etc), border size and colors via environment variables.

### Download
- [2024-02-11](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/envcfg/envcfg.patch)

### Authors
- [Dima Krasner](https://codeberg.org/dimkr) (<dima@dimakrasner.com>)

---
# fakefullscreenclient

### Description
Allow setting fake fullscreen per client

### Download
- [git branch](https://codeberg.org/notchoc/dwl/src/branch/fakefullscreenclient)
- [2024-03-29](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/fakefullscreenclient/fakefullscreenclient.patch)
### Authors
- [notchoc](https://codeberg.org/notchoc)

---
# fallback

### Description
Tries a different display mode if the preferred mode doesn't work.

### Download
- [2024-02-11](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/fallback/fallback.patch)

### Authors
- [Dima Krasner](https://codeberg.org/dimkr) (<dima@dimakrasner.com>)

---
# float-unfocused-border-color

### Description
A revive of the floatBorderColor patch.

This patch allows you to set a color for floating windows when they are unfocused.

### Download
- [git branch](https://codeberg.org/yuki-was-taken/dwl-patch/src/branch/float-unfocused-border-color/)
- [2024-06-07](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/float-unfocused-border-color/float-unfocused-border-color.patch)

### Authors
- [yuki](https://codeberg.org/yuki-was-taken)
- [Palanix (Original Author)](https://codeberg.org/Palanix)

---
# focusdir

### Description
Focus the window to the left, right, above or below the current focused window

### Download
- [git branch](https://codeberg.org/ldev105/dwl/src/branch/focusdir)
- [2023-01-22](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/focusdir/focusdir.patch)

### Authors
- [ldev105](https://codeberg.org/ldev105)

---
# foreign-toplevel-management

### Description
Implement `foreign-toplevel-management`, it add handlers for activate, close, fullscreen and destroy request events, it's missing minimize and maximize request handlers.

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.6-a/foreign-toplevel-management)
- [2024-05-02](https://codeberg.org/dwl/dwl-patches/raw/commit/e58c3ec41a39df934d2998161d7187ac965ea77a/foreign-toplevel-management/foreign-toplevel-management.patch)

### Authors
- [wochap](https://codeberg.org/wochap)
---
# gaplessgrid

### Description
Arranges windows in a grid. Except it adjusts the number of windows in the first few columns to avoid empty cells.

### Download
- [2024-07-14](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/gaplessgrid/gaplessgrid.patch)
- [2023-08-01](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/gaplessgrid/gaplessgrid-20230801.patch)
- [git branch](https://codeberg.org/dhruva_sambrani/dwl/src/branch/gaplessgrid)

## Pre-codeberg
- [2023-11-14](https://github.com/djpohly/dwl/compare/main...Sneethe:gaplessgrid.patch)
- [2021-07-27](https://github.com/djpohly/dwl/compare/main...vnepogodin:gaplessgrid.patch)

### Authors
- [Sneethe](https://github.com/Sneethe/)
- [Vladislav Nepogodin](https://github.com/vnepogodin)
- [Dhruva Sambrani](https://codeberg.org/dhruva_sambrani/) (Revived to codeberg)

---
# gaps

### Description
Adds gaps between clients, providing the ability to disable them at run-time. 

`smartgaps` can also be changed to remove gaps when there is only one client present.

### Download
- [git branch](https://codeberg.org/bigman/dwl/src/branch/gaps)
- [2024-07-12](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/gaps/gaps.patch)

### Authors
- [peesock](https://codeberg.org/bigman)
- [sewn](https://codeberg.org/sewn)
- [Serene Void](https://github.com/serenevoid)
- [Rayan Nakib](https://nakibrayan2.pages.dev)

---
# gestures

### Description
Add swipe gestures to trigger functions, similar to [libinput-gestures](https://github.com/bulletmark/libinput-gestures/tree/master). It supports the following gestures: `SWIPE_UP`, `SWIPE_DOWN`, `SWIPE_LEFT` and `SWIPE_RIGHT`

> NOTE: It requires that you have previously applied [pointer-gestures-unstable-v1](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/pointer-gestures-unstable-v1)

```c
static const Gesture gestures[] = {
  /* modifier gesture       fingers_count   function    argument */
  { MODKEY,   SWIPE_LEFT,   4,              shiftview,  { .i = 1 } },
  { 0,        SWIPE_RIGHT,  4,              shiftview,  { .i = -1 } },
};
```

**NOTE:** the example above requires the following patch [shiftview](https://codeberg.org/dwl/dwl-patches/wiki/shiftview)

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/gestures)
- [2024-07-09](https://codeberg.org/dwl/dwl-patches/raw/commit/13d96b51b54500dd24544cf3a73c61b7a1414bc6/patches/gestures/gestures.patch)
- [2024-04-11](https://codeberg.org/dwl/dwl-patches/raw/commit/be3735bc6a5c64ff76c200a8679453bd179be456/gestures/gestures.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/655fd2916c1bcaa022ce6dcdfb370051cf64df66/gestures/gestures.patch)

### Authors
- [wochap](https://codeberg.org/wochap)

---
# globalkey

### Description
This patch adds ability to pass specified in config header keys globally, somewhat in hyprlands approach.
This might deal with waylands lack of global shortcuts.

Example:
```
static const PassKeypressRule pass_rules[] = {
	ADDPASSRULE("com.obsproject.Studio", MODKEY, XKB_KEY_Home),
	ADDPASSRULE("discord", 0, XKB_KEY_n),
    /* xkb key is case ignored */
};
```
will pass `MODKEY + Home` key to obs(flatpak version) regardless of what client is currently focused if any.
String "com.obsproject.Studio" should be exact match for appid of the client. To get appid use [dwlmsg](https://codeberg.org/notchoc/dwlmsg),
or run stock dwl from a terminal then launch the needed application inside, dwl will print all the info to the stdout.

Note that if popup (like [fuzzel](https://codeberg.org/dnkl/fuzzel)) is focused, no key will be globally passed.
This is done so these menus don't get closed after hitting some of the global keys.


### Download
- [git branch](https://codeberg.org/korei999/dwl/src/branch/globalkey)
- [2024-06-08](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/globalkey/globalkey.patch)
### Authors
- [korei999](https://codeberg.org/korei999)

---
# headless

### Description
Implements `swaymsg create_output` command, it allows you to create virtual/headless outputs. But in combination with a VNC server (for example wayvnc), this allows you to essentially have additional monitors, by connecting to the VNC server with an appropiate client (for example on an tablet or laptop).

If you plan to use wayvnc, you'll need [virtual-pointer](https://codeberg.org/dwl/dwl-patches/wiki/virtual-pointer.-) patch as well 

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/v0.5/headless)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/0096e49402bc59b4050e12cdb9befb79d0011006/headless/headless.patch)

### Authors
- [wochap](https://codeberg.org/wochap)
---
# hide-behind-fullscreen

### Description
Hide all clients (and layer surfaces) behind the current client if it is
fullscreen, only the background  (layer surfaces at the background layer) will
be shown

### Download
- [git branch](https://codeberg.org/sevz/dwl/src/branch/hide-behind-fullscreen)
- [main 2024-09-01](/dwl/dwl-patches/raw/branch/main/patches/hide-behind-fullscreen/hide-behind-fullscreen.patch)
- [hide-behind-fullscreen-0.7.patch](/dwl/dwl-patches/raw/branch/main/patches/hide-behind-fullscreen/hide-behind-fullscreen-0.7.patch)

### Authors
- [sevz](https://codeberg.org/sevz)

---
# hide-behind-monocle

### Description
Hide all clients behind the focused one in the monocle layout

### Download
- [git branch](https://codeberg.org/sevz/dwl/src/branch/hide-behind-monocle)
- [main 2024-09-01](/dwl/dwl-patches/raw/branch/main/patches/hide-behind-monocle/hide-behind-monocle.patch)
- [hide-behind-monocle-0.7.patch](/dwl/dwl-patches/raw/branch/main/patches/hide-behind-monocle/hide-behind-monocle-0.7.patch)

### Authors
- [sevz](https://codeberg.org/sevz)

---
# hide_vacant_tags

### Description

Prevent [bar](/dwl/dwl-patches/wiki/bar) from drawing tags with no clients (i.e. vacant).
It also stops drawing empty rectangles on the bar for non-vacant tags as there is no need anymore to distinguish vacant tags and it offers a more visible contrast than if there were filled/empty rectangles.

### Download
- [0.7](/dwl/dwl-patches/raw/branch/main/patches/hide_vacant_tags/hide_vacant_tags.patch)

### Authors
- [sewn](https://codeberg.org/sewn)


---
# hiderule

### Description
Adds a `ishidden` option to client rules, that allows hiding any matching clients entirely.

### Download
- [git branch](https://codeberg.org/minego/dwl/src/branch/hiderule)
- [yyyy-mm-dd](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/hiderule/hiderule.patch)

### Authors
- [minego](https://codeberg.org/minego)
---
# inputdevicerules

### Description
Input device rules implemented using custom device create functions for
keyboards and pointing devices.

Examples provided:

- ignore unwanted input devices
- configure a toggle input device
- exclude certain keyboards (eg ydotool) from keyboard group

### Download
- [git branch](https://codeberg.org/bencc/dwl/src/branch/inputdevicerules)
- [2024-06-21](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/inputdevicerules/inputdevicerules.patch)

### Authors
- [Ben Collerson](https://codeberg.org/bencc)

---
# ipc

### Description
Largely based on [raphi](https://sr.ht/~raphi/)'s [somebar](https://sr.ht/~raphi/somebar/), this patch provides an ipc for wayland clients to get and set dwl state. The ipc is intended for status bars, but can also be scripted with tools like [dwlmsg](https://codeberg.org/notchoc/dwlmsg).

Status information to stdout is currently disabled as dwl tends to freeze. For now, `dwlmsg -w` should act as a drop-in replacement.

Note to [pertag](../pertag/) users: apply [this](./ipcpertag.patch) for ipc tagsetting to work as expected

### Download
- [git branch](https://codeberg.org/notchoc/dwl/src/branch/ipc)
- [2024-08-16](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/ipc/ipc.patch)
- [2024-07-29](https://codeberg.org/dwl/dwl-patches/raw/commit/d235f0f88ed069eca234da5a544fb1c6e19f1d33/patches/ipc/ipc.patch) don't focus other outputs (apply [this minipatch](./focus-tagset-output.patch) if you'd prefer that)
- [2024-07-16](https://codeberg.org/dwl/dwl-patches/raw/commit/642b2559d522034785c1c1203c6d426855ec19ca/patches/ipc/ipc.patch)
- [2024-06-30](https://codeberg.org/dwl/dwl-patches/raw/commit/9a751e5020133d3ab9219e68a43109c6f3c931a7/patches/ipc/ipc.patch)
- [2024-06-21](https://codeberg.org/dwl/dwl-patches/raw/commit/f96ee44cbaef06bd38b8fa29ac7ecba8b1b5abd5/patches/ipc/ipc.patch)
- [2024-06-19](https://codeberg.org/dwl/dwl-patches/raw/commit/e69afc7263b8d982a7923e5d4910f2e1f7140bb8/patches/ipc/ipc.patch)
- [2024-06-08](https://codeberg.org/dwl/dwl-patches/raw/commit/f8598a91b44acc3bd7e9041be97265bbce8fa219/patches/ipc/ipc.patch)
- [2024-03-13](https://codeberg.org/dwl/dwl-patches/raw/commit/0150cfebbcd85f2d6e6728afad345a11a0c45947/ipc/ipc.patch)
- [2024-02-20](https://codeberg.org/dwl/dwl-patches/raw/commit/0c5ae06e4bc1d7f641376e8fcb86b43bd48ce2ee/ipc/ipc.patch)
- [2023-10-28](https://gist.githubusercontent.com/fbushstone/b116c44340eb7a7878de1119dd931ca5/raw/ee66ac9e2a5dddd9b528df553e21080c2811e974/ipc-v2-fixed.patch) Updated version of 2023-04-29, prevents ipc from freezing the compositor in printstatus.
- [2023-04-29](https://github.com/djpohly/dwl/compare/main...madcowog:ipc-v2.patch) Use this for dwl-ipc-unstable-v2. If you are using commit [9d68554](https://github.com/djpohly/dwl/commit/9d68554c59a886b641d27a364884fb461af2d4f1) or later, use this. For status bars this protocol is supported by dwlb, Waybar and dwl-bar.
- [2023-04-29](https://github.com/djpohly/dwl/compare/main...madcowog:ipc-bbdf2.patch) Use this for dwl-ipc-unstable-v1. If you are using commit [bbdaf2a9](https://github.com/djpohly/dwl/commit/bbdf2a913b72e7a308ee0dfde6518a4285d4a775), [release 0.4](https://github.com/djpohly/dwl/releases/tag/v0.4) or earlier, use this. For status bars, this protocol is supported by dwl-bar.
- [2023-02-20](https://lists.sr.ht/~raphi/public-inbox/patches/39166) Use this for net-tapesoftware-dwl-wm-unstable-v1. If you are using commit [c69a2bec](https://github.com/djpohly/dwl/commit/c69a2bec3ff417fbc4ea8fec0a49096773e01e7d) or later, use this. For status bars this protocol is supported by somebar.

### Authors
- [MadcowOG](https://github.com/MadcowOG)
- [fbushstone](https://github.com/fbushstone)
- [notchoc](https://codeberg.org/notchoc)
- [snuk](https://codeberg.org/snuk)

---
# kblayout

### Description
This patch adds per-client keyboard layout and ability to send current
keyboard layout information to a status bar.

Only per-client feature is enabled by default. You can edit
`kblayout_file` and `kblayout_cmd` variables to notify a status bar
about keyboard layout.

[Someblocks](https://sr.ht/~raphi/someblocks) config that works
with the example settings in `config.h`:

```c
static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
	{"", "cat /tmp/dwl-kblayout",					0,		1},
};
```

Both of these features are included in one patch because their
implementation happens to share some code. If you don't need
any of these features, just disable it in `config.h`.

### Download
- [2024-06-01](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/kblayout/kblayout.patch)

### Authors
- [ForzCross](https://codeberg.org/ForzCross)
- [Nikita Ivanov](https://github.com/NikitaIvanovV)

---
# keyboardshortcutsinhibit

### Description
Allows clients to use the keyboard-shortcuts-inhibit protocol to block the compositor from using keybinds. This is useful for virtualization software like looking-glass which requires this protocol to run.

### Download
- [git branch](https://codeberg.org/Rutherther/dwl/src/branch/patch/keyboard-shortcuts-inhibit)
- [2024-05-10](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/keyboardshortcutsinhibit/keyboardshortcutsinhibit.patch)
- [2023-05-01](https://github.com/djpohly/dwl/compare/main...madcowog:keyboard-shortcuts-inhibit.patch)

### Authors
- [Rutherther](https://codeberg.org/Rutherther)
- [MadcowOG](https://github.com/MadcowOG)

---
# keycodes

### Description
Use keycodes instead of keysyms. This way, input is independent from keyboard
layout (you can use the keys.h file to customize, or get the keycodes with
`wev` or `xkbcli interactive-wayland` (x11-libs/libxkbcommon[tools] in gentoo)).

### Download
- [git branch](https://codeberg.org/sevz/dwl/src/branch/keycodes)
- [main 2024-09-01](/dwl/dwl-patches/raw/branch/main/patches/keycodes/keycodes.patch)
- [keycodes-0.7.patch](/dwl/dwl-patches/raw/branch/main/patches/keycodes/keycodes-0.7.patch)

### Config after patching 
(run in DWL source directory)
```
export XKB_DEFAULT_VARIANT=yourbestkeyboardlayout
cc -lxkbcommon -o generate-keys generate-keys.c
./generate-keys
```

### Authors
- [sevz](https://codeberg.org/sevz)

---
# less-simple-touch-input

### Description
Adds touchscreen functionality.

This patch was based on the [simple-touch-input](https://codeberg.org/dwl/dwl-patches/wiki/simple-touch-input) but instead of emulating mouse movement, this now forwards the appropriate event notifications to clients.

KNOWN BUGS:
- Sometimes, the pointer moves to where the screen is pressed, but the button press doesn't occur until the screen is touched AGAIN. This means that if you touch to click button 'Q' on the screen (for instance), nothing happens; then you touch elsewhere on the screen and THEN button 'Q' registers a click. This is annoying, doesn't always happen, and I don't yet know how to fix it.

### Download
- [git branch](https://codeberg.org/minego/dwl/src/branch/touch)
- [2024-03-26](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/less-simple-touch-input/less-simple-touch-input.patch)

### Authors
- [minego](https://codeberg.org/minego)
- [fauxmight](https://codeberg.org/fauxmight)
- [Unprex](https://github.com/Unprex)

### Changelog
- 2024-02-11 Corrected issue where motion events where not sending notifications for unfocused clients such as an on screen keyboard
- 2024-03-26 Rebased, and removed #ifdef's for the pointer constraints patch which has been merged into upstream
- 2024-03-28 Removed debug
---
# limitnmaster

### Description
Limits nmaster to within the range of currently-opened windows (nmaster will not change past the full horizontal split layout)

### Download
- [git branch](https://codeberg.org/dev-gm/dwl/src/branch/limitnmaster)
- [2024-03-15](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/limitnmaster/limitnmaster.patch)

### Authors
- [dev-gm](https://codeberg.org/dev-gm)
---
# lockedkeys

### Description
This patch allows you to add keybindings to the lockscreen.

```c
static const Key lockedkeys[] = {
	/* Note that Shift changes certain key codes: c -> C, 2 -> at, etc. */
	/* modifier                  key                 function        argument */

	/* Ctrl-Alt-Backspace and Ctrl-Alt-Fx used to be handled by X server */
	{ WLR_MODIFIER_CTRL|WLR_MODIFIER_ALT,XKB_KEY_Terminate_Server, quit, {0} },
#define CHVT(n) { WLR_MODIFIER_CTRL|WLR_MODIFIER_ALT,XKB_KEY_XF86Switch_VT_##n, chvt, {.ui = (n)} }
	CHVT(1), CHVT(2), CHVT(3), CHVT(4), CHVT(5), CHVT(6),
	CHVT(7), CHVT(8), CHVT(9), CHVT(10), CHVT(11), CHVT(12),
};
```

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/lockedkeys)
- [2024-04-11](https://codeberg.org/dwl/dwl-patches/raw/commit/fc4146f3068dcd46035a2a11fe9d6109a97ae6d6/lockedkeys/lockedkeys.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/2a6560c167e5c9afc5598ac5431d23d90de8846c/lockedkeys/lockedkeys.patch)

### Authors
- [wochap](https://codeberg.org/wochap)

---
# mastercolumn

### Description
This patch adds a layout, `mastercol`, in which the windows in the master area are arranged in columns of equal size. The number of columns is always nmaster + 1, and the last column is a stack of leftover windows (as in the normal tile layout). It effectively differs from the default tile layout only in that master windows are arranged horizontally rather than vertically.

For gaps, apply `mastercolumn-gaps.patch` on top of `mastercolumn.patch` and `gaps.patch`.

### Download
##### `mastercolumn.patch`
- [git branch](/shivers/dwl/src/branch/mastercolumn)
- [0.7](/dwl/dwl-patches/raw/branch/main/patches/mastercolumn/mastercolumn.patch)

##### `mastercolumn-gaps.patch`
- [git branch](/shivers/dwl/src/branch/mastercolumn-gaps)
- [0.7](/dwl/dwl-patches/raw/branch/main/patches/mastercolumn/mastercolumn-gaps.patch)

### Authors
- [shivers](https://codeberg.org/shivers)

---
# menu

### Description

This patch adds `menu` command, which allows dwl to interface with dmenu-like programs.

By default, two menus are available:
- focusing a window by its title by pressing `Alt+o`
- selecting a layout from a list by pressing `Alt+Shift+o`

Edit `menus` array in `config.h` to add/change menus and use a different dmenu program.

### Download
- [git branch](https://codeberg.org/nikitaivanov/dwl/src/branch/menu)
- [2024-07-13](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/menu/menu.patch)

### Authors
- [Nikita Ivanov](https://github.com/NikitaIvanovV)

---
# meson

### Description
Add the meson build system.

This is useful for people who do not want to self-manage a wlroots installation.

To enable Xwayland support, you will need to enable it in the wlroots subproject:
```sh
meson setup -Dwlroots:xwayland=enabled build
```
It is also reccomended to see the wlroots meson project configuration logs for any
unusual checks, such as requiring `hwdata` for the DRM backend.

### Download
- [git branch](/sewn/dwl/src/branch/meson)
- [2024-08-27](/dwl/dwl-patches/raw/branch/main/patches/meson/meson.patch)

### Authors
- [sewn](/sewn)


---
# minimalborders

### Description
Dynamically adjusts the borders between adjacent windows to make them visually merge

**NOTE:** to disable minimalborders after applying this patch, set `draw_minimal_borders` to `0` 

```c
static const int draw_minimal_borders = 0; /* disable minimalborders */
```

<details>
<summary>Preview:</summary>
<pre>
with:

```c
static const unsigned int borderpx         = 10;  /* border pixel of windows */
```

Before applying the patch
<img src="https://i.imgur.com/VQfXCjp.png"/>

After applying the patch
<img src="https://i.imgur.com/I7s0Xkv.png"/>
</pre>
</details>

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/minimalborders)
- [2024-07-09](https://codeberg.org/dwl/dwl-patches/raw/commit/13d96b51b54500dd24544cf3a73c61b7a1414bc6/patches/minimalborders/minimalborders.patch)
- [2024-04-11](https://codeberg.org/dwl/dwl-patches/raw/commit/7a5c3420822074c544fa102e030b7c30aa6b6be8/minimalborders/minimalborders.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/be3735bc6a5c64ff76c200a8679453bd179be456/minimalborders/minimalborders.patch)

### Authors
- [wochap](https://codeberg.org/wochap)

---
# modes

### Description
Implement  modes, that way each mapping is associated with a mode and is only active while in that mode, default mode is `NORMAL`

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
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/modes)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/modes/modes.patch)

### Authors
- [wochap](https://codeberg.org/wochap)

---
# monfig

### Description
Allows more monitor configuration in config.h

### Download
- [git branch](https://codeberg.org/Palanix/dwl/src/branch/monfig)
- [2024-02-15](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/monfig/monfig.patch)

### Authors
- [Palanix](https://codeberg.org/Palanix)

---
# movecenter

### Description

> This patch is no longer being maintained by me [wochap](https://codeberg.org/wochap), since I'm now using a different patch specific to my use case: https://codeberg.org/wochap/dwl/src/branch/v0.6-c/betterfloat/betterfloat-diff.patch.

This patch provides a keybinding to center the focused floating window.

Press <kbd>MODKEY</kbd> + <kbd>x</kbd> to center the focused floating window.

It does NOT center windows that are not floating.

The variable `respect_monitor_reserved_area` allows the user to choose whether to center relative to the monitor or relative to the window area.

<details>
<summary>Explanation of respect_monitor_reserved_area:</summary>
<pre>
The "Monitor area" refers to the space enclosed by the green rectangle, while the "Window area" refers to the space enclosed by the red rectangle.
<img src="https://i.imgur.com/xhejzPh.png"/>
</pre>
</details>

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.6/movecenter)
- [v0.6](https://codeberg.org/dwl/dwl-patches/raw/commit/b1ca929ee645cd3e175f198e250448b54624acd6/patches/movecenter/movecenter.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/187d7f511572457750fcf6e42c99cdc7befe05e7/patches/movecenter/movecenter.patch)

### Authors
- [wochap](https://codeberg.org/wochap)


---
# moveresizekb

### Description
This allows the user to change size and placement of floating windows using only the keyboard, default keybindings: 

| Keybinding | Action |
| :--- | :--- |
| <kbd>MODKEY</kbd> + <kbd>Up</kbd> | move 40px up |
| <kbd>MODKEY</kbd> + <kbd>Down</kbd> | move 40px down |
| <kbd>MODKEY</kbd> + <kbd>Left</kbd> | move 40px left |
| <kbd>MODKEY</kbd> + <kbd>Right</kbd> | move 40px right |
| <kbd>MODKEY</kbd> + <kbd>Shift</kbd> + <kbd>Up</kbd> | shrink height 40px |
| <kbd>MODKEY</kbd> + <kbd>Shift</kbd> + <kbd>Down</kbd> | grow height 40px |
| <kbd>MODKEY</kbd> + <kbd>Shift</kbd> + <kbd>Left</kbd> | shrink width 40px |
| <kbd>MODKEY</kbd> + <kbd>Shift</kbd> + <kbd>Right</kbd> | grow width 40px |

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/moveresizekb)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/moveresizekb/moveresizekb.patch)

### Authors
- [wochap](https://codeberg.org/wochap)

---
# movestack

### Description
Allows you to move a window up and down the stack.

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/movestack)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/movestack/movestack.patch)

### Authors
- [wochap](https://codeberg.org/wochap)
- [sam-barr](https://github.com/ss7m)
- [Dmitry Zakharchenko](https://github.com/dm1tz)
- [Abanoub8](https://github.com/Abanoub8)
- [Nikita Ivanov](https://github.com/NikitaIvanovV)

---
# namedscratchpads

### Description
Allows for the creation of multiple scratchpad windows, each assigned to a different keybinding. In simple terms, it enables 'run or raise' functionality

This patch adds the following functions:

* `togglescratch`: simply toggles the scratchpad window
* `focusortogglescratch`: change the focus to the scratchpad window if it is visible and toggles it if it is already in focus
* `focusortogglematchingscratch`: similar to `focusortogglescratch` but also closes all other scratchpad windows

If you don't assign keybindings to any of the above functions and so get a compiler warning about them not being used, just remove them from your dwl branch to stop the warning.

### Download
- [git branch (v0.6)](https://codeberg.org/bencc/dwl/src/branch/namedscratchpads)
- [2024-07-13 (v0.6)](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/namedscratchpads/namedscratchpads.patch)

### Authors
- [Ben Collerson](https://codeberg.org/bencc)
- [wochap](https://codeberg.org/wochap)
- [Louis-Michel Raynauld](https://github.com/loumray)

---
# naturalscrolltrackpad

### Description
Set natural scrolling only for trackpads.

### Download
- [git branch](https://codeberg.org/neuromagus/dwl/src/branch/naturalscrolltrackpad)
- [2024-01-06](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/naturalscrolltrackpad/naturalscrolltrackpad.patch)

### Authors
- [Neuromagus](https://codeberg.org/neuromagus)
- [Nikita Ivanov](https://github.com/NikitaIvanovV)

---
# nextlayout

### Description
Change the current layout to the next available one.

### Download
- [0.7](/dwl/dwl-patches/raw/branch/main/patches/nextlayout/nextlayout.patch)

### Authors
- [sewn](/sewn)


---
# numlock-capslock

### Description
Allows activating numlock or capslock at startup.

### Download
- [git branch](https://codeberg.org/sevz/dwl/src/branch/numlock-capslock)
- [main 2024-09-02](/dwl/dwl-patches/raw/branch/main/patches/numlock-capslock/numlock-capslock.patch)
- [numlock-capslock.patch](/dwl/dwl-patches/raw/branch/main/patches/numlock-capslock/numlock-capslock-0.7.patch)

### Authors
- [sevz](https://codeberg.org/sevz)

---
# passthrough

### Description
allows pausing keybind handling

also allows for bitcarrying-esque control of nested instances

default keybind is Ctrl+Logo+Alt+Shift+Esc, can be customized in config.h

### Download
- [git branch](https://codeberg.org/notchoc/dwl/src/branch/passthrough)
- [2024-06-26](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/passthrough/passthrough.patch)
- [2024-06-22](https://codeberg.org/dwl/dwl-patches/raw/commit/3f44fb23d8cb6c7d700f41525dc00493e392083c/patches/passthrough/passthrough.patch)
### Authors
- [notchoc](https://codeberg.org/notchoc)

---
# perinputconfig

### Description
Replace the singular keyboard and pointer input configuration with an array allowing to set different variables matching by name.

Tip to find the names: Grep for `device_name` and add a line after it to print to stdout. Then run EX: `dwl > /tmp/print_device_names.log`, exit dwl, and should see the names.

### Download
- [git branch](https://codeberg.org/nullsystem/dwl/src/branch/main_perinputconfig)
- [2024-06-08](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/perinputconfig/perinputconfig.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/perinputconfig/perinputconfig-v0.5.patch)

### Authors
- [nullsystem](https://codeberg.org/nullsystem)

---
# pertag

### Description
Makes layout, mwfact and nmaster individual for every tag.

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.6/pertag)
- [v0.6](https://codeberg.org/dwl/dwl-patches/raw/commit/65ea99519bbf7a52f48932aea7385f81f8b30867/patches/pertag/pertag.patch)
- [2024-04-11](https://codeberg.org/dwl/dwl-patches/raw/commit/bf098459219e7a473d8edb4c0435aeb6a4b82e38/pertag/pertag.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/3f9a58cde9e3aa02991b3e5a22d371b153cb1459/pertag/pertag.patch)

### Authors
- [wochap](https://codeberg.org/wochap)
- [Guido Cella](https://github.com/guidocella)

---
# pointer-gestures-unstable-v1

### Description
Forward the following events to client:
swipe_begin, swipe_update, swipe_end, pinch_begin, pinch_update and pinch_end

This patch allows you to pinch zoom in Chrome, for example. In combination with the following patches [gestures](https://codeberg.org/dwl/dwl-patches/wiki/gestures) and [shiftview](https://codeberg.org/dwl/dwl-patches/wiki/shiftview), it would allow you to switch workspaces by performing a 3-finger swipe on your touchpad.


### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/pointer-gestures-unstable-v1)
- [2024-07-12](https://codeberg.org/dwl/dwl-patches/raw/commit/05dbce217b676e989b0fc9e0eecf83b386ac9e07/patches/pointer-gestures-unstable-v1/pointer-gestures-unstable-v1.patch)
- [2024-07-09](https://codeberg.org/dwl/dwl-patches/raw/commit/2322f3efeae8da44227e0acc760ffd3dea153716/patches/pointer-gestures-unstable-v1/pointer-gestures-unstable-v1.patch)
- [2024-04-11](https://codeberg.org/dwl/dwl-patches/raw/commit/c676de59d51e613bd52ac46c77a24b1cac9a61a1/pointer-gestures-unstable-v1/pointer-gestures-unstable-v1.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/fc4146f3068dcd46035a2a11fe9d6109a97ae6d6/pointer-gestures-unstable-v1/pointer-gestures-unstable-v1.patch)

### Authors
- [wochap](https://codeberg.org/wochap)
---
# press_repeat_release

### Description
This patch adds 3 additional options to the `Key` struct, `on_press`, `on_repeat` and `on_release` which can be used to control which events a key binding should be triggered on.

NOTE: Due to concerns about patching difficulties this patch does NOT include any changes to `config.def.h`. After applying you will need to add the 3 additional initializers to each key binding that you would like to modify. Any key binding that is not updated will cause a build warning but should function as it does in vanilla.

### Download
- [git branch](https://codeberg.org/USERNAME/dwl/src/branch/press_repeat_release)
- [2024-03-27](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/press_repeat_release/press_repeat_release.patch)

### Authors
- [minego](https://codeberg.org/minego)
---
# primaryselection

### Description
Adds a config option to disable/enable primary selection (middle-click paste).

### Download
- [git branch](https://codeberg.org/nullsystem/dwl/src/branch/main_primaryselection)
- [2024-04-06](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/primaryselection/primaryselection.patch)

### Authors
- [nullsystem](https://codeberg.org/nullsystem)
- [Palanix](https://github.com/PalanixYT) - Previous Primary-Selection patch

---
# push

### Description
Adds functions `pushup` and `pushdown` to move windows within the tiling order.

### Download
- [git branch](https://codeberg.org/sevz/dwl/src/branch/push)
- [2024-09-03](/dwl/dwl-patches/raw/branch/main/patches/push/push.patch)
- [push-0.7.patch](/dwl/dwl-patches/raw/branch/main/patches/push/push-0.7.patch)

### Authors
- [sevz](https://codeberg.org/sevz)
- [Devin J. Pohly](https://github.com/djpohly)

---
# regexrules

### Description
Allows the use of regular expressions for window rules "app_id" and "title"

```c
static const Rule rules[] = {
    // ...
    { "kitty-htop",  NULL,  1 << 8,  0,  -1 },
    { "^kitty$",     NULL,  0,       0,  -1 },
    // ...
};
```

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/regexrules)
- [2024-04-11](https://codeberg.org/dwl/dwl-patches/raw/commit/2a6560c167e5c9afc5598ac5431d23d90de8846c/regexrules/regexrules.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/98cba933c9f4099202e54f39acbf17e05bde828a/regexrules/regexrules.patch)

### Authors
- [wochap](https://codeberg.org/wochap)

---
# regions

### Description		
This patch will allow for a program to be used and have the current window regions on all monitors to be passed to the program as standard input.		

example is `grim -g "$(slurp)"`		

### Download
- [git branch](https://codeberg.org/sewn/dwl/src/branch/regions)
- [2024-02-14](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/regions/regions.patch)

### Authors		
- [sewn](https://github.com/apprehensions)
---
# relative-mouse-resize

### Description
When resizing windows, the mouse will jump and resize the window in the quadrant that the resize starts at. 

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/relative-mouse-resize)
- [2024-07-09](https://codeberg.org/dwl/dwl-patches/raw/commit/0bd725d0786248e1dfedbe6aa7453edfe736de43/patches/relative-mouse-resize/relative-mouse-resize.patch)
- [2024-04-11](https://codeberg.org/dwl/dwl-patches/raw/commit/655fd2916c1bcaa022ce6dcdfb370051cf64df66/relative-mouse-resize/relative-mouse-resize.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/b828e21717fa584affeb3245359c3ab615759fa4/relative-mouse-resize/relative-mouse-resize.patch)

### Authors
- [wochap](https://codeberg.org/wochap)

---
# remembertags

### Description
This patch modifies the behavior when selecting tags so that selecting a tag will also enable any other tags that were previously visible.

For example:
1. Select tag 5, with mod+5
2. Toggle tag 8, with ctrl+mod+8
3. Select tag 1, with mod+1. Tags 5 and 8 should no longer be visible.
4. Select tag 5 again, with mod+5. Tag 8 should be visible since it was remembered.
5. Select tag 5 again, with mod_5. Selecting the already selected tag resets any remembered tags, so now tag 5 should be the only one visible.

### Download
- [git branch](https://codeberg.org/minego/dwl/src/branch/remembertags)
- [2024-03-27](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/remembertags/remembertags.patch)

### Authors
- [minego](https://codeberg.org/minego)
---
# restore-monitor

### Description
Moves clients to their old output when it is reattached.

### Download
- [git branch](https://codeberg.org/eyusupov/dwl/src/branch/restore-monitor)
- [2024-04-07](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/restore-monitor/restore-monitor.patch)
### Authors
- [eyusupov](https://codeberg.org/eyusupov)
---
# right

### Description
Put newly connected monitors on the right, like X does.

### Download
- [2024-02-11](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/right/right.patch)

### Authors
- [Dima Krasner](https://codeberg.org/dimkr) (<dima@dimakrasner.com>)

---
# rlimit_max

### Description
Sets the current maximum open file descriptors to the maximum available limit.

This patch is useful - and solves issue [#628](https://codeberg.org/dwl/dwl/issues/628) for running heavy Xwayland applications on systems that do not provide limits out of the box.

### Download
- [0.7](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/rlimit_max/rlimit_max.patch)

### Authors
- [sewn](https://codeberg.org/sewn)


---
# rotatetags

### Description
This patch provides the ability to rotate the tagset left / right. It implements a new function rotatetags which modifies the current tagset. Same as original dwm patch. Also adds ability to move focused client to left / right adjacent tag by specifying appropriate enum value as argument.

### Download
- [git branch](https://codeberg.org/korei999/dwl/src/branch/rotatetags)
- [2024-01-23](https://codeberg.org/korei999/dwl-patches/raw/branch/main/rotatetags/rotatetags.patch)

### Authors
- [korei999](https://codeberg.org/korei999)
---
# scenefx

### Description

Implement https://github.com/wlrfx/scenefx

```c
/* available options */

static const int opacity = 0; /* flag to enable opacity */
static const float opacity_inactive = 0.5;
static const float opacity_active = 1.0;

static const int shadow = 1; /* flag to enable shadow */
static const int shadow_only_floating = 0; /* only apply shadow to floating windows */
static const struct wlr_render_color shadow_color = COLOR(0x0000FFff);
static const struct wlr_render_color shadow_color_focus = COLOR(0xFF0000ff);
static const int shadow_blur_sigma = 20;
static const int shadow_blur_sigma_focus = 40;
static const char *const shadow_ignore_list[] = { "xdg-desktop-portal-gtk", NULL }; /* list of app-id to ignore */

static const int corner_radius = 0; /* 0 disables corner_radius */

static const int blur = 1; /* flag to enable blur */
static const int blur_optimized = 1;
static const int blur_ignore_transparent = 1;
static const struct blur_data blur_data = {
	.radius = 5,
	.num_passes = 3,
	.noise = 0.02,
	.brightness = 0.9,
	.contrast = 0.9,
	.saturation = 1.1,
};
```

> **NOTE:** If you are using nix with flakes, scenefx has a flake for scenefx https://github.com/wlrfx/scenefx/blob/main/flake.nix

> **NOTE:** Some GTK apps are being cut off when they have shadows enabled. You can use the `shadow_ignore_list` option to prevent shadows from being rendered on those apps

> **NOTE:** Blur doesn't work on windows with opacity set (opacity_active, opacity_inactive)

> **NOTE:** In DWL's Makefile `scenefx` must be placed before wlroots, e.g. `PKGS = scenefx wlroots wayland-server ...`

<details>
<summary>Preview</summary>
<pre>
<img src="https://i.imgur.com/4kFhSaS.png"/>
<img src="https://i.imgur.com/9ZQAUXx.png"/>
</pre>
</details>

### Download

- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/scenefx)
- [2024-07-09](https://codeberg.org/dwl/dwl-patches/raw/commit/13d96b51b54500dd24544cf3a73c61b7a1414bc6/patches/scenefx/scenefx.patch)

  **IMPORTANT:** This patch only works with the `2ec3505248e819191c37cb831197629f373326fb` commit on the `main` branch of `scenefx`, therefore, it does not support **blur**.

  **IMPORTANT:** This patch requires you to build DWL with the following dependencies

  - **scenefx**
  - libGL

- [2024-04-11](https://codeberg.org/dwl/dwl-patches/raw/commit/6e3a57ffd16dafa31900b7e89e51672bd7bcc1e8/scenefx/scenefx.patch)

  **IMPORTANT:** This patch only works with the `de4ec10e1ff9347b5833f00f8615d760d9378c99` commit on the `wlr_scene_blur` branch of `scenefx`, as it adds support for **blur**.

  **IMPORTANT:** This patch requires you to build DWL with the dependencies of WLROOTS:

  - **scenefx**
  - libGL
  - libcap
  - libinput
  - libpng
  - libxkbcommon
  - mesa
  - pixman
  - seatd
  - vulkan-loader
  - wayland
  - wayland-protocols
  - xorg.libX11
  - xorg.xcbutilerrors
  - xorg.xcbutilimage
  - xorg.xcbutilrenderutil
  - xorg.xcbutilwm
  - xwayland (optional)
  - ffmpeg
  - hwdata
  - libliftoff
  - libdisplay-info

- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/7a5c3420822074c544fa102e030b7c30aa6b6be8/scenefx/scenefx.patch)

### Authors

- [wochap](https://codeberg.org/wochap)

---
# scroll-factor

### Description
This patch adds scroll factor to dwl. The settings can be found in the trackpad section of the config. This allows user to control the sensitivity of 2-finger touchpad scrolling.

### Download
- [git branch](https://codeberg.org/singul4ri7y/dwl/src/branch/scroll-factor)
- [2024-07-12](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/scroll-factor/scroll-factor.patch)

### Authors
- [singul4ri7y](https://codeberg.org/singul4ri7y)

---
# setupenv

### Description
Allow configuring environment variables in config.h

### Download
- [git branch](https://codeberg.org/notchoc/dwl/src/branch/setupenv)
- [2024-03-26](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/setupenv/setupenv.patch)
### Authors
- [notchoc](https://codeberg.org/notchoc)

---
# shiftview

### Description
Add keybindings to cycle through tags with visible clients.

### Download
- [git branch](https://codeberg.org/guidocella/dwl/src/branch/shiftview)
- [2024-01-27](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/shiftview/shiftview.patch)

### Authors
- [Guido Cella](https://codeberg.org/guidocella)

---
# simpleborders

### Description
Like smartborders. Don't put borders when there is only one window on the screen.

### Download
- [git branch](https://codeberg.org/bencc/dwl/src/branch/simpleborders)
- [2024-06-18 applies to dwl wlroots-next branch](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/simpleborders/simpleborders-wlrootsnext-20240618.patch)
- [2023-01-07](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/simpleborders/simpleborders.patch)
### Authors
- [Ben Collerson](https://codeberg.org/bencc)

---
# singlemaster

### Description
Restricts layout to only having one client in the master area.

### Download
- [git branch](https://codeberg.org/bencc/dwl/src/branch/singlemaster)
- [v0.6](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/singlemaster/singlemaster.patch)

### Authors
- [Ben Collerson](https://codeberg.org/bencc)

---
# singletagset

### Description
Single set of tags shared between multiple monitors.

This patch allows all the tags to be shared between both (or more) monitors.
So a single set of tags from 1 to 9 can be viewed on any monitor, as opposed to
having separate tag sets 1 to 9 on each monitor.

Originally based on the dwm single_tagset patch:
https://dwm.suckless.org/patches/single_tagset/

### Download
- [git branch (v0.7)](https://codeberg.org/Rutherther/dwl/src/branch/v0.7/singletagset)
- [git branch (v0.6)](https://codeberg.org/bencc/dwl/src/branch/singletagset)
- [2024-07-26 (v0.7)](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/singletagset/singletagset-v0.7.patch)
- [2024-05-16 (v0.6)](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/singletagset/singletagset-v0.6.patch)

### Authors
- [Ben Collerson](https://codeberg.org/bencc)
- [Rutherther](https://codeberg.org/Rutherther)

---
# singletagset-pertag

### Description
Pertag keeps layouts, mfact and nmaster per tag
instead of per output.

This adapted version of pertag contains one version of
the rules per all outputs, instead of one per output.
This makes switching to tags from other monitors keep
the window layout.

This patch expects [singletagset](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/singletagset)
patch to be already in your tree committed. It applies onto it.

This patch is incompatible with [pertag](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/pertag).

### Download
- [2024-07-26](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/singletagset-pertag/singletagset-pertag.patch)
- [git branch](https://codeberg.org/Rutherther/dwl/src/branch/v0.7/singletagset-pertag)

### Authors
- [Rutherther](https://codeberg.org/Rutherther)
- [wochap (maintainer of pertag patch)](https://codeberg.org/wochap)
- [Guido Cella (creator of pertag patch)](https://codeberg.org/guidocella)

---
# singletagset-sticky

### Description
Makes sticky work as expected with singletagset. The sticky window will
stay on original output until you explicitely put it to a different monitor.

This patch expects both [singletagset](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/singletagset) and [sticky](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/sticky) patches to be already in
your tree committed. It applies onto them.

### Download
- [2024-07-26](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/singletagset-sticky/singletagset-sticky.patch)
- [git branch](https://codeberg.org/Rutherther/dwl/src/branch/v0.7/singletagset-sticky)

### Authors
- [Rutherther](https://codeberg.org/Rutherther)

---
# skipfocus

### Description
Adds a rule-based ability to skip automatically focusing a window on creation. Expected use-case is for transient windows like notifications etc. The window can still be focused by mouse or keyboard movement.

| `skipfocus` value | effect             |
| ----------------- | ------------------ |
| 0                 | usual              |
| 1                 | skipautofocus      |
| 2                 | skipfocus entirely |

### Download
- [20240714](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/skipfocus/skipfocus.patch)
- [20240108](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/skipfocus/skipfocus20240108.patch)
- [git branch](https://codeberg.org/dhruva_sambrani/dwl/src/branch/skipfocus)

### Authors
- [Dhruva Sambrani](https://codeberg.org/dhruva_sambrani)


---
# smartborders

### Description
The borders of a window aren't drawn when the window is the only tiling window
in its tag OR if the window is in a monocle layout.

### Download
- [git branch](https://codeberg.org/sevz/dwl/src/branch/smartborders)
- [main 2024-09-02](/dwl/dwl-patches/raw/branch/main/patches/smartborders/smartborders.patch)
- [smartborders-0.7.patch](/dwl/dwl-patches/raw/branch/main/patches/smartborders/smartborders-0.7.patch)

### Authors
- [sevz](https://codeberg.org/sevz)
- [fauxmight](https://codeberg.org/fauxmight)
- [Piotr Marendowski](https://github.com/piotr-marendowski)
- Andrey Proskurin

---
# snail

### Description
Adds a spiral-inspired layout for wide screens.

### Download
- [2024-02-11](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/snail/snail.patch)

### Authors
- [Dima Krasner](https://codeberg.org/dimkr) (<dima@dimakrasner.com>)
- [Nikita Ivanov](https://github.com/NikitaIvanovV) (fix for flickering)

---
# snail-gaps

### Description

Adds support for the [gaps patch](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/gaps)
to the [snail layout patch](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/snail).

Install the [gaps patch](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/gaps)
and the [snail patch](https://codeberg.org/dwl/dwl-patches/src/branch/main/patches/snail) first.

### Download

- [main 2024-08-08](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/snail-gaps/snail-gaps.patch)

### Authors

- [JoaoCostaIFG](https://codeberg.org/JoaoCostaIFG) ([joaocosta@posteo.net](mailto:joaocosta@posteo.net))

---
# stacker

### Description
Stacker is a patch that allows moving around the stack more freely. With only
one keybinding, quickly move, swap and jump around the window stack.

1. Focus any window of the stack with a single key binding.
2. Swap the currently focused windows with any other window in the stack.
3. Move the selected window in the stack with `relativeswap`.

This patch is heavily inspired by the original [stacker](https://dwm.suckless.org/patches/stacker/) dwm patch.

### Keybinding

- `MODKEY` + {`q`, `w`, `e`, `r`}: jump to the first, second, third and last
  window of the stack
- `MODKEY` + `SHIFT` + {`Q`, `W`, `E`, `R`}: swap the selected with the first, second, third and last
  window of the stack
- `MODKEY` + `SHIFT` + {`J`, `K`}: move the selected window up & down the stack

### Missing feature

Jumping to the last selected window is not yet implemented.

### Download
- [git branch](https://codeberg.org/jeromecst/dwl/src/branch/stacker)
- [2024-05-17](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/stacker/stacker.patch)

### Authors
- [jeromecst](https://codeberg.org/jeromecst)

---
# startargv

### Description
allow passing startup command on argv

e.g. `dwl -s foot -s` launches `foot -s`

put `sh -c` right after `dwl -s` to emulate normal behaviour

### Download
- [git branch](https://codeberg.org/notchoc/dwl/src/branch/startargv)
- [2024-07-03](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/startargv/startargv.patch)

### Authors
- [notchoc](https://codeberg.org/notchoc)

---
# sticky

### Description
Adds a toggleable function that makes a sticky client that is visible on all tags.

Originally based on [dwm sticky patch](https://dwm.suckless.org/patches/sticky).

### Download
- [2024-07-26](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/sticky/sticky.patch)
- [v0.4](https://github.com/djpohly/dwl/compare/main...dm1tz:04-sticky.patch)
- [git branch](https://codeberg.org/Rutherther/dwl/src/branch/v0.7/sticky)

### Authors
- [Rutherther](https://codeberg.org/Rutherther)
- [Dmitry Zakharchenko](https://github.com/dm1tz)

---
# swallow

### Description
Terminals swallow windows that they are the parent of.

foot is the terminal by default, you can change it in client rules in config.h.

2023-08-16 and up are made to also work with x windows: https://codeberg.org/dwl/dwl/issues/331

for freebsd users: apply swallow-freebsd.patch **on top of** swallow.patch

### Download
- [git branch](https://codeberg.org/notchoc/dwl/src/branch/swallow)
- [2024-07-13](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/swallow/swallow.patch)
- [2024-07-13](https://codeberg.org/dwl/dwl-patches/raw/commit/f64d701bab2f9f52d3637edd091684f920407d87/patches/swallow/swallow.patch)
- [2024-05-02](https://codeberg.org/dwl/dwl-patches/raw/commit/9c5d5d85f3ac780e7a14d5d0535e3349ce8b8f53/patches/swallow/swallow.patch)
- [2024-04-03](https://codeberg.org/dwl/dwl-patches/raw/commit/3c9a8e3232a8531871924484cef1ef0938730e15/swallow/swallow.patch)
- [2024-01-01](https://codeberg.org/dwl/dwl-patches/raw/commit/8a352a1b27a64821ba9fbfda52fe82463ac84c66/swallow/swallow.patch)
- [2023-10-26](https://github.com/djpohly/dwl/compare/main...youbitchoc:swallow.patch)
- [2023-08-16](https://github.com/djpohly/dwl/compare/main...mewkl:swallowx.patch)
- [2023-07-15](https://github.com/djpohly/dwl/compare/main...NikitaIvanovV:swallow.patch)
- [v0.4](https://github.com/djpohly/dwl/compare/main...dm1tz:04-swallow.patch)
- [2021-12-03](https://github.com/djpohly/dwl/compare/main...dm1tz:swallow.patch)

### Authors
- [Dmitry Zakharchenko](https://github.com/dm1tz)
- [Palanix](https://codeberg.org/Palanix)
- [Nikita Ivanov](https://github.com/NikitaIvanovV)
- [Connor Worrell](https://github.com/ConnorWorrell)
- [Mewkl](https://github.com/mewkl)
- [Choc](https://codeberg.org/notchoc)

---
# swapandfocusdir

### Description
Focus the window (floating or no) to the left, right, above, or below the current focused window.

Swap the focused window with the window (no floating) to the left, right, above, or below.

**NOTE:** this patch uses the same algorithm that River uses to select the window in the given direction.

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/swapandfocusdir)
- [2024-07-09](https://codeberg.org/dwl/dwl-patches/raw/commit/13d96b51b54500dd24544cf3a73c61b7a1414bc6/patches/swapandfocusdir/swapandfocusdir.patch)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/swapandfocusdir/swapandfocusdir.patch)

### Authors
- [wochap](https://codeberg.org/wochap)

---
# switchtotag

### Description
Add a rule option to switch to the configured tag when a window opens, then switch back when it closes.

### Download
- [git branch](https://codeberg.org/guidocella/dwl/src/branch/switchtotag)
- [2024-08-28](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/switchtotag/switchtotag.patch)

### Authors
- [Guido Cella](https://codeberg.org/guidocella)

---
# tab

### Description
Add a tab bar or window title to the top or bottom of windows.

### Download
- [git branch](https://codeberg.org/dev-gm/dwl/src/branch/tab)
- [2024-03-15](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/tab/tab.patch)

### Authors
- [dev-gm](https://codeberg.org/dev-gm)
---
# tablet-input

### Description
implements wlr-tablet-v2 for drawing tablets and supports cursor emulation

inspired by @guyuming76's [branch](https://codeberg.org/guyuming76/dwl/commits/branch/graphic_tablet), with coding help from @Palanix and testing by @Thanatos

### Download
- [git branch](https://codeberg.org/notchoc/dwl/src/branch/tablet-input)
- [2024-07-31](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/tablet-input/tablet-input.patch) fixes pen not working after lifting up
- [2024-06-21](https://codeberg.org/dwl/dwl-patches/raw/commit/18d283d3746ecbc3cd7650358c5769e03b346425/patches/tablet-input/tablet-input.patch)
- [2024-06-19](https://codeberg.org/dwl/dwl-patches/raw/commit/fee4da5cb6470ca5349fa2102765705e19d3bfa3/patches/tablet-input/tablet-input.patch)
- [2024-05-04](https://codeberg.org/dwl/dwl-patches/raw/commit/748b4bc6a73828f3e74b210862bebcda4c9dfb3c/patches/tablet-input/tablet-input.patch)

### Authors
- [notchoc](https://codeberg.org/notchoc)
- [Palanix](https://codeberg.org/Palanix)

---
# tearing

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

---
# titleurgent

### Description
Whenever a client title changes set the client's urgent flag.

Hacky solution I use to deal with qutebrowser not setting urgent flag when a new tab is opened.

### Download
- [git branch](https://codeberg.org/bencc/dwl/src/branch/titleurgent)
- [2024-01-02](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/titleurgent/titleurgent.patch)

### Authors
- [Ben Collerson](https://codeberg.org/bencc)
---
# toggle_constraints

### Description
Adds a function called togglepointerconstraints to turn pointer constraint enforcement on and off with a keybind. 

### Usage
Add a binding for the togglepointerconstraints function in the keys[] array of config.h. The function does not take any argument. Pointer constraints default to enabled, and can be toggled on and off with the function from there.

Example:
```
{ MODKEY, XKB_KEY_c, togglepointerconstraints, {0}},
```

### Download
- [Git branch](https://codeberg.org/thanatos/dwl/src/branch/toggle_constraints)
- [2024-03-26](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/toggle_constraints/toggle_constraints)

### Authors
- [thanatos](https://codeberg.org/thanatos)
---
# togglekblayout

### Description

> This patch is no longer being maintained by me [wochap](https://codeberg.org/wochap), since I'm now using a different patch specific to my use case: https://codeberg.org/wochap/dwl/src/branch/v0.6-b/xkb-rules-switcher/xkb-rules-switcher.patch

Switch between multiple keyboard layouts at runtime.

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.5/togglekblayout)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/togglekblayout/togglekblayout.patch)

### Authors
- [wochap](https://codeberg.org/wochap)
- [Stivvo](https://github.com/Stivvo)


---
# togglekblayoutandoptions

### Description
Switch between multiple keyboard layouts, variants, and options at runtime.

### Download
- [git branch](https://codeberg.org/dev-gm/dwl/src/branch/togglekblayoutandoptions)
- [2024-03-15](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/togglekblayoutandoptions/togglekblayoutandoptions.patch)

### Authors
- [dev-gm](https://codeberg.org/dev-gm)
---
# unclutter

### Description
Hide the mouse cursor if it isn't being used for a certain period of time.

### Download
- [git branch](https://codeberg.org/guidocella/dwl/src/branch/unclutter)
- [2024-08-06](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/unclutter/unclutter.patch)

### Authors
- [Guido Cella](https://github.com/guidocella)
- [dm1tz](https://github.com/dm1tz)
- [Ben Collerson](https://codeberg.org/bencc)

---
# ungroup-keyboards

### Description
Ungroup keyboard input devices based on device name.

I wrote this patch was because keyboard device grouping breaks the behaviour of
the ydotool virtual device. This patch fixes my issue #558 in the codeberg
issue tracker.

See the inputdevicerules patch for a more generalised version of this idea.

### Download
- [git branch](https://codeberg.org/bencc/dwl/src/branch/ungroup-keyboards)
- [2024-06-16](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/ungroup-keyboards/ungroup-keyboards.patch)

### Authors
- [Ben Collerson](https://codeberg.org/bencc)

---
# vanitygaps

### Description
Adds (inner) gaps between client windows and (outer) gaps between windows and
the screen edge in a flexible manner.

### Download
- [git branch](https://codeberg.org/sevz/dwl/src/branch/vanitygaps)
- [main 2024-09-01](/dwl/dwl-patches/raw/branch/main/patches/vanitygaps/vanitygaps.patch)
- [vanitygaps-0.7.patch](/dwl/dwl-patches/raw/branch/main/patches/vanitygaps/vanitygaps-0.7.patch)

### Authors
- [sevz](https://codeberg.org/sevz)
- [Bonicgamer](https://github.com/Bonicgamer)

---
# varcol

### Description
A variable column layout. 

This layout behaves much the same as the `tile` layout, but adds key bindings that can be used to:
- Increase/decrease the number of non-master columns
- Increase/decrease the colfact to adjust the column spacing
- Push a client in or out of a special `left` column
- Toggle displaying the special `left` column

### Download
- [git branch](https://codeberg.org/minego/dwl/src/branch/varcol)
- [2024-03-27](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/varcol/varcol.patch)

### Authors
- [minego](https://codeberg.org/minego)

---
# viewnextocctag

### Description
View the next or previous tag, skipping any tags that do not have any clients.

### Download
- [git branch](https://codeberg.org/bencc/dwl/src/branch/viewnextocctag)
- [2023-01-06](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/viewnextocctag/viewnextocctag.patch)

### Authors
- [Ben Collerson](https://codeberg.org/bencc)

---
# virtual-pointer

### Description
implement wlr_virtual_pointer_v1 for things like wayvnc server to work

**NOTE:** no longer neccessary if you are using a DWL version after https://codeberg.org/dwl/dwl/commit/ac6074f4fdb8cc263c877f08e16a5805d3bb22d2

### Download
- [git branch](https://codeberg.org/wochap/dwl/src/v0.5/virtual-pointer)
- [v0.5](https://codeberg.org/dwl/dwl-patches/raw/commit/0096e49402bc59b4050e12cdb9befb79d0011006/virtual-pointer/virtual-pointer.patch)

### Authors
- [wochap](https://codeberg.org/wochap)
- [youbitchoc](https://github.com/youbitchoc)
---
# warpcursor

### Description
Warp cursor to the centre of newly focused clients.

Only moves the cursor if the cursor is currently not on the new client.

This is my version of the orphaned cursorwarp patch except I left out the
config flag as I think it is unnecessary.

### Download
- [git branch](https://codeberg.org/bencc/dwl/src/branch/warpcursor)
- [v0.6](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/warpcursor/warpcursor.patch)

### Authors
- [Ben Collerson](https://codeberg.org/bencc)
- [Faerryn](https://github.com/faerryn)

---
# winview

### Description
Implements the function `winview` which switches the visible tags to the tags on which the current client is visible.

This patch is inspired from <https://dwm.suckless.org/patches/winview/>. Citing the description of the dwm patch:

> Dwm tags are a powerfull feature that allows organizing windows in workspaces. Sometime it can be difficult to remember the tag to activate to unhide a window. With the winview patch the window to unhide can be selected from the all-window view. The user switches to the all-window view (Mod1-0), selects the window (Mod1-j/k or using the mouse) and press Mod1-o. The key Mod1-o switches the view to the selected window tag.
> 
> #### Recommend patches
> 
> The grid layout is well adapted to display many windows in a limited space. Using both grid and pertag patches you will be able to select this layout for the all-window view while keeping your preferred layout for the other views.
> Configuration and Installation
> Using the default configuration file
> 
>     Make sure the directory where you build dwm does not contain a config.h file;
>     Apply the patch;
>     Run make and make install.
> 
> Using an existing customised configuration file
> 
> Apply the patch; Add the following element in the keys array:
> 
> `{ MODKEY, XK_o, winview, {0} },`
> 
> Run make and make install.
> 
> An example of how to insert this line can be found in the default config file template, config.def.h.

### Download
- [2023-11-26](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/winview/winview.patch)
- [git branch](https://codeberg.org/dhruva_sambrani/dwl/src/branch/winview)

### Authors
- [Dhruva Sambrani](https://codeberg.org/dhruva_sambrani)


---
# xwayland-handle-minimize

### Description
Some windows (wine) games go black screen after losing focus and never recover https://github.com/swaywm/sway/issues/4324. This patch fixes this by handling minimize requests that some xwayland clients do.

 ## Download
- [git branch](https://codeberg.org/korei999/dwl/src/branch/xwayland-handle-minimize)
- [2024-04-01](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/xwayland-handle-minimize/xwayland-handle-minimize.patch)

### Authors
- [korei999](https://codeberg.org/korei999)
---
# zoomswap

### Description
This patch swaps the current window (C) with the previous master (P) when zooming.
```
Original behaviour :
+-----------------+-------+
|                 |       |
|                 |       |
|                 |       |
|        P        +-------|
|                 |       |
|                 |   C   |
|                 |       |
+-----------------+-------+

+-----------------+-------+
|                 |       |
|                 |   P   |
|                 |       |
|        C        +-------|
|                 |       |
|                 |       |
|                 |       |
+-----------------+-------+

New Behaviour :
+-----------------+-------+
|                 |       |
|                 |       |
|                 |       |
|        C        +-------+
|                 |       |
|                 |   P   |
|                 |       |
+-----------------+-------+

+-----------------+-------+
|                 |       |
|                 |       |
|                 |       |
|        P        +-------+
|                 |       |
|                 |   C   |
|                 |       |
+-----------------+-------+
```

### Download
- [git branch](https://codeberg.org/Palanix/dwl/src/branch/zoomswap)
- [v0.7](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/zoomswap/zoomswap-v0.7.patch)
- [v0.6](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/zoomswap/zoomswap-v0.6.patch)
- [2024-02-15](https://codeberg.org/dwl/dwl-patches/raw/branch/main/patches/zoomswap/zoomswap.patch)

### Authors
- [Palanix](https://codeberg.org/Palanix)

---
# STALE PATCHES
## DRMLeaseManager

### Description
This implements the DRM lease protocol, which is needed to use devices such as VR headsets.

### Download
- [2023-05-26](https://github.com/djpohly/dwl/compare/main...minego:drm_lease_patch.patch)

### Authors
- [Micah N Gorrell](https://github.com/minego)
---
## XF86keysym

### Description
Utilizing the [/usr/include/X11/XF86keysym.h](https://cgit.freedesktop.org/xorg/proto/x11proto/tree/XF86keysym.h) header file to change the volume via the appropriate keys.

### Download
- [2023-10-15](https://github.com/djpohly/dwl/compare/main...nakibrayan3:dwl:update-XF86keysym-patch.patch)
- [2021-05-06](https://github.com/djpohly/dwl/compare/main...917Wolf:vol.patch)

### Authors
- [917Wolf](https://github.com/917Wolf)
- [Rayan Nakib](https://nakibrayan2.pages.dev)

---
## alphafocus

### Description
Adds configurable transparency for focused and unfocused windows.

### Download
- [2021-12-03](https://github.com/djpohly/dwl/compare/main...juliag2:alphafocus.patch)

### Authors
- [Julia](https://github.com/juliag2)
---
## attachabove

### Description
Newly created windows are placed above the currently selected window in the stack.

### Download
- [2021-01-16](https://github.com/djpohly/dwl/compare/main...ss7m:attachabove.patch)

### Authors
- [sam-barr](https://github.com/ss7m)
---
## attachtop

### Description

This is a port of attachtop patch for dwm: https://dwm.suckless.org/patches/attachtop

New client attaches below the last master/on top of the stack.

Behavior feels very intuitive as it doesn't disrupt existing masters no matter the amount of them, it only pushes the clients in stack down.

### Download
- [2023-07-15](https://github.com/djpohly/dwl/compare/main...NikitaIvanovV:attachtop.patch)

### Authors
- [Nikita Ivanov](https://github.com/NikitaIvanovV)
---
## autorotation

### Description
Adds keybindings for screen rotation and auto rotation from an accelerometer.

### Setup
Find an accelerometer device in sysfs (`cat /sys/bus/iio/devices/iio*/name`,
or using a script: [monitor-iio.sh](https://github.com/Unprex/dotfiles/blob/main/scripts/monitor-iio.sh)) \
Find the raw output file of the accelerometer
(e.g. `cat /sys/bus/iio/devices/iio:device0/in_accel_x_raw` should output an integer). \
Add the raw output file names to the dwl configuration **accel_\***.

Add a udev rule to uniquely identify the device, for example:
```
sudo echo 'SUBSYSTEM=="iio", KERNEL=="iio*", ATTR{name}=="accel_3d", GROUP="input", SYMLINK+="input/accel"' >> /etc/udev/rules.d/99-accel.rules
sudo udevadm control --reload-rules && sudo udevadm trigger
```
(the device is probably already in /dev/ e.g. `/dev/iio:device0` but on my computer the number changes after a reboot)

A symlink to the device should now be available in `/dev/input/` and accessible to input group members. \
Add the device path to the dwl configuration **accel_path**.

### Config
* `rotation_enabled`: If the auto rotation is enabled on startup.
* `rotation_delay`: How often to check the accelerometer values in milliseconds. 
* `rotation_flat`: Threshold on the normalized Z axis to consider the device flat and stop the auto rotation.
* `rotation_thresh`: Rotation threshold after which the screen flips (values less than 0.5 will cause a back and forth).

+ `accel_path`: The path to the accelerometer device file (e.g. "/dev/input/accel").
+ `accel_x`: The name of the sysfs file for the accelerometer x axis.
+ `accel_y`: The name of the sysfs file for the accelerometer y axis.
+ `accel_z`: The name of the sysfs file for the accelerometer z axis.

Default keybindings:
* `<Modkey>` + `<Shift>` + `<Arrows>`: Change the screen rotation manually (doesn't disable the auto rotation).
* `<Modkey>` + `<Shift>` + `<R>`: Enable/disable the auto rotation.

### Download
- [2022-10-25](https://github.com/djpohly/dwl/compare/main...Unprex:rotation.patch)

### Authors
- [Unprex](https://github.com/Unprex)
---
## center

### Description
Adds a rule to automatically center clients on the current monitor.

### Download
- [v0.4](https://github.com/djpohly/dwl/compare/main...dm1tz:04-center.patch)
- [v0.4-r1](https://github.com/djpohly/dwl/compare/main...dm1tz:04rc1-iscenter.patch)
- [2022-08-27](https://github.com/djpohly/dwl/compare/main...dm1tz:iscenter.patch)

### Authors
- [Dmitry Zakharchenko](https://github.com/dm1tz)

---
## clipboardManager

### Description
Store your clipboard history using `clipman` clipboard manager without your KeePassXC passwords leaking into clipman.

Ensure these dependencies are installed (instructions for debian, other distros are left as an exercise...):

    apt install clipman libmodern-perl-perl moreutils wl-clipboard

Change your command to launch `dwl` to something like the following:

    dwl -s 'pee somebar dwl-getwindowtitle'

Ensure the following command is running in the background of your `dwl` session. Put it whereever your auto-started stuff is.

    exec wl-paste -t text --watch dwl-clipman

This solution is based on the following reddit post, modified to support `dwl`. https://www.reddit.com/r/swaywm/comments/ljl0dh/keeping_secrets_secret_with_keepassxc_clipman_and/

Feel free to use this code however you want, but I can't guarantee it will work for what you are trying to do. Licenced under the same license as `dwl`, "WITHOUT WARRANTY OF ANY KIND".



### Download
- [2022-12-21](https://github.com/djpohly/dwl/compare/main...bencollerson:clipboard-manager.patch)
- [2022-12-01](https://github.com/djpohly/dwl/compare/main...bencollerson:94d0a21.patch)

### Authors
- [Ben Collerson](https://github.com/bencollerson)
---
## clipboardipc

### Description
Adds clipboard functionality. Requires the [ipc](https://github.com/djpohly/dwl/wiki/ipc) patch for dwl and `wl-clipboard` to be installed. By default, requires [clipman](https://github.com/yory8/clipman) for the clipboard and [dwl-state](https://github.com/MadcowOG/dwl-state) for getting the appid of the focused application, but you can change these in the script if you have alternatives. You may change which applications to not record by modifying the `excludes` array in `dwl-cliboard-watcher`. Make sure `wl-paste -t text -w dwl-clipboard-watcher` is running after dwl.

### Downloads
 - [2023-3-01](https://github.com/djpohly/dwl/compare/main...MadcowOG:ipc-clipboard.patch)

### Authors
 - [MadcowOG](https://github.com/MadcowOG)
---
## cyclelayouts

### Description
Adds function to cycle through available layouts.

### Download
- [v0.4](https://github.com/djpohly/dwl/compare/main...dm1tz:04-cyclelayouts.patch)
- [2021-07-27](https://github.com/djpohly/dwl/compare/main...vnepogodin:cyclelayouts.patch)

### Authors
- [Vladislav Nepogodin](https://github.com/vnepogodin)
---
## fibonacci

### Description
Arranges windows in a Fibonacci spiral or dwindle.

### Scheme
```
+-----------+-----------+  +-----------+-----------+
|           |           |  |           |           |
|           |     2     |  |           |     2     |
|           |           |  |           |           |
|     1     +--+--+-----+  |     1     +-----+-----+
|           | 5|-.|     |  |           |     |  4  |
|           +--+--+  3  |  |           |  3  +--+--+
|           |  4  |     |  |           |     | 5|-.|
+-----------+-----+-----+  +-----------+-----+-----+
	 spiral                     dwindle
```

### Download
- [2023-06-21](https://github.com/djpohly/dwl/compare/main...Abanoub8:fibonacci.patch)
- [2022-09-22](http://0x0.st/oVlu.patch)
- [2021-05-06](https://github.com/djpohly/dwl/compare/main...917Wolf:fib.patch)

### Authors
- [Abanoub8](https://github.com/Abanoub8)
- [medanisjbara](https://github.com/medanisjbara)
- [917Wolf](https://github.com/917Wolf)
- Niki Yoshiuchi
---
## focusMonPointer

### Description
Implements `focusmon()` function that moves the cursor to the focused monitor.
### Download
- [2020-10-15](https://github.com/djpohly/dwl/compare/main...Stivvo:focusMonPointer.patch)

### Authors
- [Stivvo](https://github.com/Stivvo)
---
## focusdir

### Description
Focus the window left, right, above or below the current focused window

### Download
- [2023-19-15](https://github.com/djpohly/dwl/compare/main...XGames123:focusdir.patch)

### Authors
- [ldev](https://github.com/Xgames123)
---
## focusmaster

### Description
Focus the master regardless of the current focus.

### Download
- [2022-09-02](https://github.com/djpohly/dwl/compare/main...dm1tz:fmaster.patch)
- [2022-08-18](https://github.com/djpohly/dwl/compare/main...PalanixYT:focusmaster.patch)

### Authors
- [Palanix](https://github.com/PalanixYT)
---
## genericgaps

### Description
This patch is a modified version of [vanitygaps][vanitygaps] that adds gaps around clients regardless of a layout.
It means you can apply any layout patch and the gaps will be shown properly as long as the layout does not add any gaps on its own.

This works by allowing a layout to place clients normally without gaps,
and then correcting positions and dimensions of clients afterwards to add gaps around them.
To make it work, I had to modify `resize()` function,
and, as a side effect, this change fixed some flickering I experienced when using [snail][snail] layout.

[snail]: https://github.com/djpohly/dwl/wiki/snail
[vanitygaps]: https://github.com/djpohly/dwl/wiki/vanitygaps

### Changelog

2023-11-24:
- Refactor, it does exactly the same, just using less code.
- Replace `gappih`, `gappiv`, `gappoh` and `gappov` with only `gappx`. They don't do anything anyways.

### Download
- [2023-11-24](https://github.com/djpohly/dwl/compare/main...wochap:genericgaps.patch)
- [2023-05-20](https://github.com/djpohly/dwl/compare/main...NikitaIvanovV:genericgaps.patch) generic gaps
- [2023-05-20](https://github.com/djpohly/dwl/compare/main...NikitaIvanovV:genericgaps-rule.patch) generic gaps + monitor rule to enable gaps on certain monitors by default

### Authors
- [Nikita Ivanov](https://github.com/NikitaIvanovV)

---
## gridmode

### Description
Arranges windows in a grid of equal sizes.

### Download
- [2023-06-21](https://github.com/djpohly/dwl/compare/main...Abanoub8:gridmode.patch)
- [2021-07-24](https://github.com/djpohly/dwl/compare/main...vnepogodin:gridmode.patch)

### Authors
- [Vladislav Nepogodin](https://github.com/vnepogodin)
- [Abanoub8](https://github.com/Abanoub8)
---
## hidecursor

### Description
Hide the cursor when typing

### Download
- [2023-10-25](https://github.com/djpohly/dwl/compare/main...apprehensions:hidecursor.patch)
- [2023-02-19](https://github.com/djpohly/dwl/compare/main...PalanixYT:type_hide.patch)

### Authors
- [Palanix](https://github.com/PalanixYT)
---
## kbrules

### Description
Allow for keyboard rules to be used; This allows for keyboard-specific options or layouts.

The keyboard's names can be retrieved from `libinput list-devices | grep Device`, example:
```c
static const KeyboardRule kbrules[] = {
	{ "AT Translated Set 2 keyboard", { .options = "altwin:swap_alt_win,caps:swapescape" } },
};
```

### Download
- [2023-09-20](https://github.com/djpohly/dwl/compare/main...apprehensions:dwl:kbrules.patch)

### Authors
- [sewn](https://github.com/apprehensions)
---
## keychord

### Description

This patch implements sequences for chained keybindings (like the dwm [keychord](https://dwm.suckless.org/patches/keychord/) patch).

_Notes_: 
- The maximum number of sequences is set to `5` in the `Keychord` struct for a given keybinding
- This original motivation was better support for [stumpwm](https://stumpwm.github.io/) style of keybindings, however this is not a limitation

### Example

The default values for `MODKEY` and `PREFIXKEY` can be changed in `config.def.h` and/or `config.h`.

#### emacs-like

In the example below, the `firefox` command is bound to the key sequence `alt-s alt-u f`.

```C
static const Keychord keychords[] = {
  /* Note that Shift changes certain key codes: c -> C, 2 -> at, etc. */
  /* count key_sequences                          function  argument */
  { 3, {{MODKEY, XKB_KEY_s}, {MODKEY, XKB_KEY_u}, {MOD_NONE, XKB_KEY_f}}, spawn, SHCMD("firefox") },
};
```

#### vim-like

In the example below, the `firefox` command is bound to the key sequence `alt-s u f`.

```C
static const Keychord keychords[] = {
  /* Note that Shift changes certain key codes: c -> C, 2 -> at, etc. */
  /* count key_sequences                          function  argument */
  { 3, {{MODKEY, XKB_KEY_s}, {MOD_NONE, XKB_KEY_u}, {MOD_NONE, XKB_KEY_f}}, spawn,SHCMD("firefox") },
};
```

### Download

- [2023-03-12](https://github.com/djpohly/dwl/compare/main...yveszoundi:dwl-customization:keychord-2023-03-12.patch)
- [2023-02-15](https://github.com/djpohly/dwl/compare/main...yveszoundi:dwl-customization:v0.4-keychord-2023-02-15.patch)

### Authors

- [Yves Zoundi](https://github.com/yveszoundi)
---
## keymap

### Description
Print current keyboard layout to stdout

### Download
- [2022-09-10](https://github.com/djpohly/dwl/compare/main...GospodinHoroshiy:keymap.patch)

### Authors
- [Gospodin](https://github.com/GospodinHoroshiy)
---
## master-right

### Description
Show the master area to the right.

### Reason for deprecation
I created this patch for a user on Discord and I have never used it.

### Download
- [git branch](https://codeberg.org/sevz/dwl/src/branch/master-right)
- [main 2024-09-01](/dwl/dwl-patches/raw/branch/main/patches/master-right/master-right.patch)
- [master-right-0.7.patch](/dwl/dwl-patches/raw/branch/main/patches/master-right/master-right-0.7.patch)

### Authors
- [sevz](https://codeberg.org/sevz)

---
## mouse-follows-focus

### Description
This patch adds the option to let the cursor jump to the center of new clients, as well as move the cursor to the center of clients that gains focus.

### Download
- [2023-03-17](https://github.com/djpohly/dwl/compare/main...0undefined:mouse-follows-focus.patch)

### Authors
- [0undefined](https://github.com/0undefined)
---
## move-stack-top

### Description
Extend the [movestack](https://github.com/djpohly/dwl/wiki/movestack) patch to let you also focus, or move, a client to the top or bottom of the stack.

### Download
- [2023-03-12](https://github.com/djpohly/dwl/compare/main...0undefined:dwl:move-client-top.patch)

### Authors
- [0undefined](https://github.com/0undefined)
- Original movestack patch: [sam-barr](https://github.com/ss7m)
---
## nomousefocus

### Description
Prevent focus on mouseover.

### Download
- [2023-02-05](https://github.com/djpohly/dwl/compare/main...jjjt-git:nomousefocus.patch)

### Authors
- [JJJT](https://github.com/jjjt-git)
---
## onlyquitonempty

### Description
Only exit when no windows are open

### Download
- [2022-09-11](https://github.com/djpohly/dwl/compare/main...GospodinHoroshiy:onlyquitonempty.patch)

### Authors
- [Gospodin](https://github.com/GospodinHoroshiy)
---
## privilegeDrop

### Description
Adds the -u option that allows users to pass a desired uid to drop to after becoming DRM master.

### Download
- [2021-09-06](https://github.com/djpohly/dwl/compare/main...DanielMowitz:privilege-drop.patch)

### Authors
- [Daniel Mowitz](https://github.com/DanielMowitz)
---
## relativemouseresize

### Description

When resizing windows, the mouse will no longer jump to the bottom
right corner and only resize from that corner. Instead, the mouse will
resize the window in the quadrant that the resize starts at. This is the
same resize behavior as Sway and is similar to the resizehere dwm patch.

### Download
- [v0.4](https://github.com/djpohly/dwl/compare/main...schance995:dwl:relative-mouse-resize.patch)

### Authors
- [schance995](https://github.com/schance995)
---
## restartdwl

### Description
This patch allows you to restart dwl with a keybinding.  
**NOTE:** that all of your applications are gonna get killed on dwl restart.
  
The function creates a file at **/tmp/restart_dwl** and exits dwl.  
You have to modify your dwl launch script in order for this patch to work.  
Example dwl launch script:  
```sh
do=true
while $do ||  [ -f /tmp/restart_dwl ]; do
    do=false
    rm -rf /tmp/restart_dwl > /dev/null 2>&1
    dwl
done
```
It's a do-while that checks if **/tmp/restart_dwl** exists after the first run of dwl.  
If this file exists delete it and start dwl again.  

### Download
- [2022-10-27](https://github.com/djpohly/dwl/compare/main...krypciak:patch-restartdwl.patch)

### Authors
- [krypciak](https://github.com/krypciak)
---
## restoretiling

### Description
All floating windows become tiling when switching to a different layout.

### Download
- [2020-08-28](https://github.com/djpohly/dwl/compare/main...Stivvo:restoreTiling.patch)

### Authors
- [Stivvo](https://github.com/Stivvo)
---
## stickyrule

### Description
Add a rule to clients to spawn them [sticky](sticky) on start up.
I personally use it to make [dragon](https://github.com/mwh/dragon) show up on all tags.

### Download
Apply on top of [sticky patch](sticky).

- [2023-05-27](https://github.com/dm1tz/dwl/compare/04-sticky...NikitaIvanovV:stickyrule.patch)

### Authors
- [Nikita Ivanov](https://github.com/NikitaIvanovV)

---
## swaycompat

### Description
Implements just enough of the `sway-ipc` protocol to facilitate status bars. Tested with `waybar` and `rootbar`.

### Download
- [2022-06-08](https://github.com/djpohly/dwl/compare/main...StratusFearMe21:main.patch)

### Authors
- [Isaac Mills](https://github.com/StratusFearMe21)
---
## touchscreen

### Description
Adds SIMPLE touchscreen functionality.<br>
Currently emulates mouse movement and button presses.<br>

### Download
- [2023-03-31](https://github.com/djpohly/dwl/compare/main...fauxmight:dwl:simple_touch_input.patch)
- [2022-10-16](https://github.com/djpohly/dwl/compare/main...Unprex:touch-screen.patch)

### Authors
- [fauxmight](https://github.com/fauxmight)
- [Unprex](https://github.com/Unprex)
---
## vertile

### Description
A tiled layout optimized for wide vertical monitors.
### Scheme
```
|---------------------------|
|                           |
|                           |
|             M             |
|                           |
|                           |
|---------------------------|
|            t1             |
|---------------------------|
|            t2             |
|---------------------------|
|            t3             |
|---------------------------|
```
### Download
- [2023-06-21](https://github.com/djpohly/dwl/compare/main...Abanoub8:vertile.patch)
- [2021-08-15](https://github.com/djpohly/dwl/compare/main...ChausseBenjamin:vertile.patch)

### Authors
- [Benjamin Chausse](https://github.com/ChausseBenjamin)
- [Abanoub8](https://github.com/Abanoub8)
---
## xcursor

### Description

Set cursor theme and size via `XCURSOR_THEME` and `XCURSOR_SIZE` environmental variables.

### Download
- [2023-07-18](https://github.com/djpohly/dwl/compare/main...NikitaIvanovV:xcursor.patch)

### Authors
- [Nikita Ivanov](https://github.com/NikitaIvanovV)
---

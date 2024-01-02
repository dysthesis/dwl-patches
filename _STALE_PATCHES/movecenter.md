### Description
This patch provides a keybinding to center focused windows.

Press <kbd>MODKEY</kbd> + <kbd>x</kbd> to center the focused floating window.

It does NOT uncenter the window back to its previous location. It does not center windows that are not floating.

The variable `center_relative_to_monitor` allows the user to choose whether to center relative to the monitor or relative to the window area.

<details>
<summary>Explanation of center_relative_to_monitor:</summary>
<pre>
The "Monitor area" refers to the space enclosed by the green rectangle, while the "Window area" refers to the space enclosed by the red rectangle.
<img src="https://i.imgur.com/xhejzPh.png"/>
</pre>
</details>

### Download
- [2023-09-11](https://github.com/djpohly/dwl/compare/main...wochap:movecenter.patch)

### Authors
- [wochap](https://github.com/wochap)
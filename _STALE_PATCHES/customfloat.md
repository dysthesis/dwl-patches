### Description
Rules for floating windows support default x, y, width, height. Defaults to the center of the screen and the client size.

### Changelog

2023-09-11:
- Rewrite the patch so that it works with the latest dwl
- If the width or height is less than or equal to 1, then the value will be interpreted as a percentage. For example, 0.5 represents 50%, 0.25 represents 25%, and 1 represents 100%. **NOTE**: Some clients, like Thunar, have minimum width/height
- A variable `center_relative_to_monitor` has been added, allowing the user to choose whether to center relative to the monitor or relative to the window area.

  <details>
  <summary>Explanation of center_relative_to_monitor:</summary>
  <pre>
  The "Monitor area" refers to the space enclosed by the green rectangle, while the "Window area" refers to the space enclosed by the red 
  rectangle.
  <img src="https://i.imgur.com/xhejzPh.png"/>
  </pre>
  </details>

### Download
- [2023-09-11](https://github.com/djpohly/dwl/compare/main...wochap:customfloat.patch)
- [2020-09-02](https://github.com/djpohly/dwl/compare/main...Stivvo:customFloat.patch)

### Authors
- [Stivvo](https://github.com/Stivvo)
- [wochap](https://github.com/wochap)
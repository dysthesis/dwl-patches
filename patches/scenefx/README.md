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

static const int corner_radius = 0; /* 0 disables corner_radius */
static const int corner_radius_inner = 3; /* 0 disables corner_radius */

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

> **NOTE:** Blur doesn't work on windows with opacity set (opacity_active, opacity_inactive)

> **NOTE:** In DWL's Makefile `scenefx` must be placed before `wlroots-0.18`, e.g. `PKGS = scenefx wlroots-0.18 wayland-server ...`

<details>
<summary>Preview</summary>
<pre>
<img src="https://i.imgur.com/nJIX6lp.png"/>
</pre>
</details>

### Download

- [git branch](https://codeberg.org/wochap/dwl/src/branch/v0.8-a/scenefx)

- [0.8](https://codeberg.org/dwl/dwl-patches/raw/commit/494baec5b107114b74d243440aa8581fe6c03e48/patches/scenefx/scenefx.patch)

  **NOTE:** This patch was tested with the `b2e0ac4beb85aa89d0357dc8fcf8762808650890` commit on the `main` branch of `SceneFX`. It supports rounded borders, blur, and shadows.

  **IMPORTANT:** This patch requires you to build DWL with the following dependencies

  - **scenefx**
  - libGL

- [2024-07-09](https://codeberg.org/dwl/dwl-patches/raw/commit/13d96b51b54500dd24544cf3a73c61b7a1414bc6/patches/scenefx/scenefx.patch)

  **IMPORTANT:** This patch only works with the `2ec3505248e819191c37cb831197629f373326fb` commit on the `main` branch of `scenefx`, therefore, it does not support **blur**.

  **IMPORTANT:** This patch requires you to build DWL with the following dependencies

  - **scenefx**
  - libGL

  <details>
  <summary>Preview</summary>
  <pre>
  <img src="https://i.imgur.com/4kFhSaS.png"/>
  <img src="https://i.imgur.com/9ZQAUXx.png"/>
  </pre>
  </details>

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

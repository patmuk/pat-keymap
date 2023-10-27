# zmk-config

For the [Aurora Sweep](https://splitkb.com/products/aurora-sweep), a variant of the [ferris sweep](https://github.com/davidphilipbarr/Sweep), which is based on the [ferris](https://github.com/pierrechevalier83/ferris). Utilizing the cradio firmware of ZMK or QMK.

![Aurora sweep](https://cdn.shopify.com/s/files/1/0227/9171/6941/products/AUR-SWP-build-left_1620x1080.jpg?v=1665581860)
## Layout
![Alt text](Keyboard Layout)
<img src="./config/visualisation/drawn.svg">

## build
### remote (prefered)
in github -> actions -> run workflows -> build
### local
Download ZMK/app, and within this folder:
west build -b nice_nano_v2 -- -DSHIELD=pats_left -DZMK_CONFIG="./config"

## flash
1. press the reset button twice -> nice!nano mounts as folder
2. in terqminal, copy each uf2 to each half, e.g.
   1. cp firmware-pat/splitkb_aurora_sweep_right-nice_nano_v2-zmk.uf2 /Volumes/NICENANO/CURRENT.UF2
3. wait until the drive unmounts itself

## files

config/info.json:       layout for visual editors
config/visualisation/:  files to visualize the layout

## editors
Best, plantUML like:
   webapp https://caksoylar.github.io/keymap-drawer
   CLI https://github.com/caksoylar/keymap-drawer
   install with:
      brew install pipx
      pipx install keymap-drawer
      pipx ensurepath


(all work online only)

https://nickcoutsos.github.io/keymap-editor/ - an editor, which works with .keymap files. However, it doesn't show all layers at once.

http://www.keyboard-layout-editor.com/#/gists/07709e4831a3a660797160b0fc885558 - shows all layers in one picture - but doesn't work with keymap files directly

Or:
For QMK:
https://config.qmk.fm/#/ferris/sweep/LAYOUT_split_3x5_2
Convert to ZMK:
https://aaronsantiago.github.io/qmk-to-zmk/

## inspiration / credits
- https://dlip.github.io/posts/hybrid-keyboard-chording-with-zmk/
- https://github.com/rayduck/pnohty
- https://www.charachorder.com/en-ch
- https://www.youtube.com/results?search_query=ben+vallack+keyboard

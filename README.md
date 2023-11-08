# My Keyboard Layout (aka zmk-config)

For the [Aurora Sweep](https://splitkb.com/products/aurora-sweep), a variant of the [ferris sweep](https://github.com/davidphilipbarr/Sweep), which is based on the [ferris](https://github.com/pierrechevalier83/ferris). Utilizing the cradio firmware of ZMK or QMK.

![Aurora sweep](https://cdn.shopify.com/s/files/1/0227/9171/6941/products/AUR-SWP-build-left_1620x1080.jpg?v=1665581860)
## Layout
![Keyboard Layout](./config/visualisation/drawn.svg)

### Status
The Lock and Danger layers don't work - but I don't need these (now).

# How To ...
## build
### remote (prefered)
in github -> actions -> run workflows -> build
### local
Download ZMK/app, and within this folder:
west build -b nice_nano_v2 -- -DSHIELD=pats_left -DZMK_CONFIG="./config"

## flash
1. press the reset button twice -> nice!nano mounts as folder
2. copy each uf2 to each half
3. wait until the drive unmounts itself (OS complains of unclean removal, but that is no problem)

## files

config/info.json:       layout for visual editors  
config/visualisation/:  files to visualize the layout 

## editors
Best, plantUML like:  
- webapp https://caksoylar.github.io/keymap-drawer
- CLI https://github.com/caksoylar/keymap-drawer
### install with:
1. brew install pipx
2. pipx install keymap-drawer
3. pipx ensurepath


### online only

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

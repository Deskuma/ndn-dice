# nDn-dice

nDn Dice is a dice roller for Python.
It supports nDn notation.
It is a Python module. (Pending)

## Description

```python
# =============================================================================
# nDn Dice for Python
# =============================================================================
# Description:
#   nDn dice roll function
#   nDn dice format:
#       <dice>d<face>
#       <dice>d<face><extend_dice_rule|modifier|judgement_rule>
#   dice_rule:
#       <dice>d<face>
#   extended_dice_rule:
#       dice_rule + dice_rule | dice_rule - dice_rule
#   modifier:
#       +<number> or -<number>
#   judgement_rule:
#       <judgement_prefix> <judgement_number>
#   judgement_prefix:
#       >, <, =, >=, <=, !=
# e.g.
#   '1d6', '2d8', 'd4', 'd2', '2d20+5', '1d10-10', '3d6-6',
#   '1d6+2d8<=5', '1d6+2d8+1d6>20', '1d6+2d8-3d4+5d8-d114514-1919'
# output:
#   dice rule: 1d6+2d8-3d4+5d8-d114514-1919<0
#   <-- 1d6+2d8-3d4+5d8-d114514-1919<0
#   --> dice roll: -5108
#   --> history: [-1919, [-3223], [6, 7, 7, 6, 2], [-1, -2, -4], [7, 4], [2], True]
#   --> judgement: win: True
# -----------------------------------------------------------------------------
# @author: Deskuma (and Copilot)
# @version: 1.0
# @date: 2022-05-11
# @license: MIT
# @copyright: (c) 2022 Deskuma (and Copilot)
# -----------------------------------------------------------------------------
```

## Usage

```python
import ndn_dice
dice = ndn_dice.Dice()
r = dice.roll('1d6-2d8-3d4+5d8+d114514+1919>4545')
print(r)
```

## Documentation

nDn Dice is a dice roller for Python.

```text
nDn notation:
    <dice>d<face>
    <dice>d<face><extend_dice_rule|modifier|judgement_rule>

dice_rule:
    <dice>d<face>

extended_dice_rule:
    dice_rule + dice_rule | dice_rule - dice_rule

modifier:
    +<number> or -<number>

judgement_rule:
    <judgement_prefix> <judgement_number>

judgement_prefix:
    >, <, =, >=, <=, !=

e.g.
    '1d6', '2d8', 'd4', 'd2', '2d20+5', '1d10-10', '3d6-6',
    '1d6+2d8<=5', '1d6+2d8+1d6>20', '1d6+2d8-3d4+5d8-d114514-1919'

output:
    dice rule: 1d6+2d8-3d4+5d8-d114514-1919<0
    <-- 1d6+2d8-3d4+5d8-d114514-1919<0
    --> dice roll: -5108
    --> history: [-1919, [-3223], [6, 7, 7, 6, 2], [-1, -2, -4], [7, 4], [2], True]
    --> judgement: win: True
```

## License

[MIT License](LICENSE)

## Contributors

## Changelog

- 2022-05-11: v1.0 Initial release

## TODO

## References

## See Also

## Authors

Deskuma(and Copilot)

## Copyright

Copyright (c) 2022 Deskuma (and Copilot)

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
#       <dice>d<face><extend_dice_rule|modifier|judge>
#   dice_rule:
#       <dice>d<face>
#   extended_dice_rule:
#       dice_rule + dice_rule | dice_rule - dice_rule
#   modifier:
#       +<number> or -<number> or
#       *<number> or /<number> or
#       %<number> or ^<number>
#   judge:
#       <judge_prefix> <judge_number>
#   judge_prefix:
#       >, <, =, >=, <=, !=
# e.g.
#   '1d6', '2d8', 'd4', 'd2', '2d20+5', '1d10-10', '3d6-6',
#   '1d6+2d8', '1d6-2d8', '1d6+1d6', '1d6+1d6+12', '1d6+1d6-12',
#   '1d6*2', '1d6/2', '1d6%2', '1d6^2', '1d6+1d6*2', '1d6+1d6/2',
#   '1d6+2d8<=5', '1d6+2d8+1d6>20', '1d6+2d8-3d4+5d8-d114+d514%19<19'
# output:
#    dice: 1d6+2d8-3d4+5d8-d114+d514%19<19
#    roll: 2
#   judge: True
# history: [True, [4], [2, 6], [-3, -4, -3], [8, 7, 2, 7, 7], [-7], [52], '%19']
# -----------------------------------------------------------------------------
# @author: Deskuma (and GitHub Copilot)
# @version: 1.0.1
# @date: 2022-05-13
# @license: MIT
# @copyright: (c) 2022 Deskuma (and GitHub Copilot)
# -----------------------------------------------------------------------------
```

## Usage

```python
import ndice
dice = ndice.Dice()
r = dice.roll('1d6+2d8<10')
print(r)
```

```python
>>> import ndice
>>> dice = ndice.Dice('1d6+2d8<10').roll()
>>> dice
{'result': 20, 'dice': '1d6+2d8<10', 'history': [False, [5], [8, 7]], 'judge': False}
>>> 
```

## Documentation

nDn Dice is a dice roller for Python.

```text
nDn notation:
    <dice>d<face>
    <dice>d<face><extend_dice_rule|modifier|judge>

dice_rule:
    <dice>d<face>

extended_dice_rule:
    dice_rule + dice_rule | dice_rule - dice_rule

modifier:
    <modifier_prefix> <number>

modifier_prefix:
    +, -, *, /, %, ^

judge:
    <judge_prefix> <number>

judge_prefix:
    >, <, =, >=, <=, !=

e.g.
    '1d6', '2d8', 'd4', 'd2', '2d20+5', '1d10-10', '3d6-6',
    '1d6+2d8', '1d6-2d8', '1d6+1d6', '1d6+1d6+12', '1d6+1d6-12',
    '1d6*2', '1d6/2', '1d6%2', '1d6^2', '1d6+1d6*2', '1d6+1d6/2',
    '1d6+2d8<=5', '1d6+2d8+1d6>20', '1d6+2d8-3d4+5d8-d114+d514%19<19'

output:
   dice: 1d6+2d8-3d4+5d8-d114+d514%19<19
   roll: 2
  judge: True
history: [True, [4], [2, 6], [-3, -4, -3], [8, 7, 2, 7, 7], [-7], [52], '%19']
```

## License

[MIT License](LICENSE)

## Contributors

## Changelog

- 2022-05-11: v1.0.0
  - Initial release
- 2022-05-13: v1.0.1
  - Add new modifier and judge rule
  - return to self

## TODO

## References

## See Also

Your AI pair programmer
<https://copilot.github.com/>

## Authors

Deskuma (and GitHub Copilot)

## Copyright

Copyright (c) 2022 Deskuma (and GitHub Copilot)

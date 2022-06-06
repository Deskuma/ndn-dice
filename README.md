# nDn-dice

nDn Dice is a dice roller for Python.
It supports nDn notation.
It is a Python module.

## Description

```txt
===============================================================================
nDn Dice for Python
===============================================================================
Description:
  nDn dice roll function
  nDn dice format:
      <dice>d<face>
      <dice>d<face><extend_dice_rule|modifier|judge>
  dice_rule:
      <dice>d<face>
  extended_dice_rule:
      dice_rule + dice_rule | dice_rule - dice_rule
  modifier:
      <modifier_prefix><number>
  modifier_prefix:
      +, -, *, /, %, ^
  judge:
      <judge_prefix><number>
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
-------------------------------------------------------------------------------
@author: Deskuma (and GitHub Copilot)
@version: 1.0.2a
@date: 2022-06-06
@license: MIT, BEER-WARE LICENSE
@copyright: (c) 2022 Deskuma (and GitHub Copilot)
-------------------------------------------------------------------------------
```

## Installation

```bash
pip install git+https://github.com/Deskuma/ndn-dice
```

## Usage

### shell

```sh
python -m ndice
```

### Python

```python
import ndice
dice = ndice.Dice()
d = dice.roll('1d6+2d8<10')
print(d)
# dice: 1d6+2d8<10, result: 10, judge: False, history: [False, [3], [5, 2]]
r = d.get_result()
print(r)
# 10
```

```python
>>> import ndice
>>> dice = ndice.Dice('1d6+2d8<10').roll()
>>> dice
dice: 1d6+2d8<10, result: 9, judge: True, history: [True, [1], [5, 3]]
>>>
>>> # get result hash table
>>> dice.get_result_hash()
{'result': 9, 'dice': '1d6+2d8<10', 'history': [True, [1], [5, 3]], 'judge': True}
>>> dice.get_result_hash()['history']
[True, [1], [5, 3]]
>>> dice.get_result_hash()['judge']
True
>>> # reroll dice
>>> dice.roll()
dice: 1d6+2d8<10, result: 14, judge: False, history: [False, [6], [5, 3]]
>>> dice.roll()
dice: 1d6+2d8<10, result: 16, judge: False, history: [False, [3], [7, 6]]
>>> dice.roll()
dice: 1d6+2d8<10, result: 13, judge: False, history: [False, [5], [2, 6]]
```

## Source Code

```bash
git clone https://github.com/Deskuma/ndn-dice.git
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

[MIT License, BEER-WARE](LICENSE)

## Contributors

## Changelog

- 2022-06-06: v1.0.2a
  - dice shell command
  - numpy random support (experimental)
  - Test cases & Unit tests
  - refactored
- 2022-05-13: v1.0.1
  - Add new modifier and judge rule
  - return to self
- 2022-05-11: v1.0.0
  - Initial release

## TODO

- Examples

## References

## See Also

Your AI pair programmer
<https://copilot.github.com/>

## Authors

Deskuma (and GitHub Copilot)

## Copyright

Copyright (c) 2022 Deskuma (and GitHub Copilot)

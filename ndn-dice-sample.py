#!/usr/bin/python3
# -*- coding: utf-8 -*-

# -----------------------------------------------------------------------------
# nDn Dice for Python
# -----------------------------------------------------------------------------
import ndice

# -----------------------------------------------------------------------------
# Use case: 1
dice = ndice.Dice()
r = dice.roll('3d6')
print(r)
r = dice.roll('5d6<=15')
print(r)
r = dice.roll('3d6-3d8+3=13')
print(r)
# e.g.
# dice: 3d6, result: 4, judge: None, history: [[2, 1, 1]]
# dice: 5d6<=15, result: 20, judge: False, history: [False, [3, 4, 5, 2, 6]]
# dice: 3d6-3d8+3=13, result: -6, judge: False, history: [False, [5, 3, 1], [-5, -5, -8], '+3']
print()

# -----------------------------------------------------------------------------
# Use case: 2
dice = ndice.Dice('3d6-2d6+6>=15')
for _ in range(5):
    r = dice.roll()
    print(r)
# e.g.
# dice: 3d6-2d6+6>=15, result: 11, judge: False, history: [False, [2, 6, 6], [-6, -3], '+6']
# dice: 3d6-2d6+6>=15, result: 7, judge: False, history: [False, [1, 5, 3], [-3, -5], '+6']
# dice: 3d6-2d6+6>=15, result: 16, judge: True, history: [True, [6, 6, 2], [-3, -1], '+6']
# dice: 3d6-2d6+6>=15, result: 4, judge: False, history: [False, [3, 2, 2], [-5, -4], '+6']
# dice: 3d6-2d6+6>=15, result: 16, judge: True, history: [True, [5, 6, 6], [-4, -3], '+6']
print()

# -----------------------------------------------------------------------------
# Use case: 3
dice = ndice.Dice()
dice.set_dice_rule('3d6-2d6*2<5')
print('dice>', dice.get_dice_rule())
for i in range(5):
    dice.roll()
    print('%d: roll=%d, judge=%s' % (i+1, dice.get_result(), dice.get_judge()))
# e.g.
# dice> 3d6-2d6*2<5
# 1: roll=2, judge=True
# 2: roll=7, judge=False
# 3: roll=-4, judge=True
# 4: roll=7, judge=False
# 5: roll=-2, judge=True
print()

# -----------------------------------------------------------------------------
# Use case: 4
res = ndice.Dice('3d6').roll().to_get_all()
print('result:', res)
# e.g.
# result: {'result': 7, 'dice': '3d6', 'history': [[3, 3, 1]], 'judge': None}
print()

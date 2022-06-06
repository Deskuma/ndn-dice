#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import unittest
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from ndice import Dice

class TestDice(unittest.TestCase):
    """### nDn Dice: Unit Test ###"""
    def test_dice_roll(self):
        self.__dice_roll_test__()

    # def test_basic(self):
    #     __basic_test__()

    # def test_eg(self):
    #     __eg_test__()

    def __thread_dice__(self, ndn, min, max):
        """
        Test: 1d6 Thread Pool Executor (Thread safe)
        """
        dice = Dice(ndn)
        for _ in range(100):
            r = dice.roll().get_result()
            self.assertTrue(r >= min and r <= max)

    def __dice_roll_test__(self):
        """Test"""
        works = 32
        # 128 Hundred dice roll
        with ThreadPoolExecutor(max_workers=works) as tpe:
            for _ in range(128):
                # e.g. 1d6+3
                # r = dice.roll("1d6+3").get_result()
                # self.assertTrue(r >= 4 and r <= 9)
                tpe.submit(self.__thread_dice__, "1d6", 1, 6)

        # 128 Hundred dice roll with modifier
        with ThreadPoolExecutor(max_workers=works) as tpe:
            for _ in range(128):
                # e.g. 1d6+3
                # r = dice.roll("1d6+3").get_result()
                # self.assertTrue(r >= 4 and r <= 9)
                tpe.submit(self.__thread_dice__, "1d6+3", 4, 9)

        # 128 Hundred dice roll with multiple dice
        with ThreadPoolExecutor(max_workers=works) as tpe:
            for _ in range(128):
                # e.g. 1d6+2d8
                # r = dice.roll("1d6+2d8").get_result()  # 3 <= 1d6+2d8 <= 22
                # self.assertTrue(r >= 3 and r <= 22)
                tpe.submit(self.__thread_dice__, "1d6+2d8", 3, 22)


def __eg_test__():
    """Test"""
    dice = Dice(debug=True)

    eg_rules = [
        "1d6",
        "2d8",
        "d4",
        "d2",
        "2d20+5",
        "1d10-10",
        "3d6-6",
        "1d6+2d8",
        "1d6-2d8",
        "1d6+1d6",
        "1d6+1d6+12",
        "1d6+1d6-12",
        "1d6*2",
        "1d6/2",
        "1d6%2",
        "1d6^2",
        "1d6+1d6*2",
        "1d6+1d6/2",
        "1d6+2d8<=5",
        "1d6+2d8+1d6>20",
        "1d6+2d8-3d4+5d8-d114+d514%19<19",
    ]

    for rule in eg_rules:
        print("nDn-->:", rule)
        res = dice.roll(rule)
        print("result:", res)


def __basic_test__():
    """Test"""
    dice_rules = [
        "1d6",
        "1d6+3",
        "1d6-3",
        "1d6+1d6",
        "1d6+1d6+12",
        "1d6+1d6-12",
        "1d6+1d6*2",
        "1d6+1d6/2",
        "1d6>3",
        "1d6<3",
        "1d6=3",
        "1d6!=3",
        "1d6>=3",
        "1d6<=3",
        "1d6+2d4-3d8-4d10+5d20-d100>3",
    ]
    dice = Dice(debug=True)
    # normal dice roll
    try:
        dice.roll("1d6")
        dice.roll("2d8")
        dice.roll("d4")
    except Exception as e:
        print(e)

    # dice roll with modifier
    try:
        dice.roll("2d20+5")
        dice.roll("1d10-10")
        dice.roll("3d6-6")
    except Exception as e:
        print(e)

    # dice roll with multiple dice
    try:
        dice.roll("1d6+2d8")
        dice.roll("1d6-2d8")
    except Exception as e:
        print(e)

    # dice roll with multiple dice and modifiers
    try:
        dice.roll("1d6+2d8-3d4+5d8-d114514-1919")
        dice.roll("1d6+2d8-3d4+5d8-d114514+1919")
    except Exception as e:
        print(e)

    # not a dice rule
    try:
        dice.roll("foo+bar-hoge>=fuga")
    except Exception as e:
        print(e)

        # dice roll with judgement
        dice.roll("3d6>9")
        dice.roll("3d6<9")
        dice.roll("3d6=9")
        dice.roll("3d6!=9")
        dice.roll("3d6>=9")
        dice.roll("3d6<=9")

        dice.roll("3d6+3>9")
        dice.roll("3d6+3<9")
        dice.roll("3d6+3=9")
        dice.roll("3d6+3!=9")
        dice.roll("3d6+3>=9")
        dice.roll("3d6+3<=9")

        dice.roll("3d6+4d4+3>9")

        for rule in dice_rules:
            print("nDn-->:", rule)
            res = dice.roll(rule)
            print("result:", res)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
    # ____dice_roll_test____()
    # __eg_test__()
    # __basic_test__()
    # print("test passed")
    # exit(0)

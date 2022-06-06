# -*- coding: utf-8 -*-
# Path: Python/nDn-dice/ndice/ndn_class_ver.py
"""nDn Dice for Python is a Python module for rolling dice."""

import re
import random

np = None
try:
    import numpy as np
except ImportError:
    pass

__version__ = "1.0.2a"
____module = "ndice"
____description = "nDn Dice for Python is a Python module for rolling dice."
____implement = "class Dice"


class Dice:
    """
    ===========================================================================
    nDn Dice for Python
    ===========================================================================
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
    ---------------------------------------------------------------------------
    @author: Deskuma (and GitHub Copilot)
    @version: 1.0.2a
    @date: 2022-05-13
    @update: 2022-06-06
    @license: MIT, BEER WARE
    @copyright: (c) 2022 Deskuma (and GitHub Copilot)
    ---------------------------------------------------------------------------
    """

    # -------------------------------------------------------------------------
    # Constructor
    # -------------------------------------------------------------------------
    VERSION = __version__
    ALGO_RANDOM = "random"
    ALGO_NUMPY = "numpy"
    __ALGORITHMS = {ALGO_RANDOM, ALGO_NUMPY}

    def __init__(self, ndn=None, seed=None, algo=ALGO_RANDOM, debug=None):
        """Initialize"""
        self.__reset()  # constructor
        if ndn is not None:
            self.set_dice_rule(ndn)
        self.__set_seed(seed)
        if algo is not None:
            self.__set_algorithm(algo)

        self._DICE_DEBUG_ = False if debug is None else debug

    # -------------------------------------------------------------------------
    # Constants
    # -------------------------------------------------------------------------
    KEY_RESULT = "result"
    KEY_DICE = "dice"
    KEY_HISTORY = "history"
    KEY_JUDGE = "judge"
    KEY_ALGO = "algo"
    KEY_SEED = "seed"
    # Dice rule pattern (dice_rule) and extended dice rule pattern (extended_dice_rule)
    # dice_rule_pattern = re.compile(r'^(\d+)d(\d+)$')
    # dice and rule pattern
    # dice, face, modifier, judge
    # e.g. '1d6', '2d8', 'd4', '2d20+5', '1d10-10', '3d6-6',
    #      '1d6+2d8', '1d6+2d8+1d6',
    #      '+2d8', '-2d8', '+2d8+5', '-2d8-5'
    regex_dice_rule = re.compile(r"([+-]*\d*)d(\d+)([\+\-\%\*\^\/].+)?", re.I)
    # judge rule pattern
    # judge rule:
    # e.g. 'dice_rule>9', 'dice_rule<9', 'dice_rule=9', 'dice_rule!=9', 'dice_rule>=9', 'dice_rule<=9'
    regex_judge = re.compile(r"(.*\d)(>|<|=|!=|>=|<=)(\d+)", re.I)
    # match modifier pattern:
    # e.g. '10', '-10', '+10', '*10', '/10', '%10', '^10'
    regex_modifier = re.compile(r"^[\+\-\%\*\^\/]?\d+$")

    # Template method
    def ____template____(self):
        self.____dbg(["<-> str"])  # debug

    # -------------------------------------------------------------------------
    # Public methods
    # -------------------------------------------------------------------------
    def roll(self, dice_rule=None):
        """
        Roll dice according to the dice rule.
        :param dice_rule: dice rule: <dice>d<face>+<dice_rule|modifier|judge_rule>
        :return: self
        """
        ndn = dice_rule if dice_rule is not None else self.__dice_rule
        self.____dbg(["<-- __ndn_roll:", ndn])

        # initialize
        self.__reset()  # initialize
        self.set_dice_rule(ndn)
        # roll dice
        self.__ndn_roll(ndn)
        self.____dbg(["--> __ndn_roll: hist:", self.get_history()])
        # roll result
        self.__update_result()
        return self

    def to_get_all(self):
        """
        Get all properties.
        :return: all result to hash
        """
        return self.get_result_hash()

    def get_result_hash(self):
        """Get result hash table"""
        # Hash table containing 'result', 'dice', 'history', and 'judge'
        return {
            self.KEY_RESULT: self.get_result(),
            self.KEY_DICE: self.get_dice(),
            self.KEY_HISTORY: self.get_history(),
            self.KEY_JUDGE: self.get_judge(),
            self.KEY_ALGO: self.get_algorithm(),
            self.KEY_SEED: self.get_seed(),
        }

    # -------------------------------------------------------------------------
    # Private methods
    # -------------------------------------------------------------------------
    def __clear_dice_rule(self):
        """Clear dice rule"""
        self.__dice_rule = ""

    def __check_dice_rule(self, ndn=None):
        """Check dice rule"""

        if self.__dice_rule is None:
            self.__dice_rule = ""

        rule = ndn if ndn else self.__dice_rule

        match = self.regex_dice_rule.match(rule)
        if match is None:
            raise ValueError("Invalid dice rule: {}".format(rule))

        return match is not None

    def __check_history(self):
        """Check history"""
        if self.__history is None:
            self.__clear_history()

    def __history_append(self, list):
        """Append history"""
        self.__check_history()
        self.__history.append(list)

    def __clear_history(self):
        """Clear history"""
        self.__history = []

    def __clear_result(self):
        """Clear result"""
        self.__result = 0

    def __clear_judge(self):
        """Clear judge"""
        self.__judge = None

    def __reset(self):
        """Reset"""
        self.__clear_dice_rule()
        self.__clear_history()
        self.__clear_result()
        self.__clear_judge()

    def __is_number(self, s):
        """Check if string is number"""
        return self.regex_modifier.match(s) is not None

    def __is_judge_rule(self, s):
        """Check if string is judge rule"""
        return self.regex_judge.match(s) is not None

    def __get_reverse_history(self):
        """Get reverse history"""
        self.__check_history()
        return self.__history[::-1]

    def __calc_result(self, history=None):
        """Calculate result"""
        self.____dbg(["<-- calc_result"])  # debug
        if history is None:
            history = self.get_history()
        result = 0
        for i in history:
            if type(i) is int:
                # Don't use isinstance()!
                # bool is a subclass of int
                self.____dbg(["--- int: {}".format(i)])  # debug
                # This is not a current spec...
                # result += i
            elif isinstance(i, list):
                self.____dbg(["--- list: {}".format(i)])  # debug
                result += sum(i)
            elif isinstance(i, str):
                self.____dbg(["--- str: {}".format(i)])  # debug
                prefix = i[0]
                num = int(i[1:])
                if prefix == "+":
                    result += num
                elif prefix == "-":
                    result -= num
                elif prefix == "*":
                    result *= num
                elif prefix == "/":
                    result /= num
                elif prefix == "%":
                    result %= num
                elif prefix == "^":
                    result **= num
                else:
                    msg = "Invalid prefix: {}".format(prefix)
                    raise ValueError(msg + "\n" + str(history))
        self.____dbg(["--> calc_result: {}".format(result)])  # debug
        return result

    def __update_result(self, history=None):
        """Set result"""
        history = history if history else self.__history
        self.____dbg(["<-- update_result: {}".format(history)])  # debug
        self.__result = self.__calc_result(history)
        self.____dbg(["--- calc: {}".format(self.__result)])  # debug
        # Process other results
        for i in history:
            if type(i) is bool:  # judge
                self.____dbg(["--- bool:", i])
                # Already set...
                # self.__judge = i
                pass
            elif type(i) is tuple:  # This is error message
                self.____dbg(["--- tuple:", i])
                self.__result = i
                break

    def __after_judge(self, prefix, number):
        """Judge result"""
        res = self.__calc_result()
        self.____dbg(["<-> judge:", res, prefix, number])
        if prefix == ">":
            return res > number
        elif prefix == "<":
            return res < number
        elif prefix == "=":
            return res == number
        elif prefix == "!=":
            return res != number
        elif prefix == ">=":
            return res >= number
        elif prefix == "<=":
            return res <= number
        else:
            return False

    def __str__(self):
        """Return string"""
        return "dice: %s, result: %d, judge: %s, history: %s" % (
            self.get_dice(),
            self.get_result(),
            self.get_judge(),
            self.get_history(),
        )

    def __repr__(self):
        """Return string"""
        return self.__str__()

    def ____dbg(self, list, force=False):
        """Print debug message"""
        if self._DICE_DEBUG_ or force:
            print("dbg:", list)

    def __dice_random(self, dice_num, dice_face):
        """Random dice"""
        self.____dbg(["<-- dice_random"])
        result = []
        loop = abs(dice_num)
        neg = -1 if dice_num < 0 else 1
        for _ in range(loop):
            if self.__algorithm == Dice.ALGO_RANDOM:
                result.append(random.randint(1, dice_face) * neg)
            elif self.__algorithm == Dice.ALGO_NUMPY:
                result.append(np.random.randint(1, dice_face) * neg)
            else:
                raise ValueError("Invalid algorithm: {}".format(self.__algorithm))
        self.____dbg(["--> dice_random:", result])
        return result

    def __ndn_roll(self, dice_rule):
        """Roll dice"""
        # ---------------------------------------------------------------------
        # Initialize
        # ---------------------------------------------------------------------

        # ---------------------------------------------------------------------
        # pre check nDn dice rule
        # ---------------------------------------------------------------------
        # If it starts with '-d', 'd', complete 1
        if dice_rule.startswith("-d"):
            dice_rule = "-1" + dice_rule[1:]
        elif dice_rule.startswith("d"):
            dice_rule = "1" + dice_rule
        # If there is no sign at the beginning, add '+'.
        if not dice_rule.startswith("+") and not dice_rule.startswith("-"):
            dice_rule = "+" + dice_rule

        # match judge rule and dice rule pattern
        judge = self.regex_judge.match(dice_rule)
        rule = judge.group(1) if judge else dice_rule
        judge_prefix = judge.group(2) if judge else None
        judge_number = judge.group(3) if judge_prefix else None
        self.____dbg(
            [
                "--- judge:",
                judge is not None,
                "rule:",
                rule,
                "judge_prefix:",
                judge_prefix,
                "judge_number:",
                judge_number,
            ]
        )

        # match dice rule pattern
        ndfem = self.regex_dice_rule.match(rule)
        if ndfem is None:
            # Invalid dice rule
            self.__history_append(("dice_rule is not valid", rule))
            self.__reset()  # dice rule failed
            return

        dn = ndfem.group(1)  # dice number e.g. '2d6' -> '2'
        df = ndfem.group(2)  # dice face e.g. '2d6' -> '6'
        de = ndfem.group(3)  # dice extended, modifier, (judge?)

        # format dn: '+' -> '1', '-' -> '-1', '+1' -> '1', '-1' -> '-1', '1' -> '1'
        dn = int("-1" if dn == "-" else "1" if dn == "+" else dn)
        df = int(df)
        de = de if de else ""

        self.____dbg(["--- dn:", dn, "df:", df, "de:", de])

        dice_numb = dn  # dice number
        dice_face = df  # dice face
        dice_extn = de  # dice extended, modifier, judge

        # ---------------------------------------------------------------------
        # dice extended
        # ---------------------------------------------------------------------
        if self.regex_dice_rule.match(dice_extn):
            # recursive call
            self.__ndn_roll(dice_extn)
            dice_extn = ""

        # ---------------------------------------------------------------------
        # roll dice
        # ---------------------------------------------------------------------
        self.____dbg(["<-- roll dice:", "count:", dice_numb, "face:", dice_face])
        loc_hist = self.__dice_random(dice_numb, dice_face)
        self.____dbg(["--> roll dice"])

        # ---------------------------------------------------------------------
        # modifier
        # ---------------------------------------------------------------------
        if self.regex_modifier.match(dice_extn):
            self.____dbg(["<-> modifier:", dice_extn])
            self.__history_append(dice_extn)

        # append history
        self.____dbg(
            ["<-> append history:", (loc_hist, sum(loc_hist)), "=>", self.get_history()]
        )
        self.__history_append(loc_hist)

        # ---------------------------------------------------------------------
        # judge
        # ---------------------------------------------------------------------
        if judge is not None:
            self.____dbg(["<-- judge:", judge_prefix, judge_number])
            self.__set_judge(self.__after_judge(judge_prefix, int(judge_number)))
            res = self.get_judge()
            self.__history_append(res)
            self.____dbg(["--> judge:", res])
        else:
            self.__set_judge(None)

    # -------------------------------------------------------------------------
    # getters and setters
    # -------------------------------------------------------------------------

    def set_dice_rule(self, dice_rule):
        """Set dice rule"""
        self.__check_dice_rule(dice_rule)
        self.__dice_rule = dice_rule

    def get_dice(self):
        """Get dice"""
        return self.get_dice_rule()

    def get_dice_rule(self):
        """Get dice rule"""
        return self.__dice_rule

    def get_result(self):
        """Get result"""
        return self.__result

    def get_history(self):
        """Get history"""
        return self.__get_reverse_history()

    def get_judge(self):
        """Get judge"""
        return self.__judge

    def __set_judge(self, judge):
        """Set judge"""
        self.__judge = judge

    def get_algorithm(self):
        """Get algorithm"""
        return self.__algorithm

    def __set_algorithm(self, algorithm):
        """Set algorithm"""
        # validation
        if algorithm not in self.__ALGORITHMS:
            raise ValueError("unknown algorithm: %s" % algorithm)
        self.__algorithm = algorithm
        # set seed
        if self.__algorithm == Dice.ALGO_RANDOM:
            random.seed(self.__seed)
        elif self.__algorithm == Dice.ALGO_NUMPY:
            if np is None or np.random is None:
                raise ValueError("numpy is not installed")
            np.random.seed(self.__seed)

    def get_seed(self):
        """Get seed"""
        return self.__seed

    def __set_seed(self, seed):
        """Set seed"""
        self.__seed = seed

    def get_version(self):
        """Get version"""
        return self.VERSION

    # -------------------------------------------------------------------------
    # self test
    # -------------------------------------------------------------------------

    def test(self):
        """Self Test"""
        print("self test mode")
        print("-> split: dice_rule")
        print("-- [*pending*] not implemented")
        print("<- end of self test")

    # -- end of class ---------------------------------------------------------


def dice_shell():
    __DICE_DEBUG__ = False

    dice = Dice(debug=__DICE_DEBUG__)

    print("nDn Dice Roller: Command Line Interface (CLI)")
    print("nDn Dice ver.%s" % dice.get_version())
    print('Usage: Ctrl-C or type "quit/exit" to exit')
    print('Usage: "help" to show help')
    usage_msg = """\
Usage:
  "algo"             to show algorithm
  "algo <algorithm>" to set algorithm
    algorithms:
        random     : built-in random
        numpy      : numpy.random (numpy is required)

  "seed"             to show seed
  "seed <seed>"      to set seed

  "!test"            to run self test
  "!debug"           to toggle debug mode

  "exit" or "quit"   to exit

  <dice_rule>        to roll dice
                     e.g. "1d6", "2d6-1d6", "-1d6+1", "d2", "-d100"
                          "1d6*2", "1d6/2", "1d100%25", "d4^2"

  [enter]            to reroll dice
-------: ------------------------------
"""
    while True:
        ndn = input("nDice> ")
        (ndn, *param) = ndn.split(" ")
        res = None
        try:
            if ndn == "quit" or ndn == "exit":
                break
            elif ndn == "help":
                print(usage_msg)
                continue
            elif ndn == "algo":
                if len(param) == 0:
                    print("get algorithm:", dice.get_algorithm())
                    continue
                else:
                    dice = Dice(debug=__DICE_DEBUG__, algo=param[0])
                    print("set algorithm:", dice.get_algorithm())
                    continue
            elif ndn == "seed":
                print("Note: Seed value changes only for built-in random algorithm")
                if len(param) == 0:
                    print("get seed:", dice.get_seed())
                    continue
                else:
                    dice = Dice(debug=__DICE_DEBUG__, seed=param[0])
                    print("set seed:", dice.get_seed())
                    continue
            elif ndn == "!test":
                dice.test()
                continue
            elif ndn == "!debug":
                __DICE_DEBUG__ = not __DICE_DEBUG__
                dice = Dice(debug=__DICE_DEBUG__)
                continue
            elif ndn == "":
                res = dice.roll()
            else:
                res = dice.roll(ndn)

            if res is not None:
                print(" result:", res) if __DICE_DEBUG__ else None
                print("   dice:", ndn if ndn else dice.get_dice_rule())
                print("   roll:", dice.get_result())
                print("  judge:", dice.get_judge())
                print("history:", dice.get_history())
                print("-------:", "-" * 20)
        except Exception as e:
            print(e)


# =============================================================================
# main
# nDn Dice Roller Command Line Interface (CLI)
# =============================================================================
def __main__():
    dice_shell()


if __name__ == "__main__":
    dice_shell()

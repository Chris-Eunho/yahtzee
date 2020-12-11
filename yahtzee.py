import random
import copy


def show_result(score_sheets: list) -> None:
    """Show the result of the game.

    A function that interprets two player's finished score sheets and shows the result of the game.

    :param score_sheets: A list that contains two dictionaries of score sheets.
    :precondiotion: The format of element dictionaries should be as following
                   {"name": str, "Ones": score, "Twos": score, "Threes": score, "Fours": score,
                   "Fives": score, "Sixes": score, "Three of a kind": score, "Four of a kind": score,
                   "Full House": score, "Small straight": score, "Large straight": score, "Chance": score,
                   "Yahtzee": score, "Yahtzee count": count}
                   The values named 'score' should be integer.
   :postcondition: N/A
    :return: N/A

    #Can not unittest or doctest this function because it will be an integrated function which uses multiple functions.
    """


def calculate_total_score(score_sheet: dict) -> int:
    """Calculate total score from score sheet.

    A function that calculates total score of given score sheet.


    :param score_sheet: A fully written score sheet to calculate total score.
    :precondition: The format of the dictionary should be as following
                   {"name": str, "Ones": score, "Twos": score, "Threes": score, "Fours": score,
                   "Fives": score, "Sixes": score, "Three of a kind": score, "Four of a kind": score,
                   "Full House": score, "Small straight": score, "Large straight": score, "Chance": score,
                   "Yahtzee": score, "Yahtzee count": count}
                   The values named 'score' should be integer.
    :postcondtion: Correctly returns the calculated total score.
    :return: The total score from score_sheet


    >>> print(calculate_total_score(sample_score_sheet())) #upper section bonus
    254
    >>> print(calculate_total_score(sample_score_sheet_two())) #no upper section bonus
    221
    """


def calculate_ones(dice_set: list) -> int:
    """Calculate points of Ones.

    A function that calculates the points of Ones when written with dice_set.

    :param dice_set: A set of dice that user wants to use to write Ones.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Ones when written with dice_set.
    :return: Calculated points of Ones when written with dice_set.

    >>> print(calculate_ones(["5", "2", "3", "4", "6"]))
    0

    >>> print(calculate_ones(["1", "2", "3", "4", "5"]))
    1

    >>> print(calculate_ones(["1", "1", "3", "5", "5"]))
    2

    >>> print(calculate_ones(["1", "1", "1", "5", "5"]))
    3

    >>> print(calculate_ones(["1", "1", "1", "1", "1"]))
    4

    >>> print(calculate_ones(["1", "1", "1", "1", "1"]))
    5

    """


def calculate_twos(dice_set: list) -> int:
    """Calculate points of Twos.

    A function that calculates the points of Twos when written with dice_set.

    :param dice_set: A set of dice that user wants to use to write Twos.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Twos when written with dice_set.
    :return: Calculated points of Twos when written with dice_set.

    >>> print(calculate_twos(["1", "5", "3", "4", "6"]))
    0

    >>> print(calculate_twos(["1", "2", "3", "4", "5"]))
    2

    >>> print(calculate_twos(["2", "2", "3", "5", "5"]))
    4

    >>> print(calculate_twos(["2", "2", "2", "5", "5"]))
    6

    >>> print(calculate_twos(["1", "2", "2", "2", "2"]))
    8

    >>> print(calculate_twos(["2", "2", "2", "2", "2"]))
    10

    """


def calculate_threes(dice_set: list) -> int:
    """Calculate points of Threes.

    A function that calculates the points of Threes when written with dice_set.

    :param dice_set: A set of dice that user wants to use to write Threes.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Threes when written with dice_set.
    :return: Calculated points of Threes when written with dice_set.

    >>> print(calculate_threes(["1", "2", "5", "4", "6"]))
    0

    >>> print(calculate_threes(["1", "2", "3", "4", "5"]))
    3

    >>> print(calculate_threes(["1", "3", "3", "5", "5"]))
    6

    >>> print(calculate_threes(["1", "2", "3", "3", "3"]))
    9

    >>> print(calculate_threes(["1", "3", "3", "3", "3"]))
    12

    >>> print(calculate_threes(["3", "3", "3", "3", "3"]))
    15

    """


def calculate_fours(dice_set: list) -> int:
    """Calculate points of Fours.

    A function that calculates the points of Fours when written with dice_set.

    :param dice_set: A set of dice that user wants to use to write Fours.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Fours when written with dice_set.
    :return: Calculated points of Fours when written with dice_set.

    >>> print(calculate_fives(["1", "2", "3", "5", "6"]))
    0

    >>> print(calculate_fives(["1", "2", "3", "4", "5"]))
    4

    >>> print(calculate_fives(["1", "2", "3", "4", "4"]))
    8

    >>> print(calculate_fives(["1", "2", "4", "4", "4"]))
    12

    >>> print(calculate_fives(["1", "4", "4", "4", "4"]))
    16

    >>> print(calculate_fives(["4", "4", "4", "4", "4"]))
    20

    """


def calculate_fives(dice_set: list) -> int:
    """Calculate points of Fives.

    A function that calculates the points of Fives when written with dice_set.

    :param dice_set: A set of dice that user wants to use to write Fives.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Fives when written with dice_set.
    :return: Calculated points of Fives when written with dice_set.

    >>> print(calculate_fives(["1", "2", "3", "4", "6"]))
    0

    >>> print(calculate_fives(["1", "2", "3", "4", "5"]))
    5

    >>> print(calculate_fives(["1", "2", "3", "5", "5"]))
    10

    >>> print(calculate_fives(["1", "2", "5", "5", "5"]))
    15

    >>> print(calculate_fives(["1", "5", "5", "5", "5"]))
    15

    >>> print(calculate_fives(["5", "5", "5", "5", "5"]))
    25


    """


def dice_sum(dice_set: list) -> int:
    """Calculate the sum of dice.

    A function that calculates the sum of a dice set in a list format.

    :param dice_set: A set of dice to calculate sum of.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate sum of elements of dice_set.
    :return: sum of elements of dice_set

    >>> print(dice_sum(["1", "2", "3", "4", "5"]))
    15

    >>> print(dice_sum(["1", "1", "1", "1", "1"]))
    5

    >>> print(dice_sum(["1", "3", "3", "4", "4"]))
    15



    """


def calculate_sixes(dice_set: list) -> int:
    """Calculate points of Sixes.

    A function that calculates the points of Sixes when written with dice_set.

    :param dice_set: A set of dice that user wants to use to write Sixes.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Sixes when written with dice_set.
    :return: Calculated points of Sixes when written with dice_set.

    >>> print(calculate_fives(["1", "2", "3", "4", "5"]))
    0

    >>> print(calculate_fives(["1", "2", "3", "4", "6"]))
    6

    >>> print(calculate_fives(["1", "2", "3", "6", "6"]))
    12

    >>> print(calculate_fives(["1", "2", "6", "6", "6"]))
    18

    >>> print(calculate_fives(["1", "6", "6", "6", "6"]))
    24

    >>> print(calculate_fives(["5", "6", "6", "6", "6"]))
    30
    """


def calculate_three_kind(dice_set: list) -> int:
    """Calculate points of Three of a kind.

    A function that calculates the points of Three of a kind when written with dice_set.

    :param dice_set: A set of dice that user wants to use to write Three of a kind.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Three of a kind when written with dice_set.
    :return: Calculated points of Three of a kind when written with dice_set.

    >>> print(calculate_three_kind(["2", "2", "2", "1", "6"]))
    13

    >>> print(calculate_three_kind(["4", "4", "4", "1", "6"]))
    19

    >>> print(calculate_three_kind(["2", "2", "2", "2", "6"]))
    16

    >>> print(calculate_three_kind(["2", "2", "2", "2", "1"]))
    11

    >>> print(calculate_three_kind(["5", "5", "5", "5", "1"]))
    21

    >>> print(calculate_three_kind(["5", "5", "5", "5", "5"]))
    25

    >>> print(calculate_three_kind(["1", "1", "1", "1", "1"]))
    5

    >>> print(calculate_three_kind(["2", "2", "3", "1", "1"]))
    0

    >>> print(calculate_three_kind(["1", "2", "3", "4", "5"]))
    0

    """


def calculate_four_kind(dice_set: list) -> int:
    """Calculate points of Four of a kind.

    A function that calculates the points of Four of a kind when written with dice_set.

    :param dice_set: A set of dice that user wants to use to write Four of a kind.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Four of a kind when written with dice_set.
    :return: Calculated points of Four of a kind when written with dice_set.

    >>> print(calculate_four_kind(["2", "2", "2", "2", "6"]))
    16

    >>> print(calculate_four_kind(["2", "2", "2", "2", "1"]))
    11

    >>> print(calculate_four_kind(["5", "5", "5", "5", "1"]))
    21

    >>> print(calculate_four_kind(["5", "5", "1", "5", "5"])) # non-contiguous case
    21

    >>> print(calculate_four_kind(["5", "5", "5", "5", "5"]))
    25

    >>> print(calculate_four_kind(["1", "1", "1", "1", "1"]))
    5

    >>> print(calculate_four_kind(["5", "5", "5", "2", "1"]))
    0

    >>> print(calculate_four_kind(["5", "5", "5", "1", "1"]))
    0


    """


def calculate_full_house(dice_set: list) -> int:
    """Calculate points of Full House.

    A function that calculates the points of Full House when written with dice_set.

    :param dice_set: A set of dice that user wants to use to write Full House.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Full House when written with dice_set.
    :return: Calculated points of Full House when written with dice_set.

    >>> print(calculate_full_house(["2", "2", "2", "5", "5"]))
    25

    >>> print(calculate_full_house(["2", "2", "5", "5", "5"]))
    25

    >>> print(calculate_full_house(["1", "1", "3", "3", "3"]))
    25

    >>> print(calculate_full_house(["2", "2", "2", "5", "6"]))
    0

    >>> print(calculate_full_house(["1", "1", "2", "3", "3"]))
    0

    >>> print(calculate_full_house(["2", "3", "4", "5", "5"]))
    0

    """


def calculate_small_straight(dice_set: list) -> int:
    """Calculate points of Small straight.

    A function that calculates the points of Small straight when written with dice_set.

    :param dice_set: A set of dice that user wants to use to write Small straight.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Small straight when written with dice_set.
    :return: Calculated points of Small straight when written with dice_set.

    >>> print(calculate_small_straight(["2", "3", "4", "5", "5"]))
    30

    >>> print(calculate_small_straight(["2", "3", "4", "5", "6"]))
    30

    >>> print(calculate_small_straight(["1", "3", "4", "5", "6"]))
    30

    >>> print(calculate_small_straight(["1", "1", "2", "3", "4"]))
    30

    >>> print(calculate_small_straight(["1", "2", "2", "3", "4"]))
    30

    >>> print(calculate_small_straight(["2", "3", "4", "6", "6"]))
    0

    >>> print(calculate_small_straight(["1", "1", "1", "2", "3"]))
    0

    >>> print(calculate_small_straight(["2", "2", "4", "6", "6"]))
    0

    """


def calculate_large_straight(dice_set: list) -> int:
    """Calculate points of Large straight.

    A function that calculates the points of Large straight when written with dice_set.

    :param dice_set: A set of dice that user wants to use to write Large straight.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Large straight when written with dice_set.
    :return: Calculated points of Large straight when written with dice_set.

    >>> print(calculate_large_straight(["1", "2", "3", "4", "5"]))
    40

    >>> print(calculate_large_straight(["2", "3", "4", "5", "6"]))
    40

    >>> print(calculate_large_straight(["2", "3", "4", "5", "5"]))
    0

    >>> print(calculate_large_straight(["1", "3", "4", "5", "5"]))
    0

    >>> print(calculate_large_straight(["2", "2", "2", "2", "2"]))
    0

    """


def sample_score_sheet() -> dict:
    """Return a sample score sheet.

    This function is created to help doctest.
    :precondition: N/A
    :postcondtion: correctly return a sample score sheet.
    :return: A sample score sheet.
    """
    result = {"name": "player_name", "Ones": 1, "Twos": 4, "Threes": 9, "Fours": 12, "Fives": 20, "Sixes": 18,
              "Three of a kind": 16, "Four of a kind": 23, "Full House": 25, "Small straight": 30, "Large straight": 40,
              "Chance": 21, "Yahtzee": 0, "Yahtzee count": 0}
    return result


def sample_score_sheet_two() -> dict:
    """Return a sample score sheet.

    This function is created to help doctest.
    :precondition: N/A
    :postcondtion: correctly return a sample score sheet.
    :return: A sample score sheet.
    """
    result = {"name": "player_name", "Ones": 1, "Twos": 4, "Threes": 9, "Fours": 12, "Fives": 10, "Sixes": 6,
              "Three of a kind": 10, "Four of a kind": 23, "Full House": 25, "Small straight": 30, "Large straight": 40,
              "Chance": 13, "Yahtzee": 50, "Yahtzee count": 0}
    return result


def print_score(score_sheet: dict) -> None:
    """Print score sheet.

    A function that prints a dictionary of a score sheet.

    :param score_sheet: Score sheet that contains player's game data.
    :precondition: The format of the dictionary should be as following
                   {"name": str, "Ones": score, "Twos": score, "Threes": score, "Fours": score,
                   "Fives": score, "Sixes": score, "Three of a kind": score, "Four of a kind": score,
                   "Full House": score, "Small straight": score, "Large straight": score, "Chance": score,
                   "Yahtzee": score, "Yahtzee count": count}
                   The values named 'score' can be integer that player mark for the combinations of
                   corresponding keys or ' ' if the player did not mark anything yet.
    :postcondition: N/A
    :return: N/A

    >>> print_score(sample_score_sheet())
    # doctest: +NORMALIZE_WHITESPACE
    <player_name's Score Sheet>
    [1]Ones: 1	[2]Twos: 4	[3]Threes: 9	[4]Fours: 12	[5]Fives: 20	[6]Sixes: 18
    [7]Three of a kind: 16	[8]Four of a kind: 23	[9]Full House: 25	[10]Small straight: 30
    [11]Large straight: 40	[12]Chance: 21	[13]Yahtzee: 0	**Yahtzee count: 0

    >>> print_score(sample_score_sheet_two())
    # doctest: +NORMALIZE_WHITESPACE
    <player_name's Score Sheet>
    [1]Ones: 1	[2]Twos: 4	[3]Threes: 9	[4]Fours: 12	[5]Fives: 10	[6]Sixes: 6
    [7]Three of a kind: 10	[8]Four of a kind: 23	[9]Full House: 25	[10]Small straight: 30
    [11]Large straight: 40	[12]Chance: 13	[13]Yahtzee: 50	**Yahtzee count: 0
    """


def ask_combo_to_write(dice_set: list, score_sheet: dict) -> str:
    """Ask which combination to write on the score sheet.

    A function that ask user which combination to write and return the user answer.
    It validates player's answer on whether they can write on selected combination or not.
    It keeps asking until the player answers a valid answer.

    :param dice_set: A set of dice to calculate points of a combination with.
    :param score_sheet: The score sheet that player wants to write on . It contains player's score information.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
                   The format of score_sheet should be as following
                   {"name": str, "Ones": score, "Twos": score, "Threes": score, "Fours": score,
                   "Fives": score, "Sixes": score, "Three of a kind": score, "Four of a kind": score,
                   "Full House": score, "Small straight": score, "Large straight": score, "Chance": score,
                   "Yahtzee": score, "Yahtzee count": count}
                   The values named 'score' can be " " or number in string that player wrote for the combinations of
                   corresponding keys or None if the player did not mark anything yet.
    :postcondition: Correctly return a validated player's pick on which combination to write.
    :return: A combination that player chose to write.

     #Can not doctest this function because it will require user's input.
    """


def write_score(dice_set: list, score_sheet: dict) -> None:
    """Write score sheet of Yahtzee.

    A function that writes score on Yahtzee score sheet according to calculation of points based on dice_set and
    user's input. One cannot overwrite score sheet unless it's multiple yahtzee case.
    :param dice_set: A set of dice to calculate points of a combination with.
    :param score_sheet: The score sheet that player wants to write on . It contains player's score information.
    :precondition: dice_set should be a list that contains five elements, each of which is a die number in string.
                   The format of score_sheet should be as following
                   {"name": str, "Ones": score, "Twos": score, "Threes": score, "Fours": score,
                   "Fives": score, "Sixes": score, "Three of a kind": score, "Four of a kind": score,
                   "Full House": score, "Small straight": score, "Large straight": score, "Chance": score,
                   "Yahtzee": score, "Yahtzee count": count}
                   The values named 'score' can be " " or number in string that player wrote for the combinations of
                   corresponding keys or None if the player did not mark anything yet.
    :postcondition: N/A
    :return: N/A

    #Can not unittest or doctest this function because it will be an integrated function which uses multiple functions.
    """


def is_list_inclusive(including_list: list, included_list: list) -> bool:
    """Check if one list includes the other.

    A function that checks if all members of the included_list is in the including_list.
    :param including_list: A list of which elements includes the elements of included_list
    :param included_list: A list of which all elements are also included by including_list
    :precondition: both input lists should not be empty
    postcondition: correctly return whether including_list includes included_list or not.
    :return: True if including_list includes included_list and False if not.

    >>> print(is_list_inclusive(["1", "2", "3", "4", "5"],["1", "2"]))
    True
    >>> print(is_list_inclusive(["1", "2", "3", "4", "5"],["1", "1"]))
    False
    >>> print(is_list_inclusive(["1", "2"],["1", "2"]))
    True
    >>> print(is_list_inclusive(["1", "2", "3", "4", "5"],["1", "2", "6"]))
    False
    >>> print(is_list_inclusive(["1", "2"],["1", "2", "3", "4", "5"]))
    False
    >>> print(is_list_inclusive(["1", "2", "2", "4", "5"],["1", "2", "2"]))
    True
    """


def get_difference_list(list_one: list, list_two: list) -> list:
    """Get difference of two lists

    A function that returns the difference of the two lists(list_one - list_two)

    :param list_one: A bigger, including list
    :param list_two: A smaller, included list
    :precondition: list_one should include list_two. i.e. All of the elements in list_two are in list_one.
    :postcondition: Correctly return the difference list.
    :return: The difference list of the two input lists.(list_one - list_two)
    """
    result = copy.deepcopy(list_one)
    for element in list_two:
        result.remove(element)
    return result


def change_dice_to_keep(dice_dict: dict) -> dict:
    """Change dice to keep from given dice sets.

    A function that change which dice to keep from given set of dice.

    :param dice_dict: A dictionary of dice info which contains lists of all dice and dice to keep
    :precondition: dice_dict is a dictionary of two dice lists.
                   dice_dict['All'] is a list of five die numbers in string.
                   dice_dict['Keep'] is a list, all elements of which are elements of dice_dict['All']
    :postcondition: N/A
    :return: N/A

    #Can not doctest this function because it will require user's input.
    """
    dice_to_throw = get_difference_list(dice_dict['All'], dice_dict['Keep'])
    print(f"🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲Change Dice🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲\n"
          f"\nYou can first choose dice to keep from all dice you have.\n"
          f"Then you will choose dice to throw from dice you are keeping.\n\n"
          f"Enter only the numbers of the dice you want to choose.\n"
          f"e.g.) Enter \"3\" if you want to choose one die of three.\n"
          f"e.g.2) Enter \"2255\" if you want to choose two dice of two and five each.\n\n"
          f"All dice you have: {dice_dict['All']}\n"
          f"Dice you are keeping: {dice_dict['Keep']}\n"
          f"Dice you are going to throw: {dice_to_throw}\n\n"
          f"Choose dice to keep from dice you are going to throw.\n"
          f"Hit Enter key if you don't want to keep anything more.\n")
    keep_dice(dice_dict)
    un_keep_dice(dice_dict)


def keep_dice(dice_dict: dict) -> None:
    """Let player keep dice.

    A function that helps user to keep dice from dice that are not kept.

    :param dice_dict: A dictionary of dice info which contains lists of all dice and dice to keep
    :precondition: dice_dict is a dictionary of two dice lists.
                   dice_dict['All'] is a list of five die numbers in string.
                   dice_dict['Keep'] is a list, all elements of which are elements of dice_dict['All']
    :postcondition: N/A
    :return: N/A

    #Can not doctest this function because it will require user's input.
    """
    dice_to_throw = get_difference_list(dice_dict['All'], dice_dict['Keep'])
    dice_chosen = []
    while True:
        dice_chosen[:] = input("Enter dice to keep: ").strip()
        if is_list_inclusive(dice_to_throw, dice_chosen):
            dice_dict['Keep'] += dice_chosen
            print(f"Now you are going to keep {dice_dict['Keep']}")
            break
        else:
            print(f"Invalid Input. Enter dice from {dice_to_throw} without white spaces.\n"
                  f"e.g.)If you want to chose [3, 3], then enter \"33\"\n")
    print(f"Choose dice to throw from dice you are going to keep\n"
          f"Hit Enter key if you don't want to change anything.\n")


def un_keep_dice(dice_dict: dict) -> None:
    """Let player keep dice.

    A function that helps user to un-keep dice from dice that are kept.

    :param dice_dict: A dictionary of dice info which contains lists of all dice and dice to keep
    :precondition: dice_dict is a dictionary of two dice lists.
                   dice_dict['All'] is a list of five die numbers in string.
                   dice_dict['Keep'] is a list, all elements of which are elements of dice_dict['All']
    :postcondition: N/A
    :return: N/A

    #Can not doctest this function because it will require user's input.
    """
    dice_chosen = []
    while True:
        dice_chosen[:] = input("Enter dice to throw: ").strip()
        if is_list_inclusive(dice_dict['Keep'], dice_chosen):
            dice_dict['Keep'] = get_difference_list(dice_dict['Keep'], dice_chosen)
            print(f"Now you are going to keep {dice_dict['Keep']} and throw {5 - len(dice_dict['Keep'])} new dice")
            break
        else:
            print(f"Invalid Input. Enter dice from {dice_dict['Keep']} without white spaces.\n"
                  f"e.g.)If you want to chose [3, 3], then enter \"33\"\n")


def get_difference_list(list_one: list, list_two: list) -> list:
    """Get difference of two lists

    A function that returns the difference of the two lists(list_one - list_two)

    :param list_one: A bigger, including list
    :param list_two: A smaller, included list
    :precondition: list_one should include list_two. i.e. All of the elements in list_two are in list_one.
    :postcondition: Correctly return the difference list.
    :return: The difference list of the two input lists.(list_one - list_two)

    >>> print(get_difference_list(['1','2','3','4','5'] - ['1','2','3']))
    ['4','5']

    >>> print(get_difference_list(['1','2','3','4','5'] - ['1','2','3','4','5']))
    []

    >>> print(get_difference_list(['1','2','3','4','5'] - []))
    ['1','2','3','4','5']

    >>> print(get_difference_list(['1','1','1','3','3'] - ['1','3']))
    ['1','1','3']

    """
    result = copy.deepcopy(list_one)
    for element in list_two:
        result.remove(element)
    return result


def throw_dice(dice_dict: dict) -> None:
    """Throw dice(or a die).

    A function that assign new dice list to user's current dice list based on the dice the user keeps

    :param dice_dict: A list of dice(die) that user wants to keep.
    :precondition: A dictionary of two dice lists.
                   dice_dict['All'] is a list of five die numbers in string.
                   dice_dict['Keep'] is a list, all elements of which are elements of dice_dict['All']
    :postcondition: N/A
    :return: N/A

    #Can not doctest this function because it will generate random value(s)
    """
    result = copy.deepcopy(dice_dict["Keep"])
    number_of_dice_to_throw = 5 - len(result)
    for _ in range(number_of_dice_to_throw):
        result.append(str(random.randint(1, 6)))
    dice_dict["All"] = result
    print(f"\ndice are rolling......🎲\n")


def ask_action() -> str:
    """Ask player an action option.

    A function that asks player to choose one of the three options(from 1 to 3).
    If player enter input other than 1, 2 or 3, it shows an error message and
    keeps asking until user enters valid input.

    :precondition: N/A
    :postcondition: Correctly return user's input after validation check.
    :return: User's option choice from 1 to 3 in string.

    #Can not doctest this function because it will require user's input.
    """

    result = " "
    while result not in ["1", "2", "3"]:
        print(f"What do you want to do next?\n"
              f"Enter a number from 1 to 3 according to options below.\n"
              f"[1] : Write score sheet with your current dice.\n"
              f"[2] : Change dice to keep.\n"
              f"[3] : Throw dice.\n")
        result = input("Your choice : ")
        if result not in ["1", "2", "3"]:
            print("\nPlease enter your option from 1 to 3.\n")
    return result


def get_first_dice_throw() -> dict:
    """Get a result of first dice throw

    A function that generates dictionary of two dice lists.
    The value of the key 'All' is a list of five randomly generated die numbers in string.
    The value of the key 'Keep' is an empty list.

    :precondition: N/A
    :postcondition: Correctly generate a dictionary of the two dice lists.
    :return: A dictionary of two dice lists for first dice throw.

    #Can not doctest this function because it uses random method.
    """
    dice_dict = {'All': [str(random.randint(1, 6)) for _ in range(5)], 'Keep': []}  # Result of first roll
    print(f"\nYour first dice are thrown.....🎲")
    return dice_dict


def play_turn(score_sheet: dict) -> None:
    """Play a turn of yahtzee.

    A function that play a turn of yahtzee with player's score sheet.
    A set of randomly generated five dice is given to player in the beginning.
    Player has three following options.
    [1] write score sheet, [2] keep dice and [3] throw dice
    Player is asked to choose their action until they write score sheet.
    If player throws dice twice, they used all chances to throw dice and automatically write sheet with current dice.

    :param score_sheet: The score sheet of player playing the turn.
    :precondition: The format of the dictionary should be as following
                   {"name": str, "Ones": score, "Twos": score, "Threes": score, "Fours": score,
                   "Fives": score, "Sixes": score, "Three of a kind": score, "Four of a kind": score,
                   "Full House": score, "Small straight": score, "Large straight": score, "Chance": score,
                   "Yahtzee": score, "Yahtzee count": count}
                   The values named 'score' can be " " or number in string that player wrote for the combinations of
                   corresponding keys or None if the player did not mark anything yet.
    :postcondition: N/A
    :return: N/A

    #Can not unittest or doctest this function because it will be an integrated function which uses multiple functions.
    """

    print(f"\n{score_sheet['name']}, it's your turn.")
    print_score(score_sheet)
    dice = get_first_dice_throw()
    throw_chance = 2  # Number of possible throws left
    player_action = ""  # Initialize player_action for looping
    while player_action != "1":
        print(f"\nYour current dice are : {dice['All']} and you are keeping {dice['Keep']}.\n"
              f"You have {throw_chance} more chance(s) to throw dice.\n")
        if throw_chance == 0:
            print("You used all of your chances to throw dice. Mark the score sheet with current dice.")
            write_score(dice['All'], score_sheet)
            break
        player_action = ask_action()
        if player_action == "1":
            write_score(dice['All'], score_sheet)
        elif player_action == "2":
            change_dice_to_keep(dice)
        else:
            throw_dice(dice)
            throw_chance -= 1


def play_additional_turns(score_sheets: dict) -> None:
    """Play additional turn.

    A function that lets players have additional turns for as many yahtzees they got from previous turns.
    If the two players both have yahtzees, they play turns alternatively for the smaller yahtzee counts between the two.
    Then, the player with higher yahtzee counts plays alone for the difference between the two yahtzee counts.
    If only one player had yahtzee(s), then the player plays turn(s) oneself.

    :param score_sheets: Score sheets that contain results from previous turns.
    :precondition: score_sheets should contain only two elements of dictionary.
                   Each dictionary should contain result about player's previous 13 turns.
                   The format of the dictionary should be as following :
                   {"name": str, "Ones": score, "Twos": score, "Threes": score, "Fours": score,
                   "Fives": score, "Sixes": score, "Three of a kind": score, "Four of a kind": score,
                   "Full House": score, "Small straight": score, "Large straight": score, "Chance": score,
                   "Yahtzee": score, "Yahtzee count": count}
                   The values named 'score' and 'count' should be int.
    :postcondition: N/A
    :return: N/A

    #Can not unittest or doctest this function because it will be an integrated function which uses multiple functions.
    """
    player_one_left_turn = score_sheets[0]["Yahtzee count"]
    player_two_left_turn = score_sheets[1]["Yahtzee count"]
    # In case where player one has Yahtzee counts higher than or equal to player two
    if player_one_left_turn >= player_two_left_turn:
        # Play turns alternatively for less yahtzee counts between the two
        for _ in range(player_two_left_turn):
            for score_sheet in score_sheets:
                play_turn(score_sheet)
        # Player one plays turns by oneself for the rest of yahtzee counts one has
        for _ in range(player_one_left_turn - player_two_left_turn):
            play_turn(score_sheets[0])
    # In case where player two has yahtzee counts higher than player two
    else:
        # Play turns alternatively for less yahtzee counts between the two
        for _ in range(player_two_left_turn):
            for score_sheet in score_sheets:
                play_turn(score_sheet)
        # Player two plays turns by oneself for the rest of yahtzee counts one has
        for _ in range(player_two_left_turn - player_one_left_turn):
            play_turn(score_sheets[1])


def empty_score_sheets() -> list:
    """Return a list of two empty score sheets for yahtzee game."""

    return [{"name": "Player 1", "Ones": ' ', "Twos": ' ', "Threes": ' ', "Fours": ' ', "Fives": ' ',
             "Sixes": ' ', "Three of a kind": ' ', "Four of a kind": ' ', "Full House": ' ',
             "Small straight": ' ', "Large straight": ' ', "Chance": ' ', "Yahtzee": ' ', "Yahtzee count": 0},
            {"name": "Player 2", "Ones": ' ', "Twos": ' ', "Threes": ' ', "Fours": ' ', "Fives": ' ',
             "Sixes": ' ', "Three of a kind": ' ', "Four of a kind": ' ', "Full House": ' ',
             "Small straight": ' ', "Large straight": ' ', "Chance": ' ', "Yahtzee": 0,
             "Yahtzee count": 0}]


def yahtzee_play() -> None:
    """Play one yahtzee game.

    A function that runs play_turn alternatively with two players' score sheets.
    Play 13 fixed rounds. players with yahtzee play additional turns as many as their yahtzee count(s)

    :precondition: N/A
    :postcondition : N/A
    :return: N/A

    #Can not unittest or doctest this function because it will be an integrated function which uses multiple functions.
    """
    score_sheets = empty_score_sheets()

    for _ in range(13):  # Play fixed 13 alternative rounds
        for score_sheet in score_sheets:
            play_turn(score_sheet)
    play_additional_turns(score_sheets)  # Play additional turns for as many yahtzees as each player has

    print(f"🎲🎲🎲🎲🎲🎲Game Finished!🎲🎲🎲🎲🎲🎲")
    show_result(score_sheets)


def yahtzee() -> None:
    """Run yahtzee program.

    A function that keeps playing yahtzee games until player wants to quit.

    :precondition: N/A
    :postcondition : Runs the program correctly
    :return : N/A

    #Can not unittest or doctest this function because it will be an integrated function which uses multiple functions.
    """
    print(f"🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲Welcome to Yahtzee🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲\n"
          f"Player 1 will play first, then player 2 will play second!")
    play = True
    while play:
        yahtzee_play()
        replay = input("\nType \"Y\" or \"y\" to restart the game.\nHit enter to finish the program.").lower()
        if replay != "y":
            play = False
            print("\n🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲See you again🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲")
            print("\n🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲Let's Do It Again🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲")


def main():
    yahtzee()


if __name__ == '__main__':
    main()

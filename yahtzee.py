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
    total_scores = [0, 0]
    for index, score_sheet in enumerate(score_sheets):
        score_upper_section = score_sheet['Ones'] + score_sheet['Twos'] + score_sheet['Threes'] + \
                              score_sheet['Fours'] + score_sheet['Fives'] + score_sheet['Sixes']
        score_lower_section = score_sheet['Three of a kind'] + score_sheet['Four of a kind'] + \
                              score_sheet['Full House'] + score_sheet['Small straight'] + \
                              score_sheet['Large straight'] + score_sheet['Chance'] + score_sheet['Yahtzee']
        bonus = 35 if score_upper_section >= 63 else 0
        total_scores[index] = score_upper_section + score_lower_section + bonus
        print(f"\n🎲🎲🎲🎲🎲{score_sheet['name']}'s Result🎲🎲🎲🎲🎲\n"
              f"\t\tUpper Section : {score_upper_section}\n"
              f"\t\tBonus         : {bonus}\n"
              f"\t\tLower Section : {score_lower_section}\n"
              f"\t\tTotal Score   : {total_scores[index]}\n"
              f"🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲🎲\n")
    print(f"🎲🎲\t\t{score_sheets[0]['name']}: {total_scores[0]} vs "
          f"{score_sheets[1]['name']}: {total_scores[1]}\t\t🎲🎲")
    if total_scores[0] > total_scores[1]:
        print(f"🎲🎲{score_sheets[0]['name']}'s Win! Congratulations!🎲🎲\n")
    elif total_scores[0] < total_scores[1]:
        print(f"🎲🎲{score_sheets[1]['name']}'s Win! Congratulations!🎲🎲\n")
    else:
        print(f"🎲🎲Wow, it's a tie! You should play another game!🎲🎲\n")


def make_calculate_ns(number: int):
    """Make a fucntion that calculate "N"s in yahtzee game.

    A function that generates a points calculator of an upper section combination in yahtzee game.

    :param number: A number that use wants two create function with(e.g. if number == 1, it makes a calculator for Ones)
    :precondition: number shouold be a die number (i.e. 1 to 6)
    :postcondition: Correctly generate a function that calculates one of the functions in the upper section
    :return: A function that calculates one of the functions in the upper section

    >>> print(make_calculate_ns(1)(["5", "2", "3", "4", "6"]))
    0

    >>> print(make_calculate_ns(1)(["1", "2", "3", "4", "5"]))
    1

    >>> print(make_calculate_ns(1)(["1", "1", "1", "1", "1"]))
    5

    >>> print(make_calculate_ns(2)(["2", "2", "3", "5", "5"]))
    4

    >>> print(make_calculate_ns(2)([ "2", "2", "1", "2", "2"]))
    8

    >>> print(make_calculate_ns(3)(["1", "2", "5", "4", "6"]))
    0

    >>> print(make_calculate_ns(3)([ "3", "1", "2", "3", "3"]))
    9

    >>> print(make_calculate_ns(4)(["4", "2", "3", "4", "5"]))
    8

    >>> print(make_calculate_ns(5)(["1", "2", "3", "4", "2"]))
    0

    >>> print(make_calculate_ns(5)(["5", "5", "5", "4", "5"]))
    20

    >>> print(make_calculate_ns(6)(["6", "1", "6", "6", "6"]))
    24

    >>> print(make_calculate_ns(6)(["6", "6", "6", "6", "6"]))
    30
    """

    def calculate_ns(dice_list: list) -> int:
        """Calculate points of ns of given dice list.

        :param dice_list: A list of dice to calculate.
        :precondition: dice_list should be a list that contains five elements, each of which is a die number in string.
        :postcondition: Correctly calculate the point player can get in one of upper section combination with dice_list.
        :return: Calculated points
        """
        count = 0
        for die in dice_list:
            if die == str(number):
                count += 1
        return count * number

    return calculate_ns


def dice_sum(dice_list: list) -> int:
    """Calculate the sum of dice.

    A function that calculates the sum of a dice set in a list format.

    :param dice_list: A list of dice to calculate sum of.
    :precondition: dice_list should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate sum of elements of dice_set.
    :return: sum of elements of dice_set

    >>> print(dice_sum(["1", "2", "3", "4", "5"]))
    15

    >>> print(dice_sum(["1", "1", "1", "1", "1"]))
    5

    >>> print(dice_sum(["1", "3", "3", "4", "4"]))
    15

    """
    result = 0
    for die in dice_list:
        result += int(die)
    return result


def make_calculate_n_kind(number):
    """Make a fucntion that calculates points of N of a kind.

    A function that generates a points calculator of Three of a kind or Four of a kind in yahtzee game.

    :param number: A number that use wants two create function with.
    :precondition: number shouold be 3 or 4.
    :postcondition: Correctly generate a function that calculates points of either Three or Four of a kind.
    :return: A function that calculates points of either Three or Four of a kind

    >>> print(make_calculate_n_kind(3)(["2", "2", "2", "1", "6"]))
    13

    >>> print(make_calculate_n_kind(3)(["4", "4", "1", "4", "6"]))
    19

    >>> print(make_calculate_n_kind(3)(["2", "2", "2", "2", "6"]))
    14

    >>> print(make_calculate_n_kind(3)(["3", "3", "3", "3", "3"]))
    15

    >>> print(make_calculate_n_kind(3)(["1", "2", "3", "4", "5"]))
    0

    >>> print(make_calculate_n_kind(4)(["2", "2", "2", "2", "6"]))
    14

    >>> print(make_calculate_n_kind(4)(["2", "2", "2", "2", "1"]))
    9

    >>> print(make_calculate_n_kind(4)(["5", "5", "5", "5", "1"]))
    21

    >>> print(make_calculate_n_kind(4)(["5", "5", "1", "5", "5"])) # non-contiguous case
    21

    >>> print(make_calculate_n_kind(4)(["5", "5", "5", "5", "5"]))
    25
    """

    def calculate_n_of_a_kind(dice_list):
        """Calculate points of ns of given dice list.

        :param dice_list: A list of dice to calculate points with.
        :precondition: dice_list should be a list that contains five elements, each of which is a die number in string.
        :postcondition: Correctly calculate the point player can get in either Three of Four of a kind.
        :return: Calculated points

        """
        for die in dice_list:
            if dice_list.count(die) > number - 1:
                return dice_sum(dice_list)
            return 0

    return calculate_n_of_a_kind


def calculate_small_straight(dice_lit: list) -> int:
    """Calculate points of Small straight.

    A function that calculates the points of Small straight when written with dice_set.

    :param dice_lit: A list of dice that user wants to use to write Small straight.
    :precondition: dice_list should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Small straight when written with dice_list.
    :return: Calculated points of Small straight when written with dice_list.

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
    count = 0
    previous_die = -1
    for die in sorted(dice_lit):
        die_int = int(die)
        if die_int == previous_die + 1:
            count += 1
        elif die_int != previous_die:
            count = 0
        previous_die = die_int
    if count >= 3:
        return 30
    return 0


def calculate_large_straight(dice_list: list) -> int:
    """Calculate points of Large straight.

    A function that calculates the points of Large straight when written with dice_list.

    :param dice_list: A list of dice that user wants to use to write Large straight.
    :precondition: dice_list should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Large straight when written with dice_list.
    :return: Calculated points of Large straight when written with dice_list.

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
    count = 0
    previous_die = -1
    for die in sorted(dice_list):
        die_int = int(die)
        if die_int == previous_die + 1:
            count += 1
        elif die_int != previous_die:
            count = 0
        previous_die = die_int
    if count == 4:
        return 40
    return 0


def calculate_full_house(dice_list):
    """Calculate points of Full House.

    A function that calculates the points of Full House when written with dice_list.

    :param dice_list: A list of dice that user wants to use to write Full House.
    :precondition: dice_list should be a list that contains five elements, each of which is a die number in string.
    :postcondition: Correctly calculate points of Full House when written with dice_list.
    :return: Calculated points of Full House when written with dice_list.

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
    # return zero if there are not two kinds of dice in the dice_set
    if len(set(dice_list)) != 2:
        return 0
    # for dice_set with only two kinds of elements, return 25 if dice_set has two elements of one of the two kinds
    for die in set(dice_list):
        if dice_list.count(die) == 2:
            return 25
    return 0


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

    >>> print_score(sample_score_sheet())# doctest: +NORMALIZE_WHITESPACE
    <player_name's Score Sheet>
    [1]Ones: 1	[2]Twos: 4	[3]Threes: 9	[4]Fours: 12	[5]Fives: 20	[6]Sixes: 18
    [7]Three of a kind: 16	[8]Four of a kind: 23	[9]Full House: 25	[10]Small straight: 30
    [11]Large straight: 40	[12]Chance: 21	[13]Yahtzee: 0	**Yahtzee count: 0

    >>> print_score(sample_score_sheet_two())# doctest: +NORMALIZE_WHITESPACE
    <player_name's Score Sheet>
    [1]Ones: 1	[2]Twos: 4	[3]Threes: 9	[4]Fours: 12	[5]Fives: 10	[6]Sixes: 6
    [7]Three of a kind: 10	[8]Four of a kind: 23	[9]Full House: 25	[10]Small straight: 30
    [11]Large straight: 40	[12]Chance: 13	[13]Yahtzee: 50	**Yahtzee count: 0
    """
    print(f"<{score_sheet['name']}'s Score Sheet>\n"
          f"[1]Ones: {score_sheet['Ones']}\t[2]Twos: {score_sheet['Twos']}\t[3]Threes: {score_sheet['Threes']}\t"
          f"[4]Fours: {score_sheet['Fours']}\t[5]Fives: {score_sheet['Fives']}\t[6]Sixes: {score_sheet['Sixes']}\n"
          f"[7]Three of a kind: {score_sheet['Three of a kind']}\t[8]Four of a kind: {score_sheet['Four of a kind']}\t"
          f"[9]Full House: {score_sheet['Full House']}\t[10]Small straight: {score_sheet['Small straight']}\n"
          f"[11]Large straight: {score_sheet['Large straight']}\t[12]Chance: {score_sheet['Chance']}\t"
          f"[13]Yahtzee: {score_sheet['Yahtzee']}\t**Yahtzee count: {score_sheet['Yahtzee count']}")


def number_combo_converter(number: str) -> str:
    number_combo_match = {"1": "Ones", "2": "Twos", "3": "Threes", "4": "Fours", "5": "Fives", "6": "Sixes",
                          "7": "Three of a kind", "8": "Four of a kind", "9": "Full House", "10": "Small straight",
                          "11": "Large straight", "12": "Chance", "13": "Yahtzee"}
    return number_combo_match[number]


def ask_combo_to_write(dice_list: list, score_sheet: dict) -> str:
    """Ask which combination to write on the score sheet.

    A function that ask user which combination to write and return the user answer.
    It validates player's answer on whether they can write on selected combination or not.
    It keeps asking until the player answers a valid answer.

    :param dice_list: A list of dice to calculate points of a combination with.
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

    while True:
        user_answer = input("Number of combination to write : ").rstrip()
        # Filter an invalid answer (i.e. not a number from 1 to 13)
        if user_answer not in [str(number) for number in range(1, 14)]:
            print("Invalid input. Please choose combination number from 1 to 13")
            continue
        chosen_combo = number_combo_converter(user_answer)
        # When player chose to write yahtzee
        if chosen_combo == "Yahtzee":
            if score_sheet[chosen_combo] == " " or score_sheet[chosen_combo] != 0 & len(set(dice_list)) == 1:
                break
            elif score_sheet[chosen_combo] == 0:
                print("You can't write Yahtzee anymore after writing it as 0. Choose other combination")
                continue
            else:
                print(f"{dice_list} is not Yahtzee and Yahtzee is already written. Choose other combination.")
                continue
        # When chosen combo is already written on the score sheet
        if score_sheet[chosen_combo] != " ":
            print(f"You already wrote {chosen_combo}. Choose another combination.")
            continue
        break
    return chosen_combo


def write_yahtzee(dice_list: list, score_sheet: dict) -> None:
    """Write yahtzee on score sheet.

    A function that writes yahtzee on a score sheet based on player's dice combination.
    It updates the value of "Yahtzee" and "Yahtzee count" according to user's dice list.

    :param dice_list: A numbers of player's current dice to write yahtzee with.
    :param score_sheet: The score sheet that player wants to write on . It contains player's score information.
    :precondition : dice_list should contains five elements, each of which is a die number in string.
                    score_sheet should have a key "Yahtzee" and the value of which can not be 0.
                    score_sheet should have a key "Yahtzee count" and the value of which should be integer.
    :return: N/A

    """
    if len(set(dice_list)) == 1:
        if score_sheet["Yahtzee count"] == " ":
            score_sheet["Yahtzee"] = 50
        else:
            score_sheet["Yahtzee"] += 100
        score_sheet["Yahtzee count"] += 1
    else:
        score_sheet["Yahtzee"] = 0


def write_score(dice_list: list, score_sheet: dict) -> None:
    """Write score sheet of Yahtzee.

    A function that writes score on Yahtzee score sheet according to calculation of points based on dice_set and
    user's input. One cannot overwrite score sheet unless it's multiple yahtzee case.

    :param dice_list: A list of dice to calculate points of a combination with.
    :param score_sheet: The score sheet that player wants to write on . It contains player's score information.
    :precondition: dice_list should contains five elements, each of which is a die number in string.
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
    print_score(score_sheet)
    print(f"Your dice are\n{dice_list}")
    print(f"Entre the number of combination to mark from the score sheet.\ne.g) Enter '1' to mark Ones\n")

    # Make 12 key-value pairs of combinations and the corresponding calculators  (except for Yahtzee)
    combo_points_calculators = {"Ones": make_calculate_ns(1), "Twos": make_calculate_ns(2),
                                'Threes': make_calculate_ns(3), "Fours": make_calculate_ns(4),
                                "Fives": make_calculate_ns(5), "Sixes": make_calculate_ns(6),
                                "Three of a kind": make_calculate_n_kind(3),
                                "Four of a kind": make_calculate_n_kind(4), "Full House": calculate_full_house,
                                "Small straight": calculate_small_straight, "Large straight": calculate_large_straight,
                                "Chance": dice_sum}
    # Ask user which combo to write
    combo_to_write = ask_combo_to_write(dice_list, score_sheet)

    if combo_to_write != "Yahtzee":
        # Call a calculator function corresponding to the combo user chose
        points = combo_points_calculators[combo_to_write](dice_list)
        score_sheet[combo_to_write] = points
        print(f"\n{score_sheet['name']}, you wrote {points} on {combo_to_write}.\n\n🎲Score Sheet Updated🎲")
        print_score(score_sheet)
    else:
        # Separate yahtzee case due to the inconsistency in writing score from other combos
        write_yahtzee(dice_list, score_sheet)


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
    :return: The difference list of the two input lists.

    >>> print(get_difference_list(['1','2','3','4','5'], ['1','2','3']))
    ['4', '5']

    >>> print(get_difference_list(['1','2','3','4','5'], ['1','2','3','4','5']))
    []

    >>> print(get_difference_list(['1','2','3','4','5'], []))
    ['1', '2', '3', '4', '5']

    >>> print(get_difference_list(['1','1','1','3','3'], ['1','3']))
    ['1', '1', '3']

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

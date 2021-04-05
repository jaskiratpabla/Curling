##
##=======================================================
## Jaskirat Pabla
## Curling Score
##=======================================================
##


import check


## Data Definition:

## A Rock is a Str
## Requires:
##  - Rock must be either 5 or 6 characters in length.
##  - The first 3 characters are digits representing the distance 
##    to the button for a rock. Leading zeros are included if 
##    necessary so this distance will be between 000 and 
##    999 (inclusive).
##  - The fourth character is "Y" or "R" indicating the colour of 
##    the rock (representing yellow and red respectively).
##  - The fifth and/or sixth character(s) represent the number of 
##    the end, which is a positive integer between 1 and
##    99 (inclusive).


## Constants for Testing:
sample_rock_positions = ["043Y3","045Y2","108R3","075Y4","596R1",\
                         "198R2","422R4","041Y1","400Y3","415R2",
                         "606R2","209R1","402Y3","389Y1","376R2",\
                         "042Y4","380R2","076Y4","071Y3"]
large_rock_positions = ["043Y3","045Y32","108R23","075Y54","596R81",\
                        "198R2","422R4","041Y1","400Y73","415R92",
                        "606R12","209R41","402Y3","389Y61","376R92",\
                        "042Y54","380R92","076Y54","071Y99"]
yellow_only = ["000Y98", "101Y1", "115Y3", "116Y8", "012Y10", "222Y6"]
red_only = ["999R99", "101R1", "115R3", "116R8", "012R10", "222R6"]


def end_score(col, lst_of_rocks, end_number):
    '''
    Returns the score of team col for end end_number from
    lst_of_rocks of rocks for that end_number.
    
    end_score: (anyof "Y" "R") (listof Rock) Nat -> Nat
    Requires: 1 <= end_number <= 99
    '''
    L = (list(filter(lambda posn: posn[4:] == str(end_number),
                     lst_of_rocks)))
    Y = (list(filter(lambda posn: posn[3] == "Y", L)))
    R = (list(filter(lambda posn: posn[3] == "R", L)))
    if (Y == []):
        if (col == "Y"):
            return 0
        else:
            return len(R)
    elif (R == []):
        if (col == "R"):
            return 0
        else:
            return len(Y)
    else:
        A = (list(map(lambda posn: int(posn[:3]), R)))
        B = (list(map(lambda posn: int(posn[:3]), Y)))
        if (col == "Y"):
            min_opp_team = min(A)
            W = (list(filter(lambda num: num < min_opp_team, B)))
            round_score = len(W)
        else:
            min_opp_team = min(B)
            W = (list(filter(lambda num: num < min_opp_team, A)))
            round_score = len(W)
        return round_score


def score(colour, rock_positions):
    '''
    Returns the score of team colour based on rock_positions.
    
    score: (anyof "Y" "R") (listof Rock) -> Nat
    
    Examples:
        score("Y", []) => 0
        score("R", []) => 0
        score("Y", sample_rock_positions) => 7
    '''
    if (rock_positions == []):
        total_score = 0
    else:
        max_end_number = max(list(map(lambda posn: int(posn[4:]),
                               rock_positions)))
        end_lst = range(max_end_number + 1)
        E = (list(map(lambda end: end_score(colour, rock_positions, end),
                      end_lst)))
        total_score = sum(E)
    return total_score


## Examples:
check.expect("Testing empty list, colour yellow", score("Y", []), 0)
check.expect("Testing empty list, colour red", score("R", []), 0)
check.expect("Testing random", score("Y", sample_rock_positions), 7)


## Tests:
check.expect("Testing team that never earns points in any end",
             score("R", sample_rock_positions), 0)
check.expect("Winning team only places rocks in the house (Red)",
             score("R", red_only), 6)
check.expect("Winning team only places rocks in the house (Yellow)",
             score("Y", yellow_only), 6)
check.expect("Losing team never places rocks in the house (Yellow)",
             score("Y", red_only), 0)
check.expect("Losing team never places rocks in the house (Red)",
             score("R", yellow_only), 0)
check.expect("Testing list that contains lots of ends",
             score("R", large_rock_positions), 9)
check.expect("Testing list that contains lots of ends for opposite team",
             score("Y", large_rock_positions), 10)

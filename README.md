# Curling
Curling score function in Python, full documentation and testing is included.
Curling is played by two teams throwing rocks towards circles at the end of a sheet of ice. The circles are called the house. The centre of the house is called the button.

The game is split into ends. In each end, a yellow team throws eight yellow rocks and a red team throws eight red rocks. If no rocks end up in the house, then no team scores points for that end. Otherwise, only the team with a rock finishing closest to the button scores points for that end. The number of points they score is the number of their rocks in the house that finish in a position closer to the button than every other rock of the other colour. For simplicity, we will assume that there are no ties in an end. That is, no two rocks will be the same distance to the button. Here are five examples where some of the rocks not in the house are not pictured:

![image](https://user-images.githubusercontent.com/67871488/113640247-f8263f80-9648-11eb-8e32-d7ee84b43235.png)
Credit: http://www.sportmember.pl/en/sports-rules/curling-rules 

Points earned in each end are totalled to give a team’s final score. Chips embedded in each rock report the distance to the button for the final position of each rock that finishes in the house. Chips do not report anything for rocks that are not in the house. Specifically, the chips give a list of strings where each string consists of exactly the following (in order):
- Three digits representing the distance to the button for a rock. Leading zeros are included if necessary so this distance will be between 000 and 999 (inclusive).
- "Y" or "R" indicating the colour of the rock (representing yellow and red respectively).
- The number of the end which is a positive integer between 1 and 99 (inclusive).

For example, the following list could represent the positions of all the rocks in the house in the five ends shown in the example above:

sample_rock_positions = ["041Y1","209R1","389Y1","596R1",\
                         "045Y2","198R2","376R2","380R2","415R2","606R2",\
                         "043Y3","071Y3","108R3","400Y3","402Y3",\
                         "042Y4","075Y4","076Y4","422R4"]

Unfortunately, this chip technology is very new and there are no guarantees about the order of the strings in a list of rock positions. The list might not be nicely ordered as in the example above.

The function score(colour, rock_positions) returns the score of the team throwing colour ("Y" or "R") based on rock_positions given by the chip technology as specified above. Additional challenge: No recursion and/or loops are allowed, we may only solve this question through the usage of abstract list functions!

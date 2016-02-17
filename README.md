# MapRMadness
Simulate a bracket based on user-supplied inputs
Note: currently uses 2015 bracket for testing.

### User-supplied inputs currently supported:
- Importance of tournament seeding (e.g. 1 vs. 16) - 0-100%


### Future inputs supported:
- Cinderella team: automatic bid to final four
- Importance of 3-point accuracy
- Importance of Free-throw accuracy
- Importance of Defense
- Weight on recent record (i.e. hot teams)

### Program call:
./bracket.py <seed_weight> <br>
- Produces a winner of each game in the tournament; seed weight is optional <br>
- The results will be different for each run based on randomness
- Game = "g+round+game" (e.g. g3_7 = 7th game of round #3) <br>
- Round 0 = play-in round (4 games) <br>
- Round 1 = Round of 64 (32 games) <br>
- Round 6 = Championship (1 game) <br>

### Example for 2015 bracket: (ignore team_id for now)
./bracket.py 0.8 <br>
g0_1 :  72 Dayton<br>
g0_2 :  113 Hampton<br>
g0_3 :  31 Brigham Young<br>
g0_4 :  255 Robert Morris<br>
g1_1 :  144 Kentucky<br>
g1_2 :  56 Cincinnati<br>
g1_3 :  337 West Virginia<br>
g1_4 :  169 Maryland<br>
g1_5 :  314 Texas<br>
g1_6 :  227 Notre Dame<br>
g1_7 :  130 Indiana<br>
g1_8 :  141 Kansas<br>
g1_9 :  345 Wisconsin<br>
g1_10 :  236 Oregon<br>
g1_11 :  17 Arkansas<br>
g1_12 :  115 Harvard<br>
g1_13 :  31 Brigham Young<br>
g1_14 :  22 Baylor<br>
g1_15 :  229 Ohio State<br>
g1_16 :  13 Arizona<br>
g1_17 :  327 Villanova<br>
g1_18 :  212 North Carolina State<br>
g1_19 :  348 Wyoming<br>
g1_20 :  158 Louisville<br>
g1_21 :  72 Dayton<br>
g1_22 :  232 Oklahoma<br>
g1_23 :  177 Michigan State<br>
g1_24 :  331 Virginia<br>
g1_25 :  80 Duke<br>
g1_26 :  266 San Diego State<br>
g1_27 :  323 Utah<br>
g1_28 :  104 Georgetown<br>
g1_29 :  287 Southern Methodist<br>
g1_30 :  132 Iowa State<br>
g1_31 :  71 Davidson<br>
g1_32 :  109 Gonzaga<br>
g2_1 :  56 Cincinnati<br>
g2_2 :  337 West Virginia<br>
g2_3 :  314 Texas<br>
g2_4 :  130 Indiana<br>
g2_5 :  345 Wisconsin<br>
g2_6 :  115 Harvard<br>
g2_7 :  22 Baylor<br>
g2_8 :  13 Arizona<br>
g2_9 :  212 North Carolina State<br>
g2_10 :  158 Louisville<br>
g2_11 :  232 Oklahoma<br>
g2_12 :  331 Virginia<br>
g2_13 :  80 Duke<br>
g2_14 :  323 Utah<br>
g2_15 :  132 Iowa State<br>
g2_16 :  109 Gonzaga<br>
g3_1 :  337 West Virginia<br>
g3_2 :  314 Texas<br>
g3_3 :  345 Wisconsin<br>
g3_4 :  13 Arizona<br>
g3_5 :  212 North Carolina State<br>
g3_6 :  331 Virginia<br>
g3_7 :  80 Duke<br>
g3_8 :  132 Iowa State<br>
g4_1 :  314 Texas<br>
g4_2 :  13 Arizona<br>
g4_3 :  331 Virginia<br>
g4_4 :  80 Duke<br>
g5_1 :  13 Arizona<br>
g5_2 :  331 Virginia<br>
g6_1 :  13 Arizona<br>

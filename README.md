# MapRMadness
Simulate a bracket based on user-supplied inputs
Note: currently uses 2015 bracket for testing.

### User-supplied inputs expected:
- Importance of tournament seeding (e.g. 1 vs. 16) - 0-100%
- Importance of performance against common opponents - 0-100%
- Importance of 3-point accuracy - 0-100%
- Importance of Free-throw accuracy - 0-100%
- Importance of Defense - 0-100%
- Cinderella team: automatic bid to final four - an ID for a team in the tournament

### Program call:
./bracket.py seed\_weight rank\_weight 3pt\_weight ft\_weight def\_weight cinderella\_teamID
- Produces a winner of each game in the tournament; seed weight is optional <br>
- The results will be different for each run based on randomness
- Game = "g+round+game" (e.g. g3_7 = 7th game of round #3) <br>
- Round 0 = play-in round (4 games) <br>
- Round 1 = Round of 64 (32 games) <br>
- Round 6 = Championship (1 game) <br>

### Example for 2015 bracket: (ignore team_id for now)
./bracket.py 0.85 0.5 0.4 0.4 0.1 327 <br>
g0_1 :  72 Dayton<br>
g0_2 :  163 Manhattan<br>
g0_3 :  184 Mississippi<br>
g0_4 :  255 Robert Morris<br>
g1_1 :  144 Kentucky<br>
g1_2 :  56 Cincinnati<br>
g1_3 :  337 West Virginia<br>
g1_4 :  169 Maryland<br>
g1_5 :  36 Butler<br>
g1_6 :  227 Notre Dame<br>
g1_7 :  342 Wichita State<br>
g1_8 :  141 Kansas<br>
g1_9 :  345 Wisconsin<br>
g1_10 :  236 Oregon<br>
g1_11 :  346 Wofford<br>
g1_12 :  214 North Carolina<br>
g1_13 :  349 Xavier<br>
g1_14 :  22 Baylor<br>
g1_15 :  229 Ohio State<br>
g1_16 :  13 Arizona<br>
g1_17 :  327 Villanova<br>
g1_18 :  212 North Carolina State<br>
g1_19 :  223 Northern Iowa<br>
g1_20 :  158 Louisville<br>
g1_21 :  247 Providence<br>
g1_22 :  232 Oklahoma<br>
g1_23 :  108 Georgia<br>
g1_24 :  331 Virginia<br>
g1_25 :  80 Duke<br>
g1_26 :  293 St. John's (NY)<br>
g1_27 :  323 Utah<br>
g1_28 :  104 Georgetown<br>
g1_29 :  287 Southern Methodist<br>
g1_30 :  132 Iowa State<br>
g1_31 :  71 Davidson<br>
g1_32 :  109 Gonzaga<br>
g2_1 :  144 Kentucky<br>
g2_2 :  169 Maryland<br>
g2_3 :  227 Notre Dame<br>
g2_4 :  141 Kansas<br>
g2_5 :  236 Oregon<br>
g2_6 :  214 North Carolina<br>
g2_7 :  349 Xavier<br>
g2_8 :  13 Arizona<br>
g2_9 :  327 Villanova<br>
g2_10 :  158 Louisville<br>
g2_11 :  232 Oklahoma<br>
g2_12 :  108 Georgia<br>
g2_13 :  80 Duke<br>
g2_14 :  104 Georgetown<br>
g2_15 :  132 Iowa State<br>
g2_16 :  109 Gonzaga<br>
g3_1 :  144 Kentucky<br>
g3_2 :  227 Notre Dame<br>
g3_3 :  214 North Carolina<br>
g3_4 :  349 Xavier<br>
g3_5 :  327 Villanova<br>
g3_6 :  232 Oklahoma<br>
g3_7 :  104 Georgetown<br>
g3_8 :  132 Iowa State<br>
g4_1 :  144 Kentucky<br>
g4_2 :  214 North Carolina<br>
g4_3 :  327 Villanova<br>
g4_4 :  132 Iowa State<br>
g5_1 :  144 Kentucky<br>
g5_2 :  327 Villanova<br>
g6_1 :  327 Villanova<br>



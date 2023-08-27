# Characters Battle
A battle of legends

# Battle Simulator

A simple battle simulator that simulates a battle between two players.

## How to use

1. Clone or download this repository.
2. Open a terminal window in the repository's directory.
3. Run the following command to install the required dependencies:

pip install -r requirements.txt


4. Run the following command to start the simulator:

python battle.py

How it works
The simulator works by first generating two characters, each with a name, character type, health, and strength. The characters then battle each other, taking turns rolling dice. The character with the higher dice roll wins the round.

The difference in strength between the two characters is used to determine how much health the loser of the round loses. For example, if the winner has a strength of 10 and the loser has a strength of 5, then the loser will lose 5 points of health.

The battle continues until one of the characters' health reaches 0. The winner of the battle is the character with the remaining health.

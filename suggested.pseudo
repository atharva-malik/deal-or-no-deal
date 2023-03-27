function deal_or_no_deal:

# Initialise briefcases with random values between $1 and $1,000,000

set briefcases to a list of 26 random values between 1 and 1000000

set remaining_briefcases to a list of integers from 0 to 25

# Display instructions

display game instructions

# Choose player's briefcase

prompt player to choose a briefcase

remove chosen briefcase from remaining_briefcases

# Begin game loop

while there are more than 1 remaining briefcases:

# Eliminate briefcases

set num_to_eliminate to the minimum of 5 or number of remaining briefcases

for each briefcase to eliminate:

prompt player to choose a briefcase to eliminate

remove chosen briefcase from remaining_briefcases

display the value of the eliminated briefcase

# Calculate offer from Banker

set remaining_values to the values of the remaining briefcases

set offer to the average of remaining_values

display offer

# Accept or reject offer

prompt player to choose "deal" or "no deal"

if player chooses "deal":

display winning message with offer

return

# Reveal value of player's briefcase

display message that player has chosen to keep their briefcase

display the value of the player's briefcase
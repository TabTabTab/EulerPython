#Euler173

# an outline is represented only using its cost
# as outlines has to fit inside each other, 
# outlines with an even amount of side tiles can only 
# coexist with other outlines which are also based on
# an even amount of side tiles


def get_possible_outlines(nbr_of_tiles):
	return list(xrange(8,nbr_of_tiles+1,4))

def get_nbr_of_combos_using(possible_tiles,nbr_of_tiles):
	nbr_of_combos=0
	for startIndex in xrange(0,len(possible_tiles)):
		for endIndex in xrange(startIndex+1,len(possible_tiles)+1):
			if sum(possible_tiles[startIndex:endIndex])<=nbr_of_tiles:
				nbr_of_combos=nbr_of_combos+1;
			else:
				break
	return nbr_of_combos

def get_nbr_of_tile_combos(nbr_of_tiles):	
	possible_tiles=get_possible_outlines(nbr_of_tiles)
	nbr_of_combos=0
	nbr_of_combos=nbr_of_combos+get_nbr_of_combos_using(possible_tiles[0::2],nbr_of_tiles)
	nbr_of_combos=nbr_of_combos+get_nbr_of_combos_using(possible_tiles[1::2],nbr_of_tiles)
	return nbr_of_combos


nbr_of_tiles=10**6

print get_nbr_of_tile_combos(nbr_of_tiles)
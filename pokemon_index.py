# Pokemon lists
pokemon_names   = ['charmander', 'squirtle', 'bulbasaur', 'gyrados']
pokemon_amounts = [3,             2,          5,           1]
pokemon_prices  = [100.00,        50.00,      25.00,       1000.00]
pokemon_types   = [['fire'],      ['water'],  ['grass'],   ['water', 'flying']]
type_of_pokemon = ['bug', 'dark', 'dragon', 'electric', 'fairy', 'fighting', 'fire', 'flying', 'ghost', 'grass', 'ground', 'ice', 'normal', 'poison', 'psychic', 'rock', 'steel', 'water']
while True:
    print("Welcome to the pokemon center!")
    optionInput = input("(a)dd, (r)emove, r(e)port, (s)earch by name, search by (t)ype, (l)ist or (q)uit:")
    option = str.lower(optionInput)

#if user wants to quit
    if option == "q":
        print("Goodbye!")
        break

#if user wants to select pokemon
    elif option == "s":
        pokemonInput = input("Type the name of a pokemon: ")
        pokemon = str.lower(pokemonInput)
        if pokemon in pokemon_names:

            # figure out what index the pokemon lives at
            location = pokemon_names.index(pokemon)

            # use this info to cross ref into the second list
            amount = pokemon_amounts[location]

            # use this to get the fee
            price = pokemon_prices[location]

            #grab the typing based on the location
            typing = ()
            typingExtract = pokemon_types[location]
            for typing in typingExtract:

                print("We have", str(amount), "of", pokemon.capitalize(), "at the center")
                print("It will cost $" + str(price), "to adopt this Pokemon")
                print(pokemon, "has the following types:", typing.capitalize())


        else:
            print("We do not have any", pokemon, "at the center")

    elif option == "t":

#pokemon_types   = [['fire'],      ['water'],  ['grass'],   ['water', 'flying']]
        
        typeInput = input("Enter pokemon type: ")

        print(format('Name', '<20s'), format('Amount Available', '<20s'), 'Adoption Fee', "Type(s)")
        sum=0
        #for the output based on type 
        for i in range (len(pokemon_types)):
            if typeInput in pokemon_types[i]:
                print(format(pokemon_names[i].capitalize(), '<20s'), format('3', '>16s'), format(str(pokemon_prices[i]), '>16s'), (pokemon_types[i]))
                sum+=1
        if sum == 0:
            print("We have no Pokemon of that type at our Pokemon Center")
        #if user wants a list of pokemon 


    elif option == "l":

        print(format('Name', '<20s'), format('Amount Available', '<20s'), 'Adoption Fee', "Type(s)")
        for i in range(len(pokemon_names)):
            print("{0}".format(pokemon_names[i].capitalize(), '<20s'), "{0}".format(pokemon_amounts[i], '>16s'), "{0:.2f}".format(pokemon_prices[i], '>16s'), (pokemon_types[i]))
            


#Part 2e
    elif option == "a":
        new_pokemon = input("Enter name of new pokemon: ")
        pokemon_names.append(new_pokemon)
        amount_pokemon = -1
        while amount_pokemon < 0 :
            amount_pokemon = int(input("How many of these Pokemon are you adding?"))
            if amount_pokemon < 0 or type(amount_pokemon) != int: 
                print("Invalid, please try again")
            else :
                pokemon_amounts.append(amount_pokemon)
        fee_pokemon = -1
        while fee_pokemon < 0 :
            fee_pokemon = float(input("What is the adoption fee for this Pokemon?"))
            if fee_pokemon < 0 :
                print("Invalid, please try again")
            else :
                pokemon_prices.append(fee_pokemon)
        
        print("Next you will be prompted to enter the 'types' for this Pokemon.  Pokemon can have multiple types. Type 'help' to view all possible Pokemon types, and type 'end' to stop entering types. You must enter at least one valid 'type'")
        
        type_pokemon = None
        type_list = []
        while type_pokemon != "end":
            type_pokemon = input("What type of Pokemon is this?")
            if type_pokemon == "help":
                print("*bug\n*dark\n* dragon\n* electric\n* fairy\n* fighting\n* fire\n* flying\n* ghost\n* grass\n* ground\n* ice\n* normal\n* poison\n* psychic\n* rock\n* steel\n* water")
            elif type_pokemon =="end":
                print("Pokemon Added!")
                pokemon_types.append(type_list)
            elif type_pokemon not in type_of_pokemon:
                print("This is not a valid type, please try again")
            else:
                print(f"type {type_pokemon} added")
                type_list.append(type_pokemon)


#part 2f
    elif option == "r":
        remove_pokemon = input("Enter name of Pokemon to remove: ")
        #remove_pokemon.lower()
        if remove_pokemon.lower() not in pokemon_names:
            print("Pokemon not found, cannot remove")
        else:
            index = 0
            for i in range (0,len(pokemon_names)):
                if pokemon_names[i] == remove_pokemon:
                    index = i
            pokemon_names.remove(pokemon_names[index])
            pokemon_amounts.remove(pokemon_amounts[index])
            pokemon_prices.remove(pokemon_prices[index])
            pokemon_types.remove(pokemon_types[index])
            print("Pokemon removed") 



#part 2g
    elif option == "e":
        max = 0
        max_pokemon_name = None
        min = 100000000
        min_pokemon_name = None
        total = 0
        for i in range(0, len(pokemon_names)):
            if pokemon_prices[i] >= max:
                max = pokemon_prices[i]
                max_pokemon_name = pokemon_names[i]
            if pokemon_prices[i] <= min:
                min = pokemon_prices[i]
                min_pokemon_name = pokemon_names[i]
            total += pokemon_prices[i] * pokemon_amounts[i]

        print('Highest priced Pokemon:', max_pokemon_name, '@ {0:.2f} per Pokemon'.format(max))
        print('Lowest priced Pokemon: {0} @ ${1:.2f} per Pokemon'.format(min_pokemon_name, min))
        print('Total cost to adopt all Pokemon in the Center: ${0:.2f}'.format(total))

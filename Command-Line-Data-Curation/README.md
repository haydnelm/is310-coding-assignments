For my assignment, I decided to store pokemon data in a rich table.

The table has three columns: Name, Type, and Shiny.
Name is simply the pokemon's name, type is the pokemon's type, and shiny is whether or not the pokemon is shiny t/f.

Upon running the script you will see an example table including charmander, bulbasaur, and squirtle. These entries will not be included in the users own table. 

The simple workflow would include entering the pokemons name, type, and true or false for shiny. The actual types will be verified with real pokemon types. So you cannot say something like "airplane" for a pokemon type. The offical types include: normal, fire, fighting, water, flying, grass, poison, electric, ground, psychic, rock, ice, bug, dragon, ghost, dark, steel, and fairy.

The rows will have a color style applied to them with the following convention:

        "normal": "light_yellow3",
        "fire": "red",
        "fighting": "dark_red",
        "water": "blue",
        "flying": "sky_blue3",
        "grass": "green",
        "poison": "magenta",
        "electric": "bright_yellow",
        "ground": "dark_goldenrod",
        "psychic": "deep_pink1",
        "rock": "gold3",
        "ice": "pale_turquoise1",
        "bug": "green_yellow",
        "dragon": "magenta3",
        "ghost": "medium_purple2",
        "dark": "grey27",
        "steel": "grey70",
        "fairy": "plum1"

This is to replicate the color typing from the actual pokemon game.

At any point after adding an entry the user can choose to reset the table by saying 'incorrect', conversely, they can choose to write the table to a .txt file by saying 'confirm'

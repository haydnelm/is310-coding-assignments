from rich.console import Console
from rich.table import Table

console = Console()

console.print("Here is an example of some Pokemon:", style="bold red")

table = Table(title="Pokemon")
table.add_column("Name", no_wrap=True)
table.add_column("Type(s)", no_wrap=True)
table.add_column("Shiny?", no_wrap=True)
table.add_row("Charmander", "Fire", "True", style="red")
table.add_row("Bulbasaur", "Grass", "False", style="blue")
table.add_row("Squirtle", "Water", "False", style="green")

console.print(table)
console.print("\n[bold red]Your turn! Enter some pokemon:[/bold red]")
table2 = Table(title="Pokemon")
table2.add_column("Name", no_wrap=True)
table2.add_column("Type(s)", no_wrap=True)
table2.add_column("Shiny?", no_wrap=True)

def validateType(pokemon_type):
    valid_types = {"normal", "fire", "fighting", "water", "flying", "grass", "poison", "electric", "ground", "psychic", "rock", "ice", "bug", "dragon", "ghost", "dark", "steel", "fairy"}
    return pokemon_type.lower() in valid_types

def addPokemon():
    usedTable = Table(title="Pokemon")
    usedTable.add_column("Name", no_wrap=True)
    usedTable.add_column("Type(s)", no_wrap=True)
    usedTable.add_column("Shiny?", no_wrap=True)
    console.print(usedTable)
    while True:
        name = input("Enter Pokemon name ('confirm' to finish and save data to a file, 'incorrect' to clear data): ")
        if name.lower() == 'confirm':
            save_table_to_text(usedTable)
            console.print("\n[bold red]Pokemon data has been saved to 'pokemonData.txt'![/bold red]")
            break
        elif name.lower() == 'incorrect':
            addPokemon()
            break
        while True:
            type_ = input("Enter Pokemon type: ")
            if validateType(type_):
                break
            else:
                print("Invalid type. Please enter a valid Pokemon type from the following: normal, fire, fighting, water, flying, grass, poison, electric, ground, psychic, rock, ice, bug, dragon, ghost, dark, steel, or fairy")
        shiny = input("Is it shiny? (True/False): ")
        color_map = {
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
        }
        rowColor = color_map.get(type_.lower(), "white")
        usedTable.add_row(name, type_, shiny, style=rowColor)
        console.print(usedTable)

def save_table_to_text(table):
    f = open('pokemonData.txt', 'a')
    for row_index in range(len(table.columns[0]._cells)):
        row_data = [str(column._cells[row_index]) for column in table.columns]
        f.write(', '.join(row_data) + '\n')
        print(row_data)

# Start the process
addPokemon()
from rich.console import Console
from rich.table import Table

console = Console()

console.print("Here are some data examples:", style="bold red")

table = Table(title="Pokemon")
table.add_column("Name", no_wrap=True)
table.add_column("Type(s)", no_wrap=True)
table.add_column("Shiny?", no_wrap=True)
table.add_row("Charmander", "Fire", "True", style="red")
table.add_row("Bulbasaur", "Grass", "False", style="blue")
table.add_row("Squirtle", "Water", "False", style="green")

console.print(table)
console.print("\n[bold red]Your turn! Enter some pokemon:[/bold red]")

console.print(table)

def validateType(pokemon_type):
    valid_types = {"normal", "fire", "fighting", "water", "flying", "grass", "poison", "electric", "ground", "psychic", "rock", "ice", "bug", "dragon", "ghost", "dark", "steel", "fairy"}
    return pokemon_type.lower() in valid_types

def addPokemon(table):
    while True:
        name = input("Enter Pokemon name ('exit' to finish): ")
        if name.lower() == 'exit':
            break
        while True:
            type_ = input("Enter Pokemon type(s): ")
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
        table.add_row(name, type_, shiny, style=rowColor)
        console.print(table)
addPokemon(table)
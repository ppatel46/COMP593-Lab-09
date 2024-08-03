import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests

class PokemonInfoViewer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Pokémon Info Viewer")

        # Create frames
        self.entry_frame = tk.Frame(self.root, padx=10, pady=10)
        self.info_frame = tk.LabelFrame(self.root, text="Info", padx=10, pady=10)
        self.stats_frame = tk.LabelFrame(self.root, text="Stats", padx=10, pady=10)

        # Create widgets
        self.pokemon_name_label = tk.Label(self.entry_frame, text="Pokémon Name:")
        self.pokemon_name_entry = tk.Entry(self.entry_frame)
        self.get_info_button = tk.Button(self.entry_frame, text="Get Info", command=self.get_info)

        self.name_label = tk.Label(self.info_frame, text="Name: ")
        self.type_label = tk.Label(self.info_frame, text="Type(s): ")
        self.height_label = tk.Label(self.info_frame, text="Height: ")
        self.weight_label = tk.Label(self.info_frame, text="Weight: ")

        self.hp_label = tk.Label(self.stats_frame, text="HP: ")
        self.hp_value_label = ttk.Progressbar(self.stats_frame, length=200, maximum=255)
        self.attack_label = tk.Label(self.stats_frame, text="Attack: ")
        self.attack_value_label = ttk.Progressbar(self.stats_frame, length=200, maximum=255)
        self.defense_label = tk.Label(self.stats_frame, text="Defense: ")
        self.defense_value_label = ttk.Progressbar(self.stats_frame, length=200, maximum=255)
        self.special_attack_label = tk.Label(self.stats_frame, text="Special Attack: ")
        self.special_attack_value_label = ttk.Progressbar(self.stats_frame, length=200, maximum=255)
        self.special_defense_label = tk.Label(self.stats_frame, text="Special Defense: ")
        self.special_defense_value_label = ttk.Progressbar(self.stats_frame, length=200, maximum=255)
        self.speed_label = tk.Label(self.stats_frame, text="Speed: ")
        self.speed_value_label = ttk.Progressbar(self.stats_frame, length=200, maximum=255)

        # Layout widgets
        self.entry_frame.pack(pady=10)
        self.pokemon_name_label.pack(side=tk.LEFT)
        self.pokemon_name_entry.pack(side=tk.LEFT, padx=5)
        self.get_info_button.pack(side=tk.LEFT, padx=5)

        self.info_frame.pack(padx=10, pady=5, fill="x")
        self.name_label.grid(row=0, column=0, sticky="w")
        self.type_label.grid(row=1, column=0, sticky="w")
        self.height_label.grid(row=2, column=0, sticky="w")
        self.weight_label.grid(row=3, column=0, sticky="w")

        self.stats_frame.pack(padx=10, pady=5, fill="x")
        self.hp_label.grid(row=0, column=0, sticky="w")
        self.hp_value_label.grid(row=0, column=1)
        self.attack_label.grid(row=1, column=0, sticky="w")
        self.attack_value_label.grid(row=1, column=1)
        self.defense_label.grid(row=2, column=0, sticky="w")
        self.defense_value_label.grid(row=2, column=1)
        self.special_attack_label.grid(row=3, column=0, sticky="w")
        self.special_attack_value_label.grid(row=3, column=1)
        self.special_defense_label.grid(row=4, column=0, sticky="w")
        self.special_defense_value_label.grid(row=4, column=1)
        self.speed_label.grid(row=5, column=0, sticky="w")
        self.speed_value_label.grid(row=5, column=1)

    def get_info(self):
        pokemon_name = self.pokemon_name_entry.get().strip()
        if not pokemon_name:
            messagebox.showerror("Error", "Please enter a Pokémon name")
            return

        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
            response.raise_for_status()
            data = response.json()
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Unable to fetch information for '{pokemon_name}' from the PokéAPI.")
            return

        self.name_label.config(text=f"Name: {data['name'].capitalize()}")
        types = [t['type']['name'] for t in data['types']]
        self.type_label.config(text=f"Type(s): {', '.join(types)}")
        self.height_label.config(text=f"Height: {data['height']} dm")
        self.weight_label.config(text=f"Weight: {data['weight']} hg")

        self.hp_value_label['value'] = data['stats'][0]['base_stat']
        self.attack_value_label['value'] = data['stats'][1]['base_stat']
        self.defense_value_label['value'] = data['stats'][2]['base_stat']
        self.special_attack_value_label['value'] = data['stats'][3]['base_stat']
        self.special_defense_value_label['value'] = data['stats'][4]['base_stat']
        self.speed_value_label['value'] = data['stats'][5]['base_stat']

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    viewer = PokemonInfoViewer()
    viewer.run()
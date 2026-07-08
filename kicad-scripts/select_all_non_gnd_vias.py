from kipy import KiCad

kicad = KiCad()
board = kicad.get_board()

ground_nets = {"GND", "AGND", "PGND", "GNDPWR"}

bad_vias = [
    via for via in board.get_vias()
    if via.net.name not in ground_nets
]

board.clear_selection()
board.add_to_selection(bad_vias)

print(f"Selected {len(bad_vias)} vias not on ground nets.")

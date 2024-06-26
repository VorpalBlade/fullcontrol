default_initial_settings = {
    "name": "Cubicon Style Plus-A15",
    "manufacturer": "Cubicon",
    "start_gcode": "M911 Style Plus-A15\nM201 X400 Y400\nM202 X400 Y400\nG28 ; Home\n;Prime the extruder\nG92 E0\nG1 F200 E3\nG92 E0",
    "end_gcode": "M104 S0\nM140 S0\nM904\nM117 Print completed! \nM84",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 150,
    "build_volume_y": 150,
    "build_volume_z": 150,
}

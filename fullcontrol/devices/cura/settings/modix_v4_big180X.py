default_initial_settings = {
    "name": "Modix V4 BIG-180X",
    "manufacturer": "Modix",
    "start_gcode": "G28 ; home all axes",
    "end_gcode": "M83 ; extruder relative moves \nG1 E-5 F2700 ;retract a bit \nG10 P0 S0 R0 ; turn off extruder 0 \nM106 S0 ; turn off fans \nT-1 P0 ; deselect any tools \nG4 P1 ; dwell 1ms \nG91 ;relative positioning \nG1 Z2 F500 ; Move print head up 2mm \nG90 ; absolute positioning \nG1 X{0+2} Y{data['build_volume_y']-2} F6000 ; move to the back left \nM84 ; disable motors",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 250.0,
    "dia_feed": 1.75,
    "build_volume_x": 1800,
    "build_volume_y": 600,
    "build_volume_z": 600,
}

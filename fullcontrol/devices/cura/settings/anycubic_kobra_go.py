default_initial_settings = {
    "name": "Anycubic Kobra Go",
    "manufacturer": "Anycubic",
    "start_gcode": "M140 S[first_layer_data['bed_temp']erature]; Heat bed\nM104 S[first_layer_temperature\n            ]; Heat extruder\nG21 ;metric values\nG90 ;absolute positioning\nM82 ;set extruder to absolute mode\nG28 ; Home all axes\nG92 E0 ; Reset Extruder\nM420 S1 ; Enable Bed Levelling Mesh\nM190 S[first_layer_data['bed_temp']erature\n            ]; Wait for bed to get up to temperature\nM109 S[first_layer_temperature\n            ]; Wait for extruder to get up to temperature\nG1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed\nG1 X2 Y20 Z0.3 F5000.0 ; Move to start position\nG1 X2 Y200.0 Z0.3 F1500.0 E15 ; Draw the first line\nG1 X2.4 Y200.0 Z0.3 F5000.0 ; Move to side a little\nG1 X2.4 Y20 Z0.3 F1500.0 E30 ; Draw the second line\nG92 E0 ; Reset Extruder\nG1 Z2.0 F3000 ; Move Z Axis up little to prevent scratching of Heat Bed\nG1 F2400 E-1\nG1 X5 Y20 Z0.3 F5000.0 ; Move over to prevent blob squish",
    "end_gcode": "M400 ; Wait for current moves to finish\nM220 S100 ; Reset Speed factor override percentage to default (100%)\nM221 S100 ; Reset Extrude factor override percentage to default (100%)\nG91 ; Set coordinates to relative\nG1 F2400 E-1 ; Retract filament 3mm at 40mm/s to prevent stringing\nG0 F5000 Z20 ; Move Z Axis up 20mm to allow filament ooze freely\nG90 ; Set coordinates to absolute\nG0 X0 Y220 F5000 ; Move Heat Bed to the front for easy print removal\nM104 S0 ; turn off extruder\nM140 S0 ; turn off bed\nM84 ; Disable stepper motors\n; End of custom end GCode",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 222,
    "build_volume_y": 222,
    "build_volume_z": 250,
}

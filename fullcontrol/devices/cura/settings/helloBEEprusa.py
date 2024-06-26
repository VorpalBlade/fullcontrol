default_initial_settings = {
    "name": "Hello Bee Prusa",
    "manufacturer": "Beeverycreative",
    "start_gcode": "; -- START GCODE --\nG21                     ;set units to millimetres\nG90                     ;set to absolute positioning\nM107                    ;set fan speed to zero (turned off)\nG28 X0 Y0               ;move to the X/Y origin (Home)\nG28 Z0                  ;move to the Z origin (Home)\nG92 E0                  ;zero the extruded length\nG1 F3600                ;set feedrate to 60 mm/sec\nM420 S1 \n; -- end of START GCODE --",
    "end_gcode": "; -- END GCODE --\nM104 S0                 ;set extruder temperature to zero (turned off)\nM140 S0                 ;set bed temperature to zero (turned off)\nG28 X0 Y0               ;move to the X/Y origin (Home)\nM84                     ;turn off steppers\n; -- end of END GCODE --",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 185,
    "build_volume_y": 200,
    "build_volume_z": 190,
}

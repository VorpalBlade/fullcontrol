default_initial_settings = {
    "name": "Kossel Pro",
    "manufacturer": "Johann",
    "start_gcode": "; info: M303 E0 S200 C8 ; Pid auto-tune \n\nM140 S{data['bed_temp']}; Start heating up the base\nG28 ; Home to top 3 endstops\n; Autolevel and adjust first layer\n; Adjust this value to fit your own printer!  (positive is thicker)\n; This default value is intentionally very high to accommodate the\n; variety of print heads used with this printer.  Many of you will\n; need tiny values like Z0 or Z0.1.  Use feeler gauges to dial this\n; in as accurately as possible.\nG29 Z10\n\n; Squirt and wipe ;\nM109 S220 ; Wait for the temp to hit 220\nG00 X125 Y-60 Z0.1 ;\nG92 E0 ;\nG01 E25 F100 ; Extrude a little bit to replace oozage from auto levelling\nG01 X90 Y-50 F6000 ;\nG01 Z5 ;\n\n; Set the extruder to the requested print temperature\nM104 S{data['nozzle_temp']}\n",
    "end_gcode": "M104 S0 ; turn off temperature\nM140 S0 ; turn off bed\nG28 ; home all axes\nM84 ; disable motors\n",
    "bed_temp": 60,
    "nozzle_temp": 210,
    "material_flow_percent": 100,
    "print_speed": 60,
    "travel_speed": 120,
    "dia_feed": 2.85,
    "build_volume_x": 240,
    "build_volume_y": 240,
    "build_volume_z": 240,
}

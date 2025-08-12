import time as time_module  # Import time module with an alias
from datetime import datetime

# --- CONSTANTS & DEFINITIONS ---
PUMP_HP = 1.5
FERTIGATION_TIME = "08:00"
WATER_ONLY_TIMES = ["10:00", "12:00", "14:00", "16:00"]
T2 = 15  # Fertigation runtime in minutes
Y = 10    # Water runtime in minutes
P_MIN = 20  # Minimum safe operating pressure (example value)

# --- GENERAL RULES ---
valve_states = {
    "A": "CLOSED",
    "B": "CLOSED",
    "C": "CLOSED",
    "D": "CLOSED",
    "E": "CLOSED"
}
pump_state = "OFF"

def log(message):
    print(f"{datetime.now()}: {message}")

def close_all_valves():
    global valve_states
    for valve in valve_states:
        valve_states[valve] = "CLOSED"
    log("All valves closed.")

def read_pressure():
    # Simulate reading pressure (example value)
    return 25  # Example pressure value

def start_pump():
    global pump_state
    pump_state = "ON"
    log("Pump started.")

def stop_pump():
    global pump_state
    pump_state = "OFF"
    log("Pump stopped.")

def check_fertilizer_tank():
    # Simulate checking fertilizer tank level
    fertilizer_tank_level = 10  # Example level
    low_mark = 15  # Example low mark
    if fertilizer_tank_level <= low_mark:
        refill_fertilizer_tank()

def refill_fertilizer_tank():
    stop_pump()
    close_all_valves()
    open_valve("C")  # Water tank return
    open_valve("B")  # Fertilizer suction
    log("Attempting gravity refill...")
    
    # Simulate checking for flow
    flow = False  # Simulate no flow
    if not flow:
        start_pump()
        log("Waiting for fertilizer tank to fill...")
        time_module.sleep(5)  # Simulate waiting time
        stop_pump()
    
    close_valve("C")
    add_fertilizer()
    open_valve("A")  # Fertilizer return
    start_pump()
    log("Waiting for fertilizer to dissolve...")
    time_module.sleep(5)  # Simulate waiting time
    stop_pump()
    close_valve("A")
    close_valve("B")
    log("Fertilizer tank refilled & mixed.")

def add_fertilizer():
    # Placeholder function to simulate adding fertilizer
    log("Adding fertilizer to the tank.")

def open_valve(valve):
    global valve_states
    valve_states[valve] = "OPEN"
    log(f"{valve} opened.")

def close_valve(valve):
    global valve_states
    valve_states[valve] = "CLOSED"
    log(f"{valve} closed.")

def check_pressure():
    if read_pressure() < P_MIN:
        stop_pump()
        close_all_valves()
        log("Aborted: Low pressure")
        return "FAIL"
    return "OK"

def fertigation_run():
    stop_pump()
    check_fertilizer_tank()
    close_valve("C")
    close_valve("D")  # Isolate water tank
    open_valve("A")
    open_valve("B")
    open_valve("E")  # Fertilizer loop + to drippers
    if check_pressure() == "FAIL":
        return
    start_pump()
    log(f"Waiting for fertigation to complete for {T2} minutes...")
    time_module.sleep(T2 * 60)  # Simulate waiting time
    stop_pump()
    close_all_valves()
    log("Fertigation completed.")

def water_run():
    stop_pump()
    check_fertilizer_tank()
    close_valve("A")
    close_valve("B")  # Isolate fertilizer tank
    open_valve("C")
    open_valve("D")
    open_valve("E")  # Water loop + to drippers
    if check_pressure() == "FAIL":
        return
    start_pump()
    log(f"Waiting for water run to complete for {Y} minutes...")
    time_module.sleep(Y * 60)  # Simulate waiting time
    stop_pump()
    close_all_valves()
    log("Water run completed.")

# --- MAIN DAILY LOOP ---
def main():
    while True:
        current_time = datetime.now().strftime("%H:%M")
        if current_time == FERTIGATION_TIME:
            fertigation_run()
        
        for time in WATER_ONLY_TIMES:
            if current_time == time:
                water_run()
        
        time_module.sleep(60)  # Check every minute

if __name__ == "__main__":
    main()

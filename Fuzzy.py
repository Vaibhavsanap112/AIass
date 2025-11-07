#& "C:\Program Files\Python312\python.exe" -m pip install networkx
#& "C:\Program Files\Python312\python.exe" -m pip install numpy matplotlib scikit-fuzzy python-constraint networkx



import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Input variables
temp = ctrl.Antecedent(np.arange(0, 41, 1), 'Temperature')
humid = ctrl.Antecedent(np.arange(0, 101, 1), 'Humidity')
fan = ctrl.Consequent(np.arange(0, 101, 1), 'FanSpeed')

# Membership functions
temp['low'] = fuzz.trimf(temp.universe, [0, 0, 20])
temp['medium'] = fuzz.trimf(temp.universe, [10, 20, 30])
temp['high'] = fuzz.trimf(temp.universe, [20, 40, 40])

humid['low'] = fuzz.trimf(humid.universe, [0, 0, 50])
humid['high'] = fuzz.trimf(humid.universe, [50, 100, 100])

fan['slow'] = fuzz.trimf(fan.universe, [0, 0, 50])
fan['medium'] = fuzz.trimf(fan.universe, [25, 50, 75])
fan['fast'] = fuzz.trimf(fan.universe, [50, 100, 100])

# Rules
rule1 = ctrl.Rule(temp['high'] | humid['high'], fan['fast'])
rule2 = ctrl.Rule(temp['medium'], fan['medium'])
rule3 = ctrl.Rule(temp['low'] & humid['low'], fan['slow'])

# Control system
fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
fan_sim = ctrl.ControlSystemSimulation(fan_ctrl)

# ---- User Input ----
t = float(input("Enter Temperature (0-40): "))
h = float(input("Enter Humidity (0-100): "))
fan_sim.input['Temperature'] = t
fan_sim.input['Humidity'] = h
fan_sim.compute()

print(f"Recommended Fan Speed: {fan_sim.output['FanSpeed']:.2f}")

# ------------------------------------------------------
# EXPLANATION OF THE CODE (FUZZY LOGIC FAN SPEED CONTROL)
# ------------------------------------------------------

# 📘 AIM:
# To recommend the fan speed based on **temperature** and **humidity** using 
# a **Fuzzy Logic System**.

# ------------------------------------------------------
# 🧩 CONCEPT USED
# ------------------------------------------------------
# **Fuzzy Logic**:
# - Deals with reasoning that is approximate rather than exact.
# - Inputs (temperature, humidity) and output (fan speed) are represented as **fuzzy sets**.
# - **Rules** are applied to infer output based on the degree of membership.

# ------------------------------------------------------
# 🧩 CODE EXPLANATION (LINE BY LINE)
# ------------------------------------------------------

# Import Libraries
# import numpy as np
# import skfuzzy as fuzz
# from skfuzzy import control as ctrl
# → numpy is for numerical operations
# → skfuzzy is for fuzzy logic operations

# ------------------------------------------------------
# 1️⃣ DEFINE INPUTS AND OUTPUT
# ------------------------------------------------------
# Inputs (Antecedents)
# temp = ctrl.Antecedent(np.arange(0, 41, 1), 'Temperature')   # 0-40 °C
# humid = ctrl.Antecedent(np.arange(0, 101, 1), 'Humidity')    # 0-100 %
# Output (Consequent)
# fan = ctrl.Consequent(np.arange(0, 101, 1), 'FanSpeed')      # 0-100 %

# ------------------------------------------------------
# 2️⃣ DEFINE MEMBERSHIP FUNCTIONS
# ------------------------------------------------------
# Temperature
# temp['low'] = fuzz.trimf(temp.universe, [0, 0, 20])
# temp['medium'] = fuzz.trimf(temp.universe, [10, 20, 30])
# temp['high'] = fuzz.trimf(temp.universe, [20, 40, 40])

# Humidity
# humid['low'] = fuzz.trimf(humid.universe, [0, 0, 50])
# humid['high'] = fuzz.trimf(humid.universe, [50, 100, 100])

# Fan Speed
# fan['slow'] = fuzz.trimf(fan.universe, [0, 0, 50])
# fan['medium'] = fuzz.trimf(fan.universe, [25, 50, 75])
# fan['fast'] = fuzz.trimf(fan.universe, [50, 100, 100])

# → Membership functions define **how input/output values belong to fuzzy sets**

# ------------------------------------------------------
# 3️⃣ DEFINE RULES
# ------------------------------------------------------
# rule1 = ctrl.Rule(temp['high'] | humid['high'], fan['fast'])
# rule2 = ctrl.Rule(temp['medium'], fan['medium'])
# rule3 = ctrl.Rule(temp['low'] & humid['low'], fan['slow'])
# → Fuzzy rules that decide the fan speed:
# Example:
#   - If temperature is high OR humidity is high → fan speed is fast
#   - If temperature is medium → fan speed is medium
#   - If temperature is low AND humidity is low → fan speed is slow

# ------------------------------------------------------
# 4️⃣ CREATE CONTROL SYSTEM
# ------------------------------------------------------
# fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
# fan_sim = ctrl.ControlSystemSimulation(fan_ctrl)
# → Sets up the fuzzy control system and prepares it for input

# ------------------------------------------------------
# 5️⃣ USER INPUT & COMPUTATION
# ------------------------------------------------------
# t = float(input("Enter Temperature (0-40): "))
# h = float(input("Enter Humidity (0-100): "))
# fan_sim.input['Temperature'] = t
# fan_sim.input['Humidity'] = h
# fan_sim.compute()
# → Takes temperature and humidity from user
# → Computes the fuzzy output (fan speed) using the rules

# ------------------------------------------------------
# 6️⃣ DISPLAY OUTPUT
# ------------------------------------------------------
# print(f"Recommended Fan Speed: {fan_sim.output['FanSpeed']:.2f}")
# → Displays the recommended fan speed based on fuzzy reasoning

# ------------------------------------------------------
# 🧮 SAMPLE INPUT / OUTPUT
# ------------------------------------------------------
# Input:
# Enter Temperature (0-40): 30
# Enter Humidity (0-100): 70

# Output:
# Recommended Fan Speed: 86.25

# ------------------------------------------------------
# 🧠 SIMPLE UNDERSTANDING
# ------------------------------------------------------
# - Inputs (temperature, humidity) are mapped to fuzzy sets (low, medium, high).
# - Rules are applied using fuzzy logic operators (AND, OR).
# - Fuzzy output is defuzzified to get a crisp fan speed value.
# - Useful when precise thresholds are difficult to define.

# ------------------------------------------------------
# 🌍 REAL-TIME APPLICATIONS
# ------------------------------------------------------
# 1. Automatic fan speed control in smart homes.
# 2. Climate control systems in cars or offices.
# 3. Industrial ventilation systems.
# 4. Any system where approximate reasoning is needed.
# ------------------------------------------------------

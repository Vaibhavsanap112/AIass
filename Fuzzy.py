
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

temperature = ctrl.Antecedent(np.arange(0, 51, 1), "temperature")
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), "fan_speed")

temperature["cold"] = fuzz.trimf(temperature.universe, [0, 0, 20])
temperature["warm"] = fuzz.trimf(temperature.universe, [10, 25, 40])
temperature["hot"]  = fuzz.trimf(temperature.universe, [30, 50, 50])

fan_speed["low"]    = fuzz.trimf(fan_speed.universe, [0, 0, 50])
fan_speed["medium"] = fuzz.trimf(fan_speed.universe, [25, 50, 75])
fan_speed["high"]   = fuzz.trimf(fan_speed.universe, [50, 100, 100])

rule1 = ctrl.Rule(temperature["cold"], fan_speed["low"])
rule2 = ctrl.Rule(temperature["warm"], fan_speed["medium"])
rule3 = ctrl.Rule(temperature["hot"],  fan_speed["high"])

fan_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
fan_sim = ctrl.ControlSystemSimulation(fan_ctrl)

temp_value = float(input("Enter current temperature (°C): "))
fan_sim.input["temperature"] = temp_value
fan_sim.compute()

print(f"Recommended fan speed: {fan_sim.output['fan_speed']:.2f}%")

fan_speed.view(sim=fan_sim)

plt.show()
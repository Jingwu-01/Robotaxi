import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Example data
energy_data = """<energyOutput>
  <timestep time="0.00">
    <vehicle id="ev1" battery="48.76" consumption="0.24"/>
    <vehicle id="ev2" battery="47.90" consumption="0.35"/>
  </timestep>
  <timestep time="1.00">
    <vehicle id="ev1" battery="48.52" consumption="0.24"/>
    <vehicle id="ev2" battery="47.55" consumption="0.35"/>
  </timestep>
  <timestep time="2.00">
    <vehicle id="ev1" battery="48.28" consumption="0.24"/>
    <vehicle id="ev2" battery="47.20" consumption="0.35"/>
  </timestep>
</energyOutput>"""


root = ET.fromstring(energy_data)
time_steps = []
total_consumptions = []

# Iterate over each timestep
for timestep in root.findall("timestep"):
    time = float(timestep.get("time"))
    total_consumption = 0.0
    
    # For each timestep, sum the energy consumption for all vehicles
    for vehicle in timestep.findall("vehicle"):
        consumption = float(vehicle.get("consumption"))
        total_consumption += consumption
    
    time_steps.append(time)
    total_consumptions.append(total_consumption)

# Plot total energy consumption over time
plt.figure(figsize=(8, 6))
plt.plot(time_steps, total_consumptions, marker='o', linestyle='-', color='b')
plt.title("Total Energy Consumption at Each Timestep")
plt.xlabel("Time (s)")
plt.ylabel("Total Energy Consumption (kWh)")
plt.grid(True)
plt.show()
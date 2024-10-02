import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Sample emissions data. 
# TODO: Could directly read from an xml file. 
emissions_data = """<emissions>
  <timestep time="0.00">
    <vehicle id="veh1" CO2="0.2" CO="0.02" HC="0.001" NOx="0.003"/>
    <vehicle id="veh2" CO2="0.3" CO="0.03" HC="0.002" NOx="0.004"/>
  </timestep>
  <timestep time="1.00">
    <vehicle id="veh1" CO2="0.25" CO="0.02" HC="0.001" NOx="0.003"/>
    <vehicle id="veh2" CO2="0.35" CO="0.03" HC="0.002" NOx="0.004"/>
  </timestep>
</emissions>
"""

root = ET.fromstring(emissions_data)
time_steps = []
total_CO2_emissions = []

# Iterate over each timestep
for timestep in root.findall("timestep"):
    time = float(timestep.get("time"))
    total_consumption = 0.0
    
    # For each timestep, sum the CO2 for all vehicles
    for vehicle in timestep.findall("vehicle"):
        CO2 = float(vehicle.get("CO2"))
        total_CO2 += CO2
    
    time_steps.append(time)
    total_CO2_emissions.append(total_CO2)

# Plot total CO2 emissions over time
plt.figure(figsize=(8, 6))
plt.plot(time_steps, total_CO2_emissions, marker='o', linestyle='-', color='r')
plt.title("Total CO₂ Emissions at Each Timestep")
plt.xlabel("Time (s)")
plt.ylabel("Total CO₂ Emissions (g)")
plt.grid(True)
plt.show()
from Model import DrivingModel
import configparser

config = configparser.ConfigParser()
config.read('general.ini')
totalAgents = int(config["DRIVER AGENTS"]["n"])
simSteps = int(config["SIMULATION STEPS"]["steps"])
    
drivingModel = DrivingModel(totalAgents)
for i in range(simSteps):
    drivingModel.step()

drivers_data = drivingModel.driver_collector.get_agent_vars_dataframe()
drivers_data.to_csv('/home/dgarcia/TFG/Documentation/results1.csv', encoding='utf-8')
print(drivers_data)

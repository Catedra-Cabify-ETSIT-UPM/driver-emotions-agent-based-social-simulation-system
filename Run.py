from Model import DrivingModel

drivingModel = DrivingModel(200)
for i in range(180):
    drivingModel.step()

drivers_data = drivingModel.driver_collector.get_agent_vars_dataframe()
drivers_data.to_csv('/home/dgarcia/TFG/Documentation/results.csv', encoding='utf-8')
print(drivers_data)

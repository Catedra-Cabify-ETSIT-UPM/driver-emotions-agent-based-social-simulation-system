from mesa.datacollection import DataCollector

class DriverCollector(DataCollector):

    def collect(self, model):
        #Collect all the data for the given model object.
        if self.model_reporters:
            for var, reporter in self.model_reporters.items():
                self.model_vars[var].append(reporter(model))

        if self.agent_reporters:
            agent_records = self._record_agents(model)
            self._agent_records[model.schedule.steps] = list(agent_records)

import os

from AutoWSGR.daily_api import DailyOperation

operation = DailyOperation(f"{os.path.dirname(os.path.abspath(__file__))}/user_settings.yaml")
operation.run()

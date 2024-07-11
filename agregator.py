from dataclasses import dataclass
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from mongo_client import salary


@dataclass
class Agregator:
    dt_from: str
    dt_upto: str
    group_type: str

    def get_data_from_collection(self):
        data = salary.find({"dt": {"$gte": self.dt_from, "$lte": self.dt_upto + self.what_is_parametr()}})
        return data

    def what_is_parametr(self):
        if self.group_type == "hour":
            return timedelta(hours=1)
        elif self.group_type == "day":
            return timedelta(days=1)
        elif self.group_type == "month":
            return relativedelta(months=1)
        else:
            return timedelta(days=7)

    def nullable(self, dt: datetime):
        if self.group_type == "month":
            return dt.replace(day=1, hour=0, minute=0)
        if self.group_type == "day":
            return dt.replace(hour=0, minute=0)
        if self.group_type == "hour":
            return dt.replace(minute=0)

    def start_aggregation(self) -> dict:
        response = dict()

        param = self.what_is_parametr()
        data = self.get_data_from_collection()
        data = sorted(data, key=lambda x: x["dt"])

        while self.nullable(self.dt_from) <= self.dt_upto:
            response[self.nullable(self.dt_from).isoformat()] = 0
            self.dt_from += param

        for x in data:
            if x["dt"] <= self.dt_upto:
                response[self.nullable(x["dt"]).isoformat()] += x["value"]

        return {"dataset": list(response.values()), "labels": list(response.keys())}

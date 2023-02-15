from datetime import date


class ConvertDate:
    def __init__(self):
        self.hello = "world"

    def get_weekday(self, enter_date):
        chosen_date = enter_date.split("-")
        real_date = date(
            year=int(chosen_date[0]),
            month=int(chosen_date[1]),
            day=int(chosen_date[2])
        )
        return real_date.strftime("%A")

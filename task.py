from developer import Developer
from datetime import date


def colculet_date(start: date, end: date):
    if start.day + end.day > 30:
        if (start.month + (start.day + end.day) / 30) > 12:
            start.year = end.year + \
                (start.month + (start.day + end.day) / 30) // 12
            start.month = (start.month + (start.day + end.day) // 30) % 12
            start.day = (start.day + end.day) % 30
        else:
            start.month = start.month + (start.day + end.day) // 30
            start.day = (start.day + end.day) % 30
    else:
        start.day = start.day + end.day
    return date(start.year, start.month, start.day)


def difficulty_one_to_five(difficulty):
    if difficulty < 1:
        difficulty = 1
    if difficulty > 5:
        difficulty = 5
    return difficulty


class Task:
    def __init__(
        self,
        description_task: str,
        date_open: date,
        witch_project,
        day_work: int,
        difficulty,
        developer: Developer = None,
        completed: bool = False,
    ) -> None:
        self._description_task = description_task
        self._date_open = date_open
        self._date_end = colculet_date(date_open, day_work)
        self._witch_project = witch_project
        self._day_work = day_work
        self._difficulty = difficulty_one_to_five(difficulty)
        self._developer = developer
        if developer != None:
            self._reword = developer.experience * (
                developer.task_completed / developer.day_work
            )
        else:
            self._reword = 0
        self._completed = completed

    @property
    def description_task(self):
        return self._description_task

    @property
    def date_open(self):
        return self._date_open

    @property
    def date_end(self):
        return self._date_end

    @date_end.setter
    def date_end(self, x):
        self._date_end = x

    @property
    def witch_project(self):
        return self._witch_project

    # @witch_project.setter
    # def witch_project(self,x):
    #     self._witch_project=x
    @property
    def day_work(self):
        return self._day_work

    @day_work.setter
    def day_work(self, x):
        self._day_work = x

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, x):
        self._difficulty = x

    @property
    def developer(self):
        return self._developer

    @developer.setter
    def developer(self, x):
        self._developer = x

    @property
    def reword(self):
        return self._reword

    @property
    def completed(self):
        return self._completed

    @completed.setter
    def completed(self, x):
        self._completed = x

class Developer:
    def __init__(
        self, name:str, task_completed:int, day_work, reword, task_to_do
    ) -> None:
        self._name = name
        self._task_completed = task_completed
        self._day_work = day_work
        self._reword = reword
        self._task_to_do = task_to_do
        self._experience = 1

    @property
    def task_completed(self):
        return self._task_completed

    @task_completed.setter
    def task_completed(self, x):
        self._task_completed = x

    @property
    def day_work(self):
        return self._day_work

    @day_work.setter
    def day_work(self, x):
        self._day_work = x

    @property
    def reword(self):
        return self._reword

    @reword.setter
    def reword(self, x):
        self._reword += x

    @property
    def task_to_do(self):
        return self._task_to_do

    @task_to_do.setter
    def task_to_do(self, x):
        self._task_to_do = x

    @property
    def experience(self):
        return self._experience

    @experience.setter
    def experience(self, x):
        self._experience += x

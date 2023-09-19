from task import Task

# לא הספקתי לבדוק את הקוד בכלל 
class Project:
    def __init__(
        self, description: str, date_open: int, date_end, project_end=False
    ) -> None:
        self._description = description
        self._date_open = date_open
        self._date_end = date_end
        self._list_task = []
        self._list_developer = []
        self._task_to_do = []
        self._task_end = []
        self._cost_project = 0
        self._project_end = project_end

    @property
    def description(self):
        return self._description

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
    def list_task(self):
        return self._list_task

    # @list_task.setter
    # def list_task(self,x):
    #     self._list_task =x

    @property
    def list_developer(self):
        return self._list_developer

    # @list_developer.setter
    # def list_developer(self,x):
    #     self._list_developer =x

    @property
    def task_to_do(self):
        return self._task_to_do

    # @task_to_do.setter
    # def task_to_do(self,x):
    #     self._task_to_do =x

    @property
    def task_end(self):
        return self._task_end

    # @task_end.setter
    # def task_end(self,x):
    #     self._task_end =x

    @property
    def cost_project(self, list_developer):
        total = 0
        for i in list_developer:
            total += i._reword
        return total

    @cost_project.setter
    def cost_project(self, x):
        self._cost_project = x

    @property
    def project_end(self):
        return self._project_end

    @project_end.setter
    def project_end(self, x):
        self._project_end = x

    def add_task(self, new_task: Task):
        if new_task in self.list_task:
            raise "is already here !"
        elif new_task.witch_project == self.description:
            self._list_task.append(new_task.description_task)
            self._list_developer.append(new_task.developer)
            self._task_to_do.append(new_task.description_task)
        else:
            raise " in anther project "

    def remove_task(self, removing_task: Task):
        if removing_task.completed == False:
            self._list_task.pop(removing_task.description_task)
            self._list_developer.pop(removing_task.developer)
            self._task_to_do.pop(removing_task.description_task)

    def search_task(self, description):
        for i in self.list_task:
            if description == i.description_task:
                return i
        else:
            raise "not fond "

    def finish_task(self, finish_task: Task):
        if finish_task.developer in self.list_developer:
            finish_task.completed = True
            self._task_end.append(finish_task.description_task)
            self._list_developer.pop(finish_task.developer)
            self._task_to_do.pop(finish_task.description_task)
            finish_task.developer.reword
            finish_task.developer.experience
        else:
            raise " you can not do it, get outtttt"

from project.task import Task


class Section:

    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if any([x.name == new_task for x in self.tasks]):
            return f"Task is already in the section {self.name}"
        else:
            self.tasks.append(new_task)
            return f"Task {new_task} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in self.tasks:
            return f"Could not find task with the name {task_name}"
        else:
            self.completed = True
            return "Completed task {task_name}"

    def clean_section(self):
        removed_tasks = len(self.tasks)
        self.tasks.clear()
        return f"Cleared {removed_tasks} tasks."

    def view_section(self):
        result = f"Section {self.name}"
        for task in self.tasks:
            result += "\n" + f"{task.details()}"



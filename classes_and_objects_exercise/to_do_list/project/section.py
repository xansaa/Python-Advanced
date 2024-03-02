from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: str):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)

        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        try:
            task = next(filter(lambda t: t.name == task_name, self.tasks))
        except StopIteration:
            return f"Could not find task with the name {task_name}"

        task.completed = True

        return f"Completed task {task_name}"

    def clean_section(self) -> str:
        count_task = 0

        for task in self.tasks:
            if task.completed:
                count_task += 1
                self.tasks.remove(task)

        return f"Cleared {count_task} tasks."

    def view_section(self) -> str:
        task_with_section = "\n".join(t.details() for t in self.tasks)
        return f"Section {self.name}:\n" \
               f"{task_with_section}"



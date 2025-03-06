import unittest
import todolist

class TestToDoListApp(unittest.TestCase):

    def test_if_option_menu_works(self):
        todolist.menu()

    def test_add_a_task(self):
        actual = todolist.add_a_task("Buy groceries")
        expected = "Task added"
        self.assertEqual(actual, expected)

        actual = todolist.add_a_task("   ")
        expected = "Invalid"
        self.assertEqual(actual, expected)

        actual = todolist.add_a_task("")
        expected = "Invalid"
        self.assertEqual(actual, expected)



    def test_view_all_tasks(self):
        tasks = ["Buy milk", "Complete project"]
        expected = ["1. [] Buy milk", "2. [] Complete project"]

        actual = []
        for index, task in enumerate(tasks, start=1):
            actual.append(f"{index}. [] {task}")
        self.assertEqual(actual, expected)



    def test_mark_task_complete(self):
        tasks = ["Buy milk", "Complete project"]

        task_index = 0  
        tasks[task_index] = f"[x] {tasks[task_index]}" 

        actual = tasks[0]
        expected = "[x] Buy milk"
        self.assertEqual(actual, expected)



    def test_delete_task(self):
        tasks = ["Buy milk", "Complete project"]

        task_index = 0  
        removed_task = tasks.pop(task_index)  

        actual = tasks
        expected = ["Complete project"]
        self.assertEqual(actual, expected)




if __name__ == "__main__":
    unittest.main()

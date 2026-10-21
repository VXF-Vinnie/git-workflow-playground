import unittest

from todo import add_task, complete_task, format_task


class TodoTests(unittest.TestCase):
    def test_add_task(self):
        tasks = add_task([], "Buy groceries")
        self.assertEqual(tasks, [{"title": "Buy groceries", "done": False}])

    def test_complete_task(self):
        tasks = complete_task([{"title": "Study", "done": False}], 0)
        self.assertTrue(tasks[0]["done"])

    def test_format_task(self):
        task = {"title": "Study", "done": True}
        self.assertEqual(format_task(0, task), "0. [x] Study")


if __name__ == "__main__":
    unittest.main()

import unittest

from todo import add_task, complete_task, format_task


class TodoTests(unittest.TestCase):
    def test_add_task(self):
        tasks = add_task([], "Buy groceries")
        self.assertEqual(
            tasks, [{"title": "Buy groceries", "done": False, "priority": "normal"}]
        )

    def test_complete_task(self):
        tasks = complete_task([{"title": "Study", "done": False}], 0)
        self.assertTrue(tasks[0]["done"])

    def test_format_task(self):
        task = {"title": "Study", "done": True}
        self.assertEqual(format_task(0, task), "0. [x] Study")

    def test_format_high_priority(self):
        task = {"title": "Pay rent", "done": False, "priority": "high"}
        self.assertEqual(format_task(1, task), "1. [ ] Pay rent (!)")

    def test_format_due_date(self):
        task = {"title": "Essay", "done": False, "due": "Oct 25"}
        self.assertEqual(format_task(2, task), "2. [ ] Essay (due Oct 25)")

if __name__ == "__main__":
    unittest.main()

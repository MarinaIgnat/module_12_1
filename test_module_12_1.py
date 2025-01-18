import module_12_1 as mod
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        w = mod.Runner('Name')
        for i in range(10):
            w.walk()
        self.assertEqual(w.distance, 50)

    def test_run(self):
        r = mod.Runner('Name')
        for i in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        c_1 = mod.Runner('Name_1')
        c_2 = mod.Runner('Name_2')
        for i in range(10):
            c_1.run()
        for i in range(10):
            c_2.walk()
        self.assertNotEqual(c_1.distance, c_2.distance)


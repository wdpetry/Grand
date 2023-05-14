import Comment as c
import commentRunner as cr
import unittest

class Test_ave_engagement(unittest.TestCase):
    def test_average_engagement(self):
        comments = []
        comments += [c.Comment("test",0,0,True)]
        comments += [c.Comment("test",1,1,False)]
        self.assertEqual(cr.average_engagement(comments), 1, "Should be 1")

        comments = []
        comments += [c.Comment("test",100,200,True)]
        comments += [c.Comment("test",300,400,False)]
        self.assertEqual(cr.average_engagement(comments), 500, "Should be 500")


if __name__ == "__main__":
    unittest.main()
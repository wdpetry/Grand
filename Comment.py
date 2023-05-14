class Comment:
    def __init__(self,txt,up=0,down=0,flagged=False):
        self.text = txt;
        self.likes = up;
        self.dislikes = down;
        self.is_flagged = flagged

    def print_info(self):   
        print("Comment: %s" % self.text)
        print("Likes: %d, Dislikes: %d, Is Flagged: %s\n" % (self.likes,self.dislikes,self.is_flagged))

class Question(Comment):
    def __init__(self,txt,up=0,down=0,flagged=False,_topic="",ans=""):
        super().__init__(txt,up,down,flagged)
        self.topic = _topic
        self.answer = ans

    def print_info(self):
        print("Comment: %s" % self.text)
        print("Likes: %d, Dislikes: %d, Is Flagged: %s" % (self.likes,self.dislikes,self.is_flagged))
        print("Topic: %s" % self.topic)
        print("Answer: %s\n" % self.answer)

import Comment as c

def main():
    comments = [];           
    comments += [c.Comment("pineapple on pizza",10,10,True)]
    comments += [c.Comment("I liked this video",30,20,False)]
    comments += [c.Comment("LOL",4,1,False)]
    comments += [c.Question("Should I dislike Shrek?",1,15,True,"Blasphemy","No, you shouldn't")]
    comments += [c.Question("Why did the programmer quit their job?",12,12,False,"Coding","They didn't get arrays")]
    print_all(comments)
    ave_likes_dislikes = average_engagement(comments)
    print("AVERAGE ENGAGEMENT: %0.1f likes and dislikes per comment" % ave_likes_dislikes)

def average_engagement(the_comments):
    sum_likes_dislikes = 0
    for obj in the_comments:
        sum_likes_dislikes += obj.likes + obj.dislikes
    return sum_likes_dislikes/len(the_comments)

def print_all(the_comments):
    print("**ALL COMMENTS AND QUESTIONS**\n")
    for obj in the_comments:
        obj.print_info()
    print_unflagged(the_comments)

def print_unflagged(the_comments):
    print("**UNFLAGGED COMMENTS AND QUESTIONS**\n")
    for obj in the_comments:
        if(not obj.is_flagged):
            obj.print_info()

if __name__ == "__main__":
    main()

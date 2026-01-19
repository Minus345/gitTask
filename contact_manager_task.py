import json
import datetime

class User:
    def __init__(self, username):
        self.username = username
        self.posts = []
        self.likedPostSuccessfully = []

    """ this function creates a post for our super coll social media app form Kim :D """
    def createPost(self, content):
        post = {"u": self.username, "c": content, "l": [], "cm": []}
        self.posts.append(post)
        return post

    def printPosts(self):
        if len(self.posts) > 0:
            for i, post in enumerate(self.posts):
                print(u"Post {}:\n{}".format(i, post))
        else:
            print(u"No posts to display.")

    def likePost(self, post):
        if post not in self.likedPostSuccessfully:
            self.likedPostSuccessfully.append(post)
            post["l"].append(self.username)
            print("Post liked successfully.")
        else:
            print("You have already liked this post.")

    def cop(self, p, c):
        p["cm"].append({"u": self.username, "c": c})

class SM:
    def __init__(self):
        self.u = {}

    def cu(self, u):
        if u not in self.u:
            self.u[u] = User(u)
        else:
            print("User already exists.")

    def gu(self, u):
        return self.u.get(u)

    def mm(self):
        while True:
            print("Social Media Platform")
            print("1. Create User")
            print("2. Create Post")
            print("3. View Timeline")
            print("4. Like a Post")
            print("5. Comment on a Post")
            print("6. Exit")
            c = input("Enter your choice: ")
            if c == '1':
                u = input("Enter username: ")
                self.cu(u)
            elif c == '2':
                u = input("Enter username: ")
                us = self.gu(u)
                if us:
                    c = input("Enter post content: ")
                    p = us.cp(c)
                    print("Post created by {} with content: {}".format(p['u'], p['c']))
                else:
                    print("User not found.")
            elif c == '3':
                u = input("Enter username: ")
                us = self.gu(u)
                if us:
                    us.rt()
                else:
                    print("User not found.")
            elif c == '4':
                u = input("Enter username: ")
                us = self.gu(u)
                if us:
                    pi = int(input("Enter the post index you want to like: "))
                    au = input("Enter the author's username: ")
                    auu = self.gu(au)
                    if auu:
                        us.lp(auu.p[pi])
                    else:
                        print("Author not found.")
                else:
                    print("User not found.")
            elif c == '5':
                u = input("Enter username: ")
                us = self.gu(u)
                if us:
                    pi = int(input("Enter the post index you want to comment on: "))
                    au = input("Enter the author's username: ")
                    auu = self.gu(au)
                    if auu:
                        co = input("Enter your comment: ")
                        us.cop(auu.p[pi], co)
                    else:
                        print("Author not found.")
                else:
                    print("User not found.")
            elif c == '6':
                break
            else:
                print("Invalid choice. Please enter a valid option.")

def main():
    s = SM()
    s.mm()

if __name__ == "__main__":
    main()

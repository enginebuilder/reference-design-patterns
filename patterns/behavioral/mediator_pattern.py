from collections import defaultdict

class Forum:
    def post_message(self, topic, message, user):
        pass

class Message:
    def __init__(self, user, message) -> None:
        self.user = user
        self.message = message

class DiscussionForum(Forum):
    messages = defaultdict(list)
    def post_message(self, topic, message, user):
        self.messages[topic].append(Message(user, message))
    
    def print_messages(self, topic):
        for m in self.messages[topic]:
            print(f"{m.user.get_name()} said {m.message}")
    
class User:
    def __init__(self, name, forum) -> None:
        self.name = name
        self.forum = forum

    def get_name(self):
        return self.name
    
    def send_message(self, topic, message):
        self.forum.post_message(topic, message, self)

if __name__ == "__main__":
    forum = DiscussionForum()
    john = User("John", forum)
    llama = User("llama", forum)
    john.send_message("random", "python is the best")
    llama.send_message("random", "ChatGPT is the best")
    forum.print_messages("random")

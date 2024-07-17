# Define objects to be observed
class Event: 
    def __init__(self, title) -> None:
        self.title = title

# Define observers
class Participant:
    def __init__(self, email) -> None:
        self.email = email

class Calendar:

    def __init__(self) -> None:
        self.participants: list[Participant] = list()
    
    def invite(self, participant):
        self.participants.append(participant)
    
    def notify(self, event: Event):
        for p in self.participants:
            print(f"{p.email} invited to attend {event.title}")

    def add_event(self, event):
        self.notify(event)

if __name__ == "__main__":
    john = Participant("john@example.com")
    rob = Participant("rob@example.com")
    calendar = Calendar()
    calendar.invite(john)
    calendar.invite(rob)
    calendar.add_event(Event("Holi celebration!"))
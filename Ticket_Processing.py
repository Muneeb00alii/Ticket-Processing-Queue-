class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


def ticketing_process(total_queues, person_per_queue):
    # Creating Queues
    queues = [Queue() for _ in range(total_queues)]

    total_persons = total_queues * person_per_queue
    time = 2
    total_time = time * total_persons

    # Adding People in the Queues

    for i in range(total_queues):
        for j in range(person_per_queue):
            person_number = total_persons - (i * person_per_queue + j)
            queues[i].enqueue(f"Person {person_number}")

        queues[i].items.reverse()

    print(f"Total Persons in All Queue: {total_persons}\n")

    # Processing the Queues
    while True:
        all_empty = True
        # Selecting The Queue
        current_queue = queues[-1]
        while not current_queue.is_empty():
            all_empty = False

            # Printing All Queues After Processing
            print("\nCurrent state of queues:\n")
            for allQueues in queues:
                print(allQueues)

            # Processing the first person in the last queue
            person = current_queue.dequeue()
            print(f"\nProcessing Ticket of {person}")

            # Moving the last person of the 2nd last queue to the last queue

            if len(queues) > 1:
                for i in range(total_queues - 2 , -1, -1):
                    preceding_queue = queues[i]
                    last_person = preceding_queue.dequeue()
                    if last_person is not None:
                        queues[i + 1].enqueue(last_person)

        if all_empty:
            break

        # Calculating The Time

        if total_time > 60:
            minutes = total_time // 60
            seconds = total_time % 60
            print(f"\nTicket Collector takes {minutes} Minutes and {seconds} Seconds to Process all the Tickets.")
        else:
            print(f"\nTicket Collector takes {total_time} Seconds to Process all the Tickets.")

    print("\nAll People Processed. Enjoy the Movie!\n")

def run():
    total_queues = int(input("Enter the Number of Queues: "))
    person_per_queue = int(input("Enter the Number of Persons Per Queue: "))
    print()
    ticketing_process(total_queues, person_per_queue)

# run()

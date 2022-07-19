tickets = ["ticket1", "ticket2", "ticket3"]
iter_tickets = iter(tickets)


try:
    print(next(iter_tickets))
    print(next(iter_tickets))
    print(next(iter_tickets))
    print(next(iter_tickets))
    print(next(iter_tickets))
except Exception as e:
    print(e.message)
    print("Ya no se puede iterar mas")

# print(next(tickets)) error




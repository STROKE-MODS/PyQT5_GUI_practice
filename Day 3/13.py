class train:
    number_of_seats = 85
    train_status = "On going"
    number_of_ticket  = 0
    train_name = ["Rajdhani Express","EMU","Metro"]
    def seats_booking(him,seats):
        print("Your seats are booked.")
        him.number_of_seats = him.number_of_seats - seats
    def trains(him):
        for train in him.train_name:
            print(train)
yo = train()

work = input("What do you want to do ?\n---->")
if (work == "seats remaining"):
    print(yo.number_of_seats)
if (work == "book ticket"):
    seats = int(input("Enter the number of seats you want : "))
    yo.seats_booking(seats)
if (work == "train name"):
    yo.trains()
if (work == "train status"):
    print(yo.train_status)
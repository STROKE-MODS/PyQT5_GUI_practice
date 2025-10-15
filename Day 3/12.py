class train:
    number_of_seats = 85
    train_status = "On going"
    number_of_ticket  = 0
    train_name = ["Rajdhani Express","EMU","Metro"]
    def seats_booking(self,seats):
        print("Your seats are booked.")
        self.number_of_seats = self.number_of_seats - seats
    def trains(self):
        for train in self.train_name:
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

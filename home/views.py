from django.shortcuts import render, HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from .models import *
import logging, random, string
# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    #code
    return render(request, "index.html")

def travel(request):
    #code
    return render(request,"travel.html")

def health(request):
    #code
    return render(request,"health.html")

def assist(request):
    #code
    return render(request,"assist.html")

def bonus(request):
    #code
    return render(request,"bonus.html")

def discount(request):
    #code
    return render(request,"discount.html")

def life(request):
    #code
    return render(request,"life.html")

def retire(request):
    #code
    return render(request,"retire.html")

def train(request):
    #code
    return render(request,"train.html")

def wellness(request):
    #code
    return render(request,"wellness.html")

def initialBook(request):
    #code
    context = {}
    airports = Airport.objects.all()
    context['Airports'] = airports
    if request.method == "POST":
        departureloc = request.POST['departure air']   #portname
        print(departureloc)
        arrivalloc = request.POST['arrival air']
        print(arrivalloc)
        NoofPassengers = request.POST['NoOfPassengers']
        print(NoofPassengers)
        Flights = Flight.objects.filter(departure=departureloc,destination=arrivalloc,status='Scheduled')
        Airline_flights = Airline_Flight.objects.all()
        Airlines = Airline.objects.all()
        print(Airlines)
        if Flights==None:    
            logger.debug("No Flights Found. We apologize for inconvenience")
            return render(request, 'initialBook.html', context)
        context['Flights']=Flights
        print(context)
        context['Airline_flights']=Airline_flights
        print(context)
        context['Airlines']=Airlines
        print(context)
        context['NoOfPassengers'] = int(NoofPassengers)
        print(context)
        print(type(NoofPassengers))
        return render(request,'chooseFlights.html', context)
    
    return render(request, "initialBook.html", context)

def cancel(request):
    context = {}
    if request.method == "POST":
        reservationno = request.POST['ResNo']
        #Delete this reservation and move to book new Flight
        DeleteRes = Reservation.objects.get(reservationno = reservationno)
        Resflight = ReservedFlight.objects.get(reservationno = DeleteRes)
        Resflight.delete()
        PasCounts = PassengerCount.objects.filter(reservationno= DeleteRes)
        for passcount in PasCounts:
            passcount.delete()
        deleteBooks = Booking.objects.filter(reservationno = reservationno)
        UsersToBeDeleted = []
        PersonsToBeDeleted = []
        for delBook in deleteBooks:
            persondel = delBook.personid.personid
            belongs = Belonging.objects.get(personid = delBook.personid.personid) #requires a person object
            DelPass = Passenger.objects.get(personid = delBook.personid.personid)
            DelPass.delete()
            delLuggage = belongs.luggageno
            belongs.delete()
            delLuggage.delete()
            delBook.delete()
            prsnid = persondel.personid
            deluser = User.objects.get(id = prsnid)
            UsersToBeDeleted.append(deluser)
            PersonsToBeDeleted.append(persondel)
        ResTicks = ReservedTicket.objects.filter(reservationno = DeleteRes)
        for ResTick in ResTicks:
            deltick = ResTick.ticketno
            ResTick.delete()
            deltick.delete()
        logger.debug(f"Reservation No {DeleteRes.reservationno} successfully Deleted!")
        DeleteRes.delete()
        for delperson in PersonsToBeDeleted:
            delperson.delete()
        for deluser in UsersToBeDeleted:
            deluser.delete()
        return render(request, "index.html", context)
    return render(request, "cancel.html")

def change(request):
    #code
    context = {}
    if request.method == "POST":
        reservationno = request.POST['ResNo']
        #Delete this reservation and move to book new Flight
        DeleteRes = Reservation.objects.get(reservationno = reservationno)
        Resflight = ReservedFlight.objects.get(reservationno = DeleteRes)
        Resflight.delete()
        PasCounts = PassengerCount.objects.filter(reservationno= DeleteRes)
        for passcount in PasCounts:
            passcount.delete()
        deleteBooks = Booking.objects.filter(reservationno = reservationno)
        print(f"deleteBooks: {deleteBooks}")
        UsersToBeDeleted = []
        PersonsToBeDeleted = []
        for delBook in deleteBooks:
            print(f"delBook: {delBook}")
            persondel = delBook.personid.personid
            print(f"persondel: {persondel}")
            belongs = Belonging.objects.get(personid = delBook.personid.personid) #requires a person object
            print(f"belongs: {belongs}")
            DelPass = Passenger.objects.get(personid = delBook.personid.personid)
            print(f"DelPass: {DelPass}")
            DelPass.delete()
            delLuggage = belongs.luggageno
            print(f"delLuggage: {delLuggage}")
            belongs.delete()
            delLuggage.delete()
            delBook.delete()
            prsnid = persondel.personid
            print(f"prsnid: {prsnid}")
            deluser = User.objects.get(id = prsnid)
            print(f"deluser: {deluser}")
            UsersToBeDeleted.append(deluser)
            PersonsToBeDeleted.append(persondel) 
        print("\nLOOP ENDED\n")
        ResTicks = ReservedTicket.objects.filter(reservationno = DeleteRes)
        print(f"ResTicks: {ResTicks}")
        for ResTick in ResTicks:
            print(f"ResTick: {ResTick}")
            deltick = ResTick.ticketno
            print(f"deltick: {deltick}")
            ResTick.delete()
            deltick.delete()
        print("\nResTicks LOOP ENDED\n")    
        DeleteRes.delete()
        for delperson in PersonsToBeDeleted:
            delperson.delete()
        for deluser in UsersToBeDeleted:
            deluser.delete()
        airports = Airport.objects.all()
        context['Airports'] = airports
        return render(request, "initialBook.html", context)
    return render(request, "change.html")

def track(request):
    #code   
    context={}
    if request.method == "POST":
        ReservationNo = request.POST['ResNo']
        reservation = Reservation.objects.get(reservationno = ReservationNo)
        reservedtickets = ReservedTicket.objects.filter(reservationno = reservation)
        print(reservedtickets)
        persons = Person.objects.all()
        belongings = Belonging.objects.all()
        Airline_Flights = Airline_Flight.objects.all()
        Airlines = Airline.objects.all()
        context['Airlines'] = Airlines
        context['Airline_Flights'] = Airline_Flights
        context['Belongings'] = belongings
        context['Persons'] = persons
        context['Reservation'] = reservation
        context['ReservedTickets'] = reservedtickets
        return render(request,"confirmation.html",context)
    return render(request, "track.html")

def faq(request):
    #code    
    return render(request, "faq.html")

def EmpIndex(request):
    return render(request,"EmpIndex.html")

def EmpProfile(request):
    context = {}
    crnt_user = request.user
    print(f"crntuser: {crnt_user}")
    prsn = Person.objects.get(personid = crnt_user.id)
    print(f"prsn: {prsn}")
    context['Firstname'] = prsn.firstname
    print(f"{prsn.firstname} added")
    context['Middlename'] = prsn.middlename
    print(f"{prsn.middlename} added")
    context['Lastname'] = prsn.lastname
    print(f"{prsn.lastname} added")
    context['Age'] = prsn.age
    print(f"{prsn.age} added")
    context['Phoneno'] = prsn.phoneno
    print(f"{prsn.phoneno} added")
    context['Address'] = prsn.address
    print(f"{prsn.address} added")
    context['Gender'] = prsn.gender
    print(f"{prsn.gender} added")

    emp = Employee.objects.get(personid = prsn)
    print(f"emp: {emp}")
    context['Job'] = emp.job
    print(f"{emp.job} added")
    context['Qualification'] = emp.qualification
    print(f"{emp.qualification} added")
    context['Salary'] = emp.salary
    print(f"{emp.salary} added")
    context['Startdate'] = emp.startdate
    print(f"{emp.startdate} added")
    context['Enddate'] = emp.enddate
    print(f"{emp.enddate} added")
    return render(request,"EmpProfile.html", context)

def EmpFlights(request):
    if request.method == "POST":
        context = {}
        flightno = request.POST['FlightNo']
        flight = Flight.objects.get(flightno = flightno)
        context['ArrivalDate'] = flight.arrivaldate
        context['ArrivalTime'] = flight.arrivaltime
        context['DepartureTime'] = flight.departuretime
        context['DepartureDate'] = flight.departuredate
        context['Departure'] = flight.departure
        context['Destination'] = flight.destination
        context['Status'] = flight.status
        context['FlightNo'] = flightno
        airflight = Airline_Flight.objects.get(flightno = flight)
        flightairplane = FlightAssignment.objects.get(flightno = flight)
        belongings = Belonging.objects.all()
        context['Belongings'] = belongings
        context['PlaneNo'] = flightairplane.airplaneid.airplaneid
        context['planecapacity'] = flightairplane.airplaneid.capacity
        context['Airlinename'] = airflight.licenseno.airlinename
        context['PlaneFuel'] = flightairplane.airplaneid.fuel
        context['PlaneReg'] = flightairplane.airplaneid.registrationno
        context['Planemodel'] = flightairplane.airplaneid.modelno
        
        #flight to reserved flights to fetch all registrations of that flight
        flightreservations = ReservedFlight.objects.filter(flightno = flight)
        reservations = []
        for flyreservation in flightreservations:
            res = flyreservation.reservationno
            reservations.append(res)
        NoOfReservations = len(reservations)
        bookings = Booking.objects.all()
        passengers = Passenger.objects.all()
        persons = Person.objects.all()
        ReservedTickets = ReservedTicket.objects.all()
        context['ReservedTickets'] = ReservedTickets
        context['Persons'] = persons
        context['Passengers'] = passengers
        context['Bookings'] = bookings
        context['Reservations'] = reservations
        context['NoOfReservations'] = NoOfReservations
        return render(request, "FlightsToEmp.html", context)
    return render(request,"EmpFlights.html")

def EmpPolicy(request):
    return render(request,"EmpPolicy.html")

def about(request):
    #code    
    return render(request, "about.html")

def login_request(request):
    context = {}
    # Handles POST request
    if request.method == "POST":
        # Get username and password from request.POST dictionary
        username = request.POST['username']
        password = request.POST['psw']
        ChkEmp = request.POST.get('EmpChk','')
        print(ChkEmp)
        # Try to check if provide credential can be authenticated
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid, call login method to login current user
            login(request, user)
            if ChkEmp == "yes":
                return render(request, "EmpIndex.html")
            else:
                return redirect(index)                                #IDHAR AAO
        else:
            # If not, return to login page again
            logger.debug("Incorrect username and/or password.")
            return render(request, 'user_login.html', context)
    else:
        return render(request, 'user_login.html', context)
    
def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout user in the request
    logout(request)
    # Redirect user back to course list view
    return redirect(index)

def registration_request(request):
    context = {}
    # If it is a GET request, just render the registration page
    if request.method == 'GET':
        return render(request, 'user_registration.html', context)
    # If it is a POST request
    elif request.method == 'POST':
        # Get user information from request.POST
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']

        middlename = request.POST['middlename']
        phoneNo = request.POST['phno']
        address = request.POST['address']
        age = request.POST['age']
        gender = request.POST['gender']

        user_exist = False
        try:
            # Check if user already exists
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not, simply log this is a new user
            logger.debug("{} is new user.".format(username))
        # If it is a new user
        if not user_exist:
            # Create user in auth_user table
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            Person.objects.create(personid=user.pk,
                                  phoneno=phoneNo,
                                  address=address,
                                  age= age,
                                  gender=gender ,
                                  firstname= first_name,
                                  middlename=middlename,
                                  lastname= last_name )
            # Login the user and redirect to course list page
            login(request, user)
            return redirect(index)
        else:
            logger.debug("{} already exists!".format(username))
            return render(request, 'user_registration.html', context)
        
def finalBook(request,flightno=0, NoOfPassengers=0):
    context = {}
    loopvar = []
    for i in range(1,int(NoOfPassengers)+1):
        loopvar.append(i)
    context['loopvar'] = loopvar
    flight = Flight.objects.filter(flightno=int(flightno))
    context['Flight'] = flight
    context['NoOfPassengers'] = int(NoOfPassengers)
    context['TotalCost'] = 100*int(NoOfPassengers)
    if request.method=="POST":
        crntuser = request.user
        resDate = request.POST['Reservation Date']
        print(flight)
        for f in flight:
            reservation = Reservation.objects.create(flightno = f,
                                                    totalcost = 100*int(NoOfPassengers),
                                                    reservationdate = resDate,
                                                    bookingstatus = "Booked")
            flight=f
        for i in range(1,int(NoOfPassengers)+1):
            firstname = request.POST[f'firstname{i}']
            middlename = request.POST[f'middlename{i}']
            lastname = request.POST[f'lastname{i}']
            age = request.POST[f'age{i}']
            gender = request.POST[f'gender{i}']
            username = request.POST[f'username{i}']
            password = request.POST[f'psw{i}']
            phoneno = request.POST[f'phno{i}']
            address = request.POST[f'address{i}']
            passportno = request.POST[f'passport{i}']
            NoOfBags = request.POST[f'NoOfBags{i}']
            Luggagetype = request.POST[f'Luggagetype{i}']
            user_exist = False
            try:
                # Check if user already exists
                user = User.objects.get(username=username)
                print(user)
                person = Person.objects.get(personid = user.id)
                print(person)
                user_exist = True
            except:
                # If not, simply log this is a new user
                logger.debug("{} is new user.".format(username))
            
            # If it is a new user
            if not user_exist:
                print("User Exist nahi krta")
                # Create user in auth_user table
                user = User.objects.create_user(username=username, 
                                                first_name=firstname,
                                                last_name=lastname,
                                                password=password)
            
                person = Person.objects.create(personid=user.pk,
                                    phoneno=phoneno,
                                    address=address,
                                    age= age,
                                    gender=gender ,
                                    firstname= firstname,
                                    middlename=middlename,
                                    lastname= lastname)
            
            PassengerCount.objects.create(reservationno= reservation,
                                                     age=age,
                                                     name=firstname)
            
            prefix = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase)
            number = random.randint(1000, 9999)
            seatno = prefix + str(number)
            ticket = Ticket.objects.create(flightno = flight,
                                           fare = 100.0,
                                           personid = person,
                                           seatno=seatno)
            ReservedTicket.objects.create(reservationno = reservation,
                                          ticketno = ticket)
            luggage = Luggage.objects.create(noofbags = NoOfBags,
                                   type = Luggagetype)
            Belonging.objects.create(luggageno = luggage,
                                     personid = person)
            bookpassenger = Passenger.objects.create(ticketno=ticket, personid=person, flightno=flight, passportno=passportno)
            bookpassenger.reservation.set([reservation])

            if bookpassenger.personid == crntuser.id:        
                Booking.objects.create(reservationno = reservation,
                                                personid = bookpassenger)
    
        ReservedFlight.objects.create(reservationno = reservation,
                                        flightno = flight)
        flightair = Airline_Flight.objects.get(flightno = flightno)
        fm = FinancialManagement.objects.get(licenseno = flightair.licenseno)
        TotalCost = 100*int(NoOfPassengers)
        fm.revenue+=TotalCost
        fm.save()
        reservedtickets = ReservedTicket.objects.filter(reservationno = reservation)
        print(reservedtickets)
        persons = Person.objects.all()
        belongings = Belonging.objects.all()
        Airline_Flights = Airline_Flight.objects.all()
        Airlines = Airline.objects.all()
        context['Airlines'] = Airlines
        context['Airline_Flights'] = Airline_Flights
        context['Belongings'] = belongings
        context['Persons'] = persons
        context['Reservation'] = reservation
        context['ReservedTickets'] = reservedtickets
        return render(request,"confirmation.html",context)
    return render(request,"FinalBook.html",context)
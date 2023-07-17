from django.db import models

# class Airline_Flight(models.Model):
#     licenseno = models.OneToOneField('Airline', models.DO_NOTHING, db_column='LicenseNo', primary_key=True)  # Field name made lowercase. The composite primary key (LicenseNo, FlightNo) found, that is not supported. The first column is selected.
#     flightno = models.ForeignKey('Flight', models.DO_NOTHING, db_column='FlightNo')  # Field name made lowercase.
#     def __str__(self):
#         return f'{str(self.licenseno)}: {self.flightno}'
#     class Meta:
#         managed = True
#         db_table = 'airline_flight'
#         unique_together = (('licenseno', 'flightno'),)


class Airline(models.Model):
    airlinename = models.CharField(db_column='AirlineName', max_length=100, blank=True, null=True)  # Field name made lowercase.
    licenseno = models.IntegerField(db_column='LicenseNo', primary_key=True)  # Field name made lowercase.
    registeredcountry = models.CharField(db_column='RegisteredCountry', max_length=50, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.airlinename
    class Meta:
        managed = True
        db_table = 'airlines'
'''
class Flight(models.Model):
    flightno = models.CharField(db_column='FlightNo', max_length=100, primary_key=True)  # Field name made lowercase.
    arrivaldate = models.DateField(db_column='ArrivalDate', blank=True, null=True)  # Field name made lowercase.
    arrivaltime = models.TimeField(db_column='ArrivalTime', blank=True, null=True)  # Field name made lowercase.
    departuretime = models.TimeField(db_column='DepartureTime', blank=True, null=True)  # Field name made lowercase.
    departuredate = models.DateField(db_column='DepartureDate', blank=True, null=True)  # Field name made lowercase.
    destination = models.CharField(db_column='Destination', max_length=100, blank=True, null=True)  # Field name made lowercase.
    departure = models.CharField(db_column='Departure', max_length=100, blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return 'Flight#'+str(self.flightno)+f' ({self.departure} to {self.destination})'
    class Meta:
        managed = True
        db_table = 'flight'''
class Flight(models.Model):
    flightno = models.CharField(db_column='FlightNo', max_length=100, primary_key=True) 
    arrivaldate = models.DateField(db_column='ArrivalDate', blank=True, null=True) 
    arrivaltime = models.TimeField(db_column='ArrivalTime', blank=True, null=True)  
    departuretime = models.TimeField(db_column='DepartureTime', blank=True, null=True) 
    departuredate = models.DateField(db_column='DepartureDate', blank=True, null=True)  
    destination = models.CharField(db_column='Destination', max_length=100, blank=True, null=True) 
    departure = models.CharField(db_column='Departure', max_length=100, blank=True, null=True)  
    status = models.CharField(db_column='Status', max_length=50, blank=True, null=True) 
    #plane = ForeignKey(Airplane, through='flightassignment')
    def __str__(self):
        return 'Flight#'+str(self.flightno)+f' ({self.departure} to {self.destination})'
    class Meta:
        db_table = 'flight'

class Airline_Flight(models.Model):
    licenseno = models.ForeignKey('Airline', models.DO_NOTHING, db_column='LicenseNo')  # Field name made lowercase. The composite primary key (LicenseNo, FlightNo) found, that is not supported. The first column is selected.
    flightno = models.OneToOneField('Flight', models.DO_NOTHING, db_column='FlightNo', primary_key=True)  # Field name made lowercase.
    def __str__(self):
        return f'{str(self.licenseno)}: {self.flightno}'
    class Meta:
        managed = True
        db_table = 'airline_flight'
        unique_together = (('licenseno', 'flightno'),)

class Airport(models.Model):
    airportcode = models.CharField(db_column='AirportCode', primary_key=True, max_length=10)  # Field name made lowercase.
    contactinfo = models.CharField(db_column='ContactInfo', max_length=100, blank=True, null=True)  # Field name made lowercase.
    location = models.CharField(db_column='Location', max_length=100, blank=True, null=True)  # Field name made lowercase.
    portname = models.CharField(db_column='PortName', max_length=100, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.portname
    class Meta:
        managed = True
        db_table = 'airport'

'''
class Airplane(models.Model):
    airplaneid = models.IntegerField(db_column='AirplaneID', primary_key=True)  # Field name made lowercase. The composite primary key (AirplaneID, RegistrationNo) found, that is not supported. The first column is selected.
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  # Field name made lowercase.
    fuel = models.DecimalField(db_column='Fuel', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    registrationno = models.CharField(db_column='RegistrationNo', max_length=50)  # Field name made lowercase.
    modelno = models.CharField(db_column='ModelNo', max_length=50, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.registrationno
    class Meta:
        managed = True
        db_table = 'airplane'
        unique_together = (('airplaneid', 'registrationno'),)'''
class Airplane(models.Model):
    airplaneid = models.IntegerField(db_column='AirplaneID', primary_key=True)
    capacity = models.IntegerField(db_column='Capacity', blank=True, null=True)  
    fuel = models.DecimalField(db_column='Fuel', max_digits=10, decimal_places=2, blank=True, null=True)
    registrationno = models.CharField(db_column='RegistrationNo', max_length=50)
    modelno = models.CharField(db_column='ModelNo', max_length=50, blank=True, null=True) 
    flights = models.ManyToManyField('Flight', through='FlightAssignment')
    Airports = models.ManyToManyField(Airport, through='Reside')
    def __str__(self):
        return self.registrationno
    class Meta:
        managed = True
        db_table = 'airplane'
        unique_together = (('airplaneid', 'registrationno'),)

'''class FlightAssignment(models.Model):
    airplaneid = models.ManyToManyField(Airplane, models.DO_NOTHING, db_column='AirplaneId')  # Field name made lowercase. The composite primary key (AirplaneId, FlightNo) found, that is not supported. The first column is selected.
    flightno = models.ForeignKey(Flight, models.DO_NOTHING, db_column='FlightNo')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'flightassignment'
        unique_together = (('airplaneid', 'flightno'),)'''
class FlightAssignment(models.Model):
    airplaneid = models.ForeignKey('Airplane', models.DO_NOTHING, db_column='AirplaneId')
    flightno = models.OneToOneField('Flight', models.DO_NOTHING, db_column='FlightNo',primary_key=True) 
    # id = models.AutoField(primary_key=True)
    def __str__(self):
        return str(self.flightno)+' in '+str(self.airplaneid)
    
    class Meta:
        managed = True
        db_table = 'flightassignment'
        unique_together = (('airplaneid', 'flightno'),)



# class Airport(models.Model):
#     airportcode = models.CharField(db_column='AirportCode', primary_key=True, max_length=10)  # Field name made lowercase.
#     contactinfo = models.CharField(db_column='ContactInfo', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     location = models.CharField(db_column='Location', max_length=100, blank=True, null=True)  # Field name made lowercase.
#     portname = models.CharField(db_column='PortName', max_length=100, blank=True, null=True)  # Field name made lowercase.

#     def __str__(self):
#         return self.portname
    

#     class Meta:
#         managed = True
#         db_table = 'airport'

class Belonging(models.Model):
    luggageno = models.OneToOneField('Luggage', models.CASCADE, db_column='LuggageNo', primary_key=True)  # Field name made lowercase. The composite primary key (LuggageNo, PersonId) found, that is not supported. The first column is selected.
    personid = models.ForeignKey('Person', models.CASCADE, db_column='PersonId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'belonging'
        unique_together = (('luggageno', 'personid'),)


class Booking(models.Model):
    reservationno = models.ForeignKey('Reservation', models.CASCADE, db_column='ReservationNo')  # Field name made lowercase. The composite primary key (ReservationNo, PersonId) found, that is not supported. The first column is selected.
    personid = models.ForeignKey('Passenger', models.CASCADE, db_column='PersonId')  # Field name made lowercase.
    id = models.AutoField(primary_key=True)
    class Meta:
        db_table = 'booking'
        unique_together = (('reservationno', 'personid'),)

class Employee(models.Model):
    job = models.CharField(db_column='Job', max_length=50, blank=True, null=True)  # Field name made lowercase.
    qualification = models.CharField(db_column='Qualification', max_length=50, blank=True, null=True)  # Field name made lowercase.
    salary = models.DecimalField(db_column='Salary', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    startdate = models.DateField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    personid = models.OneToOneField('Person', models.DO_NOTHING, db_column='PersonId', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'employee'


class FinancialManagement(models.Model):
    licenseno = models.OneToOneField(Airline, models.DO_NOTHING, db_column='LicenseNo', primary_key=True)  # Field name made lowercase.
    revenue = models.DecimalField(db_column='Revenue', max_digits=10, decimal_places=2)  # Field name made lowercase. The composite primary key (Revenue, LicenseNo) found, that is not supported. The first column is selected.

    def __str__(self):
        return 'Revenue: '+self.licenseno.airlinename
    class Meta:
        managed = True
        db_table = 'financialmanagement'
        unique_together = (('revenue', 'licenseno'),)

class Luggage(models.Model):
    luggageno = models.AutoField(db_column='LuggageNo', primary_key=True)  # Field name made lowercase.
    noofbags = models.IntegerField(db_column='NoOfBags', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'luggage'


# class Passenger(models.Model):
#     ticketno = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='TicketNo', blank=True, null=True)  # Field name made lowercase.
#     personid = models.OneToOneField('Person', models.DO_NOTHING, db_column='PersonId', primary_key=True)  # Field name made lowercase.
#     flightno = models.ForeignKey(Flight, models.DO_NOTHING, db_column='FlightNo', blank=True, null=True)  # Field name made lowercase.
#     passportno = models.CharField(db_column='PassportNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
#     reservation = models.ManyToManyField(Reservation, through='Booking')
#     class Meta:
#         managed = True
#         db_table = 'passenger'


class PassengerCount(models.Model):
    reservationno = models.OneToOneField('Reservation', models.CASCADE, db_column='ReservationNo', primary_key=True)  # Field name made lowercase. The composite primary key (ReservationNo, Age, name) found, that is not supported. The first column is selected.
    age = models.IntegerField(db_column='Age')  # Field name made lowercase.
    name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'passengercount'
        unique_together = (('reservationno', 'age', 'name'),)


class Person(models.Model):
    personid = models.IntegerField(db_column='PersonId', primary_key=True)  # Field name made lowercase.
    phoneno = models.CharField(db_column='PhoneNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=100, blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=10, blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='Lastname', max_length=50, blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='Middlename', max_length=50, blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.firstname+' '+self.lastname
    class Meta:
        managed = True
        db_table = 'person'


class Reservation(models.Model):
    reservationno = models.AutoField(db_column='ReservationNo', primary_key=True)  # Field name made lowercase.
    flightno = models.ForeignKey(Flight, models.DO_NOTHING, db_column='FlightNo', blank=True, null=True)  # Field name made lowercase.
    totalcost = models.DecimalField(db_column='TotalCost', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    reservationdate = models.DateField(db_column='ReservationDate', blank=True, null=True)  # Field name made lowercase.
    bookingstatus = models.CharField(db_column='BookingStatus', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reservation'

class Passenger(models.Model):
    ticketno = models.ForeignKey('Ticket', models.DO_NOTHING, db_column='TicketNo', blank=True, null=True)  # Field name made lowercase.
    personid = models.OneToOneField('Person', models.CASCADE, db_column='PersonId', primary_key=True)  # Field name made lowercase.
    flightno = models.ForeignKey(Flight, models.DO_NOTHING, db_column='FlightNo', blank=True, null=True)  # Field name made lowercase.
    passportno = models.CharField(db_column='PassportNo', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reservation = models.ManyToManyField(Reservation, through='Booking')
    class Meta:
        managed = True
        db_table = 'passenger'

class ReservedFlight(models.Model):
    reservationno = models.OneToOneField(Reservation, models.CASCADE, db_column='ReservationNo', primary_key=True)  # Field name made lowercase.
    flightno = models.ForeignKey(Flight, models.CASCADE, db_column='FlightNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reservedflight'

class ReservedTicket(models.Model):
    reservationno = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='ReservationNo', blank=True, null=True)  # Field name made lowercase.
    ticketno = models.OneToOneField('Ticket', models.DO_NOTHING, db_column='TicketNo', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'reservedtickets'

class Reside(models.Model):
    airplaneid = models.OneToOneField(Airplane, models.DO_NOTHING, db_column='AirplaneId') 
    airportcode = models.ForeignKey(Airport, models.DO_NOTHING, db_column='AirportCode')  # Field name made lowercase.
    id = models.AutoField(primary_key=True)
    class Meta:
        managed = True
        db_table = 'reside'
        unique_together = (('airplaneid', 'airportcode'),)


class Ticket(models.Model):
    ticketno = models.AutoField(db_column='TicketNo', primary_key=True)  # Field name made lowercase.
    flightno = models.ForeignKey(Flight, models.DO_NOTHING, db_column='Flightno', blank=True, null=True)  # Field name made lowercase.
    seatno = models.CharField(db_column='SeatNo', max_length=10, blank=True, null=True)  # Field name made lowercase.
    fare = models.DecimalField(db_column='Fare', max_digits=10, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    personid = models.OneToOneField(Person,models.CASCADE,db_column='PersonId')
    class Meta:
        db_table = 'tickets'


class Work(models.Model):
    licenseno = models.OneToOneField(Airline, models.DO_NOTHING, db_column='LicenseNo', primary_key=True)  # Field name made lowercase. The composite primary key (LicenseNo, PersonId) found, that is not supported. The first column is selected.
    personid = models.ForeignKey(Person, models.DO_NOTHING, db_column='PersonId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'works'
        unique_together = (('licenseno', 'personid'),)

create table Students(
  Student_ID int not null primary key,
  LastName varchar(255),
  FirstName varchar(255),
  Address varchar(255),
  County varchar(255),
  Gender varchar(255)
);

create table Teachers(
  Teacher_ID int not null primary key,
  LastName varchar(255),
  FirstName varchar(255),
  Subject varchar(255)
);

create table Detention(
  Detention_ID int not null,
  Student_ID int not null,
  Teacher_ID int not null,
  Timee time,
  Datee date,
  Room varchar(255),
  foreign key (Student_ID) references Students(Student_ID),
  foreign key (Teacher_ID) references Teachers(Teacher_ID)
);

insert into Students values 
(1, 'Wash', 'Sam', 'Felixstowe', 'Suffolk', 'Male'),(2,'Liverton', 'James', 'Farm', 'Suffolk', 'Male'),(3,'Foster','Arlo','Debenham','Suffolk','Male');

insert into Teachers values (1, 'Foster', 'Arlo','Latin'),(2,'Liverton','James','Computer Science'), (3, 'Iacc', 'Rio', 'Fine Art');

insert into Detention values(3,1,1, '07:00', '2020-01-15', 'Lab 3');

#delete from Students where LastName = 'Liverton';

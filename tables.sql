
-- Identity
CREATE TABLE Identity (
PICno VARCHAR(20),	-- iska kitna rakhna hai size
PICtype VARCHAR(10) NOT NULL,
PIC BLOB NOT NULL,
PRIMARY KEY id_pk PICno,
CHECK (PICtype in ('BIRTH','PAN','DRIVING','AADHAR')));

-- Address
CREATE TABLE Address (
Houseno INT NOT NULL,
Streetno VARCHAR(10) NOT NULL,
PIN INT NOT NULL,
PO VARCHAR(20) NOT NULL,
Town VARCHAR(20) NOT NULL,
District VARCHAR(20) NOT NULL,
State VARCHAR(25) NOT NULL,
PRIMARY KEY ad_pk (Houseno,Streetno,PIN));

-- Polling
CREATE TABLE Polling (
Partno VARCHAR(11), -- iske size ka bhi koi idea nahi hai
Acno VARCHAR(30) NOT NULL, -- iska size bhi dekh lo
PRIMARY KEY po_pk (Partno),
FOREIGN KEY po_fk (Acno) REFERENCES Constituency(Acno);

-- Constituency
CREATE TABLE Constituency (
Acno VARCHAR(30),
Acname VARCHAR(30) NOT NULL,
Population INT,
PRIMARY KEY c_pk (Acno));

-- Election
CREATE TABLE Election (
Id VARCHAR(10),
year INT NOT NULL,
PRIMARY KEY e_pk (Id),
CHECK year > 1946);

-- Voter Table
CREATE TABLE Voter (
Voterid VARCHAR(20),
Name VARCHAR(50) NOT NULL,
Age INT NOT NULL,
Gender VARCHAR(6) NOT NULL,
DOB date NOT NULL,
DOI date NOT NULL,
DOA date NULL,
emailID VARCHAR(60) NULL,
Phoneno NUMBER(12,0) NULL,
PICno VARCHAR(20) NOT NULL,
Houseno INT NOT NULL,
Streetno VARCHAR(10) NOT NULL,
PIN INT NOT NULL,
Caste VARCHAR(3) NOT NULL,
Partno VARCHAR(11) NOT NULL,
PRIMARY KEY v_pk (Voterid),
CHECK Age >= 18,
CHECK (Gender in ('male','female')),
UNIQUE KEY v_uk (PICno),
FOREIGN KEY v_fk1 (Houseno,Streetno,PIN) REFERENCES Address(Houseno,Streetno,PIN),
CHECK (Caste in ('GEN','OBC','SC','ST')),
FOREIGN KEY v_fk2 Partno REFERENCES Polling(Partno));

-- Party
CREATE TABLE Party (
Partyid VARCHAR(10),
PartyName VARCHAR(20) NOT NULL,
Symbol BLOB NOT NULL,
Type VARCHAR(10) NOT NULL,
PRIMARY KEY pa_pk (Partyid),
CHECK (Type in ('National','Regional')));

-- Candidate
CREATE TABLE Candidate (
Candidateid VARCHAR(10),
Voterid VARCHAR(20) NOT NULL,
AC_participate VARCHAR(20) NOT NULL,
Type VARCHAR(3) NOT NULL,
Partyid VARCHAR(10),
PRIMARY KEY ca_pk (Candidateid),
FOREIGN KEY ca_fk1 (Voterid) REFERENCES Voter(Voterid),
FOREIGN KEY ca_fk2 (AC_participate) REFERENCES Constituency(Acno),
CHECK (Type in ('MLA','MP'),
FOREIGN KEY ca_fk3 (Partyid) REFERENCES Party(Partyid));

-- Statistics
CREATE TABLE Statistics (
Electionid VARCHAR(10) NOT NULL,
Partyid VARCHAR(10) NOT NULL,
STVotes INT,
SCVotes INT,
OBCVotes INT,
GENVotes INT,
FemaleVotes INT,
MaleVotes INT,
PRIMARY KEY st_pk (Electionid,Partyid),
FOREIGN KEY st_fk1 (Electionid) REFERENCES Election(Electionid),
FOREIGN KEY st_fk2 (Partyid) REFERENCES Party(Partyid));

-- Relation
CREATE TABLE Relation (
Voterid VARCHAR(20) NOT NULL,
Relationvoterid VARCHAR(20) NOT NULL,
Relation VARCHAR(10) NOT NULL,
PRIMARY KEY re_pk (Voterid,Relationvoterid),
CHECK (Relation in ('Father','Mother','Brother','Sister','Spouse')));




-- queries



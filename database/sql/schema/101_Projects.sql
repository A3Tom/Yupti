CREATE TABLE Projects (
    ProjectID INT IDENTITY PRIMARY KEY,
    ClientID INT NOT NULL,
    Name VARCHAR(255) NOT NULL,
    Description VARCHAR(1023),
    StartDate DATETIME NOT NULL,
    EndDate DATETIME,
    
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);
CREATE TABLE TimeEntries (
    TimeEntryID INT IDENTITY PRIMARY KEY,
    ProjectID INT NOT NULL,
    StartTime DATETIME NOT NULL,
    EndTime DATETIME NOT NULL,
    Description VARCHAR(1023),
    
    FOREIGN KEY (ProjectID) REFERENCES Projects(ProjectID)
);
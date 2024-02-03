USE Yupti;
GO

CREATE TABLE TimeEntryTags (
    TimeEntryID INT NOT NULL,
    TagID INT NOT NULL,
    PRIMARY KEY (TimeEntryID, TagID),
    FOREIGN KEY (TimeEntryID) REFERENCES TimeEntries(TimeEntryID),
    FOREIGN KEY (TagID) REFERENCES Tags(TagID)
);
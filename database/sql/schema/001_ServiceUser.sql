USE Yupti;
GO

CREATE LOGIN svc_yupti_dev WITH PASSWORD = 'QmlnUG9wZUZyYW5jbyE=';
GO

CREATE USER svc_yupti_dev FOR LOGIN svc_yupti_dev;
GO

EXEC sp_addrolemember 'db_datareader', 'svc_yupti_dev';
EXEC sp_addrolemember 'db_datawriter', 'svc_yupti_dev';
GO

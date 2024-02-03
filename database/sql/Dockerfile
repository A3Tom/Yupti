FROM mcr.microsoft.com/mssql/server:2019-latest
WORKDIR /app

COPY schema/ /app/schema
COPY run_sql.sh /app

ENV SA_PASSWORD=ThePopeRunsTheR3m0
ENV ACCEPT_EULA=Y

EXPOSE 1433

RUN /app/run_sql.sh
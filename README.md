# Yupti
So what are ye upti ?  

A permy question in ma life; I've always been shanner at trackin time so I wanted to get better at this and at the same time make an app usin tech I find interestin and fun but don't get to use on the daily.  

## Tech stack

- Docker / MSSql Server
- Python 3.x
- Vue 3

## So what am a buildin here ?

### MVP
- [X] Must be able to add clients
- [X] Must be able to add projects related to clients
- [ ] Ability to add a time entry with a start & end datetime via API and Web
- [ ] Ability to list time entries
- [ ] All entities must be editable
- [ ] An actual workin webpage

### Bonus Points
- [ ] User accounts with logins
- [ ] User Timezone info (who knew that'd be important in an app entirely focused around time...)
- [ ] Time entries tags
- [ ] List time entries by tag
- [ ] Exportable time entries
- [ ] API Unit tests
- [ ] Front end unit tests
- [ ] A timeline view of time entries by day
- [ ] A timeline view of time entries for the week

### Super Bonus Points
- [ ] CI/CD pipeline - look ano this is low hanging fruit but the bonus points are lookin heavy crowded
- [ ] Development environment deployment target
- [ ] A themed site, wit a pipe dream I know but am aiming for it
- [ ] E2E test suite


## Getting Started

First up; get the SQL Server docker image on the go, it's the quickest and least painful way 
```bash
docker build -t yupti-infrastructure .\database\sql\Dockerfile
docker run -e 'ACCEPT_EULA=Y' -e 'SA_PASSWORD=ThePopeRunsTheR3m0' -p 1433:1433 --name YuptiInfra -d yupti-infrastructure
```

Quality, now lets get make sure you're environment is set up sound.  

Rename `.env.sample` to just `.env` - the conn string should be sound if yer using the Dockerfile, good luck if yer no, especially if yer usin a SQLExpress instance...

Create a new py `venv` and install the requirements

```bash
py -m venv venv
pip install -r server\requirements.txt 
```

Right, off ye pop

```bash
py server\run.py
```


### Running http tests

The next step, though optional, is to scout oot the RestClient http test suite found in `\server\tests\http\` and sling some requests to the API and see the magic happen.
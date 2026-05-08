\# Incident Tracker



A CLI and REST API tool to track, manage and resolve incidents for teams.



\## Features

\- Add, list, update and delete incidents

\- Auto-incremented IDs

\- Status tracking (open, in\_progress, resolved)

\- Persistent JSON storage

\- REST API with Flask



\## Tech Stack

\- Python

\- Flask

\- JSON



\## Live API

https://incident-tracker-1-qdym.onrender.com/incidents



\## API Endpoints

\- GET /incidents — list all incidents

\- POST /incidents — add new incident

\- PUT /incidents/<id> — update incident

\- DELETE /incidents/<id> — delete incident



\## How to run locally

git clone https://github.com/Ender-Endes/incident-tracker

cd incident-tracker

pip install -r requirements.txt

python app.py


# ml-teams-tech-test - sijan rana

### Instructions



To run project:
1) Activate virtual environment ```venv\Scripts\activate```

2) Run ExportCSV and generate coverage via ```coverage run src/ExtractToCSV --calls data/calls.json --operators data/operators.json```

    - addtional parameters include:
        - ```--output OUTPUT``` for output filename e.g. 'report.csv'
        - ```--log-level LOGLEVEL``` to set log level e.g. 'info'

3) View coverage with ```coverage report```
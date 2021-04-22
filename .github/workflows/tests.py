name: Tests
on:
  push:
  workflow_dispatch:

jobs:
  tests:
    name: "Tests"
    runs-on: ubuntu-latest
    steps:
      - name: Checkout the repo
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8

      - name: Set up PostgreSQL
        uses: harmon758/postgresql-action@v1
        with:
          postgresql version: '11'
          postgresql: calaccess_raw

      - name: Install
        run: |
          python -m pip install --upgrade --no-cache-dir pip
          python -m pip install --no-cache-dir pipenv
          pipenv sync --dev
        shell: bash

      - name: Test
        run: |
          cp example/$DATABASE_SETTINGS.template example/settings_local.py
          pipenv run flake8 calaccess_raw
          pipenv run coverage run example/manage.py test calaccess_raw
          pipenv run coveralls

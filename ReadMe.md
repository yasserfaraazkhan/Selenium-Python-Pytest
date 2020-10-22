# Selenium Python Pytest

This repository contains a pytest setup for running e2e test against firefox and Chrome. There is option of running in Headless mode too. Dockerfile is available to run the tests easily without the setup hassle.

Requirements:
1. have python installed `brew install python`
2. Install `pyenv` to use different python versions
3. Make sure ChromeDriver and GekoDriver aer in executable path
`brew install chromedriver` and `brew install geckodriver` 
```
 pyenv local 3.6.8
 pyenv virtualenvwrapper_lazy
 mkvirtualenv venv
 pip install -r requirements.txt
```

### Selecting the base url

You can set the base url with `--baseUrl` cli argument (if running your app against different ENV):

```
py.test tests --base-url https://google.com
```
## Running the tests with docker

There is a make Makefile present to run the whole test suite with ``make test``. You can run `make build-no-cache` to completely rebuild the container.

### Developing tests

Running `make dev` will start a shell inside the Docker container with everything set up for you to run the tests.

Then either run tests inside the container or with docker compose you can select to run only specific files or tests

```
pytest test_ordering_checkout.py
docker-compose run e2e pytest test_ordering_checkout
```

## Without docker
### Running different test files in different browsers
`pytest --B firefox` # default is chrome

### Running in headless mode
`pytest --chromeOption=headless` # we can pass more chrome options

### To run test with reports:
`pytest --html=report.html`

### To run test in parallel:
`pytest -n 2` # 2 is number of browsers

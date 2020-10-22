build:
	docker-compose build

build-no-cache:
	docker-compose build --no-cache

test: build
	docker-compose run e2e py.test --chromeOptions=headless

dev: build
	docker-compose run e2e bash

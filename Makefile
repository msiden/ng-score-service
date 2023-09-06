build-deploy:
	docker build --no-cache -t ng-score-service:latest .

build-local:
	docker build --no-cache -t ng-score-service -f ./Dockerfile.dev .

build-test:
	docker build --no-cache -t ng-score-service-test -f ./Dockerfile.test .

run-local: build-local
	docker run -ti -p 8081:8081 ng-score-service

run-test: build-test
	docker run -ti ng-score-service-test bash

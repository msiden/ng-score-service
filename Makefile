build-deploy:
	docker build --no-cache -t ng-score-service:latest .

build-local:
	docker build --no-cache -t ng-score-service -f ./Dockerfile.dev .

run-local-docker: build-local
	docker run -ti --network="host" -p 8081:8081 ng-score-service

run-local:
	cd src/score-service/ && gunicorn -w 1 -b 0.0.0.0:8081 "app:app()" && cd ../../

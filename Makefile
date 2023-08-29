build-deploy:
	docker build --no-cache -t ng-score-service:latest .

build-local:
	docker build --no-cache -t ng-score-service -f ./Dockerfile.dev .

run-local: build-local
	docker run -ti -p 8081:8081 ng-score-service

# run-local-with-frontend: build-local
# 	docker-compose up

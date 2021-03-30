ENVIRONMENT := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))

ifneq ($(ENVIRONMENT),)
	include $(BASE_DIR)/security/$(ENVIRONMENT).sh
endif

include env.sh


all: help
dev:
	@#


# target: help - Display callable targets.
help: 
ifneq ($(ENVIRONMENT),)
	@#
else
	@egrep "^# target:" [Mm]akefile
endif


# target: build - build base image
.PHONY: build
build:
	@echo "---> build ${CONTAINER_IMAGE}"
	@docker build -t ${CONTAINER_IMAGE} $(BASE_DIR)/properly_thegraph_api
	@echo "		end"


# target: bootstrap - bootstrap service
.PHONY: bootstrap
bootstrap:
	@docker-compose \
		-p $(PROJECT) \
		-f bootstrap.yml \
		run --rm $(CONTAINER)


# target: shell - shell base python image
.PHONY: shell
shell:
ifeq ($(ENVIRONMENT),)
	@echo 'nothing to do  - use <ENVIRONMENT> '
else	
	@docker-compose \
		-p $(PROJECT) \
		-f run.yml \
		-f $(ENVIRONMENT)/run.yml \
		run --rm --service-ports $(CONTAINER) \
		/bin/bash
endif
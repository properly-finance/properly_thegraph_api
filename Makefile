COMMAND := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))

ifeq ($(BASE_DIR),)
	export BASE_DIR := $(shell pwd)/..
endif

# target: help - Display callable targets.
.PHONY: help
help: 
ifeq ($(findstring help,$(COMMAND)),help)
	@#
else
	@egrep "^# target:" [Mm]akefile
endif

dev:
	@#

build:
	@#
bootstrap:
	@#
shell:
	@#
test:
	@#


# target: compose (help) - Section for <compose> project
.PHONY: compose
compose: 
	@make -s -C ./compose $(COMMAND)

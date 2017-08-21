publish = $(foreach port,$(DRL_OPEN_PORTS),--publish $(port))
mount = $(foreach volume,$(DRL_MOUNTED_VOLUMES),-v $(volume))

.PHONY: build
build:
	docker build -t $(DRL_IMAGE_NAME) .


.PHONY: run
run: build rm
	$(DRL_NV_HEADER) nvidia-docker run --detach=true $(publish) $(mount) --name $(DRL_CONTAINER_NAME) --workdir=$(DRL_WORK_DIR) $(DRL_IMAGE_NAME)

.PHONY: exec
exec:
	nvidia-docker exec --interactive --tty $(DRL_CONTAINER_NAME) /bin/bash


.PHONY: stop
stop:
	-docker stop $(DRL_CONTAINER_NAME)


.PHONY: rm
rm: stop
	-docker rm $(DRL_CONTAINER_NAME)

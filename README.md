Welcome to Redis Ansible Role’s documentation!
==============================================

REDIS
-----

This role install redis as container and his monitoring on zabbix

### Requirements

Docker and Zabbix if you want monitoring

### Dependencies

-   Docker
-   Zabbix-server
-   Zabbix redis templates

### Example Playbook

    - hosts: servers
      roles:
        - { role: redis }

redis ansible role default variables
------------------------------------

#### Sections

-   Redis docker management
-   Redis monitoring management

### Redis docker management

`redis_docker_image`

Redis docker image

    redis_docker_image: redis

`redis_version`

Redis docker image version (TAG)

    redis_version: 3.2.9

`redis_docker_labels`

Yaml dictionary which maps Docker labels. os\_environment: Name of the
environment, example: Production, by default “default”.
os\_contianer\_type: Type of the container, by default redis.

    redis_docker_labels:
      os_environment: "{{ docker_os_environment | default('default') }}"
      os_contianer_type: redis

### Redis monitoring management

`redis_monitoring`

Enable or disable redis monitoring

    redis_monitoring: true

`redis_check_redisstatus`

Enable of disable redis status check, bu default True.

    redis_check_redisstatus: true

Changelog
---------

**Redis**

This project adheres to Semantic Versioning and human-readable
changelog.

### Redis master - unreleased

##### Added

-   First addition

##### Changed

-   First change

### Redis v0.0.1 - 2017/07/12

##### Added

-   Initial version

Copyright
---------

Redis

Copyright (C) DATE Raul Melo &lt;<raul.melo@opensolutions.cloud>&gt;

LICENSE

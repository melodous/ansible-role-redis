Welcome to Redis Ansible Role’s documentation!
==============================================

Role Name
---------

A brief description of the role goes here.

### Requirements

Any pre-requisites that may not be covered by Ansible itself or the role
should be mentioned here. For instance, if the role uses the EC2 module,
it may be a good idea to mention in this section that the boto package
is required.

### Dependencies

A list of other roles hosted on Galaxy should go here, plus any details
in regards to parameters that may need to be set for other roles, or
variables that are used from other roles.

### Example Playbook

Including an example of how to use your role (for instance, with
variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
        - { role: username.rolename, x: 42 }

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

### Redis v0.0.0 - DATE

##### Added

-   Initial version

Copyright
---------

Redis

Copyright (C) DATE User/Company &lt;<email@email.com>&gt;

LICENSE

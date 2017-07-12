
redis ansible role default variables
====================================

.. contents:: Sections
   :local:

Redis docker management
-----------------------

.. envvar:: redis_docker_image

Redis docker image
::

  redis_docker_image: redis



.. envvar:: redis_version

Redis docker image version (TAG)
::

  redis_version: 3.2.9


.. envvar:: redis_docker_labels

Yaml dictionary which maps Docker labels.
os_environment: Name of the environment, example: Production, by default "default".
os_contianer_type: Type of the container, by default redis.
::

  redis_docker_labels:
    os_environment: "{{ docker_os_environment | default('default') }}"
    os_contianer_type: redis





Redis monitoring management
---------------------------

.. envvar:: redis_monitoring

Enable or disable redis monitoring
::

  redis_monitoring: true



.. envvar:: redis_check_redisstatus

Enable of disable redis status check, bu default True.
::

  redis_check_redisstatus: true



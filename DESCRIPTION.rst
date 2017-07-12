REDIS
=====

This role install redis as container and his monitoring on zabbix

Requirements
------------

Docker and Zabbix if you want monitoring

Dependencies
------------

- Docker
- Zabbix-server
- Zabbix redis templates

Example Playbook
----------------

.. code::

  - hosts: servers
    roles:
      - { role: redis }

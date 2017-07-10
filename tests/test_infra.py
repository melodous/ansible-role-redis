def test_redis_server_running_and_enabled(Command, Service):
    # Check that docker service is running and enabled
    docker_service = Service("docker")
    assert docker_service.is_running
    assert docker_service.is_enabled
    # Check that redis service is running and enabled
    redis_service = Service("redis")
    assert redis_service.is_running
    assert redis_service.is_enabled

    # Check that redis-cli ping
    redis_output = Command.check_output("docker exec redis redis-cli ping")
    assert redis_output == "PONG"


def test_redis_start_stop(Command, Service):
    # Check init scripts are working
    Command.run_expect([0], "systemctl stop redis")
    redis_service = Service("redis")
    assert not redis_service.is_running
    Command.run_expect([0], "systemctl start redis")
    assert redis_service.is_running
    Command.run_expect([0], "systemctl restart redis")
    assert redis_service.is_running
    redis_output = Command.check_output("docker exec redis redis-cli ping")
    assert redis_output == "PONG"


def test_socket(Socket):
    # Check redis port is up and running
    assert Socket("tcp://0.0.0.0:6379").is_listening


def test_monitoring(Command):
    from zabbix_api import ZabbixAPI
    import datetime, time
    zbx = ZabbixAPI("http://172.28.128.3", timeout=10)
    zbx.login("Admin", "zabbix")
    zbx_host_list = get_host_by_host_name(zbx, "Redis")
    assert len(zbx_host_list) == 1
    zbx_host = zbx_host_list[0]['hostid']
    assert zbx_host == '10105'
    item = zbx.item.get(
        {
            "output": ["lastvalue"],
            "hostids": zbx_host,
            "search": {
                "key_": "net.tcp.port"
            },
            "startSearch": "true"
        }
    )
    assert  item[0]['lastvalue'] == '1'
    Command.run_expect([0], "docker stop redis")
    timeout = 60
    init = datetime.datetime.now()
    while True:
        item = zbx.item.get(
            {
                "output": ["lastvalue"],
                "hostids": zbx_host,
                "search": {
                    "key_": "net.tcp.port"
                },
                "startSearch": "true"
            }
        )
        if item[0]['lastvalue'] == '0':
            break
        diff = (datetime.datetime.now() - init).total_seconds()
        assert int(diff) < timeout
        time.sleep(5)
    Command.run_expect([0], "docker start redis")
    check_item(zbx, zbx_host, "net.tcp.port", '1', 60)


def check_item(zbx, host, key, value, timeout):
    import datetime, time
    init = datetime.datetime.now()
    while True:
        item = zbx.item.get(
                {
                    "output": ["lastvalue"],
                    "hostids": host,
                    "search": {
                        "key_": key
                    },
                    "startSearch": "true"
                }
            )
        if item[0]['lastvalue'] == value:
            break
        diff = (datetime.datetime.now() - init).total_seconds()
        assert int(diff) < timeout
        time.sleep(5)


def get_host_by_host_name(zbx, host_name):
    host_list = zbx.host.get(
            {
                'output': 'extend', 'filter': {'host': [host_name]}
            }
        )
    return host_list

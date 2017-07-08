import pytest

def test_redis_server_running_and_enabled(Command,Service):
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

def test_redis_start_stop(Command,Service):
  Command.run_expect([0],"systemctl stop redis")
  redis_service = Service("redis")
  assert not redis_service.is_running
  Command.run_expect([0],"systemctl start redis")
  assert redis_service.is_running
  Command.run_expect([0],"systemctl restart redis")
  assert redis_service.is_running
  redis_output = Command.check_output("docker exec redis redis-cli ping")
  assert redis_output == "PONG"

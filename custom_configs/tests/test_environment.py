from pytest import mark


@mark.skip
def test_environment_is_qa(env):
    assert env == "qa"


def test_environment_is_dev(env):
    assert env == "dev"


@mark.skip
def test_environment_is_qa_again(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://myqa-env.com"
    assert port == 80


def test_environment_is_dev_again(app_config):
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://mydev-env.com"
    assert port == 8080

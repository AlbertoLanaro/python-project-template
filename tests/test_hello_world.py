from python_project_template.utils import get_hello_world_str


def test_get_hello_world_string():
    assert get_hello_world_str() == "Hello World!"

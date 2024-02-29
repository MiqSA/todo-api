from services.todo.main import fetch_todos, ErrorTodosAPI
import pytest


def test_0_success_get_todos_defalt():
    response = fetch_todos()
    assert len(response) == 5
    assert isinstance(response, list)

def test_0_success_get_todos_limit():
    response = fetch_todos(limit=1)
    assert len(response) == 1
    assert isinstance(response, list)

def test_1_error_todos():
    with pytest.raises(ErrorTodosAPI) as excinfo:  
        fetch_todos(url="https://localhost1q2123323") 
    assert "Error in get todos" in str(excinfo.value)


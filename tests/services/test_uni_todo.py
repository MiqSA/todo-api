from services.todo.main import fetch_todos, ErrorTodosAPI
import pytest


def test_0_success_get_todos_defalt():
    response = fetch_todos()
    assert isinstance(response, dict)
    assert response['status_code'] == 200

def test_1_error_todos():
    with pytest.raises(ErrorTodosAPI) as excinfo:  
        fetch_todos(url="https://localhost1q2123323") 
    assert "Error in get todos" in str(excinfo.value)


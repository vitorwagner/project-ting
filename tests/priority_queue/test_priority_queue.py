from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    first_insert = {'qtd_linhas': 9}
    second_insert = {'qtd_linhas': 4}
    third_insert = {'qtd_linhas': 2}
    fourth_insert = {'qtd_linhas': 5}
    fifth_insert = {'qtd_linhas': 7}
    sixth_insert = {'qtd_linhas': 11}
    seventh_insert = {'qtd_linhas': 3}

    priority_queue.enqueue(first_insert)
    priority_queue.enqueue(second_insert)
    priority_queue.enqueue(third_insert)
    priority_queue.enqueue(fourth_insert)
    priority_queue.enqueue(fifth_insert)
    priority_queue.enqueue(sixth_insert)
    priority_queue.enqueue(seventh_insert)
    assert len(priority_queue) == 7

    assert priority_queue.search(0) == second_insert
    assert priority_queue.search(1) == third_insert
    assert priority_queue.search(2) == seventh_insert
    assert priority_queue.search(3) == first_insert
    assert priority_queue.search(4) == fourth_insert
    assert priority_queue.search(5) == fifth_insert
    assert priority_queue.search(6) == sixth_insert

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(-7)
    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(777)

    assert priority_queue.dequeue() == second_insert
    assert priority_queue.dequeue() == third_insert
    assert priority_queue.dequeue() == seventh_insert
    assert priority_queue.dequeue() == first_insert
    assert priority_queue.dequeue() == fourth_insert
    assert priority_queue.dequeue() == fifth_insert
    assert priority_queue.dequeue() == sixth_insert
    assert len(priority_queue) == 0

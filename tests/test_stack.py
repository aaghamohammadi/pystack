import pytest

from pystack.stack import Stack


@pytest.mark.smoke
class StackTest:
    def setup_method(self):
        self.st = Stack()

    @pytest.mark.ex
    def test_stack_is_empty(self):
        assert self.st.is_empty()
        assert len(self.st) == 0
        assert repr(self.st) == "Stack()"
        assert str(self.st) == "Stack()"
        with pytest.raises(IndexError):
            self.st.pop()

    def test_push_one_item(self):
        self.st.push(2)
        assert not self.st.is_empty()
        assert len(self.st) == 1
        assert self.st.top() == 2
        assert repr(self.st) == "Stack()"
        assert str(self.st) == "Stack(2)"

    def test_push_multiple_items(self):
        self.st.push(5)
        self.st.push(3)
        self.st.push(7)
        assert len(self.st) == 3
        assert self.st.top() == 7
        assert str(self.st) == "Stack(5, 3, 7)"

    @pytest.mark.ex
    @pytest.mark.slow
    def test_push_multiple_items_until_exception_raises(self):
        for i in range(1_000_000):
            self.st.push(i)
        assert self.st.is_full()
        with pytest.raises(OverflowError):
            self.st.push(23)

    def test_pop_one_item(self):
        self.st.push(5)
        top = self.st.pop()
        assert top == 5
        assert self.st.is_empty()
        assert len(self.st) == 0

    @pytest.mark.ex
    def test_pop_multiple_items(self):
        self.st.push(3)
        self.st.push(7)
        assert self.st.pop() == 7
        assert self.st.pop() == 3
        with pytest.raises(IndexError):
            self.st.pop()

    @pytest.mark.ex
    def test_push_non_integer_items(self):
        with pytest.raises(TypeError):
            self.st.push("3")
        with pytest.raises(TypeError):
            self.st.push(3.1)
        with pytest.raises(TypeError):
            self.st.push(True)

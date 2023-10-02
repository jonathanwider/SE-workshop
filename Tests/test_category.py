import pytest
from question import Question
from category import Category

class Test_Category(object):
    def test_add_question(self):
        mock_category = Category(title="Mock")
        mock_question = Question(title="Is this a question?", answer="Yes it is.")
        mock_category.add_question(mock_question)
        assert mock_question in mock_category.questions
from team import Team
from question import Question
from category import Category

class Test_Team(object):
    def test_won_question(self):
        mock_category = Category(title="Mock")
        mock_question = Question(title="Is this a question?", answer="Yes it is.")
        mock_team = Team(name="Test")
        mock_team.won_question(mock_question)
        assert mock_team.points == 1

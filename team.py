from question import Question
class Team(object):
    def __init__(self, name: str):
        """

        :param name: The name of the team
        """
        self.name = name
        self._correct_questions: set(Question) = set()

    def won_question(self, question: Question):
        """
        Add the question the questions won by the team
        :param question: the question that was won by the team
        :return:
        """
        self._correct_questions.add(question)

    @property
    def points(self) -> int:
        """

        :return: number of questions won by team
        """
        return len(self._correct_questions)
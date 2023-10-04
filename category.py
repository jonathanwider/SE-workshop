from question import Question
class Category(object):
    def __init__(self, title: str, questions: [Question] = None):
        """

        :param title: The category's title (e.g. sports)
        :param questions: The questions of the category, optional for init, can be added later with :func:`add_question <category.Category.add_question>`
        """
        if questions == None:
            questions = []
        self.title = title
        self.questions = questions
        self._currentQuestion = 0

    def add_question(self, question: Question):
        """
        Adds the question to the category
        :param question: the question to add
        :return:
        """
        self.questions.append(question)

    def add_questions(self, questions: [Question]):
        self.questions.extend(questions)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and getattr(other, 'title') == self.title and getattr(other, 'questions') == self.questions

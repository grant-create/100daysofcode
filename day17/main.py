from data import question_data as data
from quiz_game import Question
from quiz_brain import Quiz_Brain

question_bank = []
for q in data:
    new_q = Question(q['text'], q['answer'])
    question_bank.append(new_q)

quiz = Quiz_Brain(question_bank)

while quiz.still_has_questions():   
    quiz.next_question()
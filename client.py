from game import Game
from game_result import GameResult
from game_status import GameStatus


def end_of_game_handler(result: GameResult):
    print(f"Заданно вопросов: {result.question_passed}. Допущенные ошибки: {result.mistakes_made}")
    print(f"Вы выйграли!" if result.won else "Вы проиграли!")


game = Game("Questions.csv", end_of_game_handler, allowed_mistakes=2)

while game.game_status == GameStatus.IN_PROGRESS:
    q = game.get_next_questions()
    print(f"Вернно ли следующие утреврждение? Введите 'д' или 'н' \n{q.text}")

    answer = input()
    is_answer = answer == "д"

    if answer != "д" and answer != "н":
        print("Некоректный ввод ответа, Введите 'y' или 'n'")
        continue

    if q.is_true == is_answer:
        print("Хорошая работа! Вы правы!")
    else:
        print("Упс, вообще-то вы ошиблись. Вот вам обьяснение:")
        print(q.explanation)

    game.give_answer(is_answer)

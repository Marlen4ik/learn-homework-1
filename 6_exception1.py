"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она
  перехватывала KeyboardInterrupt, писала пользователю "Пока!"
  и завершала работу при помощи оператора break

"""

questions_and_answers: dict[str, str] = {
    "Как дела?": "Хорошо!",
    "Что делаешь?": "Программирую",
}


def hello_user(answers_dict: dict):
    while True:
        try:
            if (text := input()) in answers_dict:
                print(answers_dict[text])
        except KeyboardInterrupt:
            print("Пока!")
            break


if __name__ == "__main__":
    hello_user(questions_and_answers)

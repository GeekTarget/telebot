import sqlite3


class DateBase:
    message = ''  # to send a message

    def __init__(self, base_name):
        """Инициализация базы данных"""
        self.db = sqlite3.connect(base_name)
        self.sql = self.db.cursor()

    # Позволяет подписаться на рассылку
    def subscribe(self, user, sub):
        with self.db:
            self.sql.execute(f'SELECT username FROM subscribes WHERE  username = "{user}"')
            if self.sql.fetchone() is None:  # Проверяет есть ли user в бд
                self.sql.execute(f"INSERT INTO subscribes VALUES(?,?)", (user, sub))  # если нет, то заносит данные
                self.db.commit()
                self.message = 'Вы успешно подписались на рассылку!'
                return
            else:
                self.sql.execute(f'SELECT subscribe FROM subscribes WHERE username = "{user}"')
                if sub in self.sql.fetchone()[0]:  # Проверяет не совпадает ли нынешняя подписка
                    self.message = 'У вас уже есть такая активная подписка!'
                    return  # с прошлой
                else:
                    self.sql.execute(f'SELECT subscribe FROM subscribes WHERE username = "{user}"')
                    text = self.sql.fetchone()[0] + ', ' + sub
                    self.sql.execute(f'UPDATE subscribes SET subscribe = "{text}" WHERE username = "{user}"')
                    self.db.commit()
                    self.message = 'Вы успешно подписались на рассылку!'
                    return

    # Позволяет отписаться от рассылки
    def unsubscribe(self, user, sub):
        with self.db:
            self.sql.execute(f'SELECT username FROM subscribes WHERE username = "{user}"')
            if self.sql.fetchone() is None:  # Проверяет, есть ли user в бд, если нет то ничего не делает
                self.message = 'У вас нет активных подписок!'
                return
            else:
                self.sql.execute(f'SELECT subscribe FROM subscribes WHERE username = "{user}"')
                if sub not in self.sql.fetchone()[0]:  # Проверяет есть ли нышешняя подписка в активных
                    self.message = 'У вас нет такой активной подписки!'
                    return
                else:
                    self.sql.execute(f'SELECT  subscribe FROM subscribes WHERE username = "{user}"')
                    subs = self.sql.fetchone()[0].split(', ')
                    if len(subs) != 1:  # Проверяет, сколько активных подписок у user
                        subs.pop(subs.index(sub))  # если больше 1, то убирает только одну подписку
                        text = ', '.join(subs)
                        self.sql.execute(f'UPDATE subscribes SET subscribe = "{text}" WHERE username = "{user}"')
                        self.message = 'Вы отписались от рассылки ' + sub
                        self.db.commit()
                        return
                    else:
                        self.sql.execute(f'DELETE FROM subscribes WHERE username = "{user}"')
                        self.message = 'Вы отписались от рассылки ' + sub  # Если активная подписка одна,
                        self.db.commit()  # то удаляет все данные user
                        return

    def show_subs(self, user):
        with self.db:
            self.sql.execute(f'SELECT subscribe FROM subscribes WHERE username = "{user}"')
            if self.sql.fetchone() is None:
                self.message = 'У вас нет активных подписок!'
                return
            else:
                self.sql.execute(f'SELECT subscribe FROM subscribes WHERE username = "{user}"')
                return self.sql.fetchone()[0]

    def show_subscribers(self):
        with self.db:
            self.sql.execute(f'SELECT username FROM subscribes')
            return self.sql.fetchall()

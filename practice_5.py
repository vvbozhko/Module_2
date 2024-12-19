import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = int(hash(password))
        self.age = age

    def __hash__(password):
        return hash(password)

    def __str__(self):
        return f"{self.nickname}"

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        # hashed_password = int(hash(password))
        for user in self.users:
            if user.nickname == nickname and user.password == int(hash(password)):
                self.current_user = user
                print(f"Пользователь {nickname} вошел.")
                return
        print("Неправильный логин или пароль.")

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует.")
                return
        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        # print(f"Пользователь {nickname} зарегистрирован и вошел.")

    def log_out(self):
        self.current_user = None
        print("Пользователь вышел.")

    def add(self, *videos):
        for video in videos:
            if not any(i.title == video.title for i in self.videos):
                self.videos.append(video)
            else:
                print(f"Видео {video.title} уже есть.")

    def get_videos(self, search_word):
        search_word = search_word.lower()
        return [video.title for video in self.videos if search_word in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode == True and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return

                print(f"Смотрим '{video.title}' с {video.time_now} секунды.")
                a = ""
                while video.time_now < video.duration:
                    time.sleep(0.3)
                    video.time_now += 1
                    a = str(a) + str(video.time_now)
                print(f'{str(a)} Конец видео.')
                #     print(f'{video.time_now}') # для вывода в столбик
                # print("Конец видео")

                video.time_now = 0
                return
        print("Видео не найдено.")


# Код для проверки
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
# ur.log_in('vasya_pupkin', 'Lolkekcheburek')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')



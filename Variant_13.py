# Импорт из модуля
from tkinter import *
from datetime import datetime
import time


# Настройки
def setting():
    # Окно настроек
    root = Tk()
    root.title('НАСТРОЙКИ')

    width = 600
    height = 600
    result = None

    # Изображение шестеренки
    img_Setting = PhotoImage(file="3.3.png")

    img_small_setting = img_Setting.subsample(5, 5)

    label = Label(root, image=img_small_setting)
    label.place(relx=0.05, y=height - 568, anchor="center")

    # Настройки окна
    root.geometry(f"{width}x{height}")
    root.resizable(width=False, height=False)
    root.config(bg='gold')

    # Заголовок
    title_label = Label(
        root,
        text="Введите размеры окна",
        font=("Arial", 26, "bold"),
        bg='white'
    )
    title_label.pack()

    # Подпись ширина
    width_label = Label(
        root,
        text="Ширина:",
        font=("Arial", 20, "bold"),
        bg='gold'
    )
    width_label.place(x=140, y=120)

    # Поле ввода ширины
    width_entry = Entry(
        root,
        font=("Arial", 25, "bold italic"),
        width=7
    )
    width_entry.place(x=300, y=120)

    # Подпись высота
    height_label = Label(
        root,
        text="Высота:",
        font=("Arial", 20, "bold"),
        bg='gold'
    )
    height_label.place(x=140, y=200)

    # Поле ввода высоты
    height_entry = Entry(
        root,
        font=("Arial", 25, "bold italic"),
        width=7
    )
    height_entry.place(x=300, y=200)

    # Кнопка подтверждения и проверка
    def apply_size():
        nonlocal result

        w = width_entry.get()
        h = height_entry.get()

        if w.isdigit() and h.isdigit():
            w = int(w)
            h = int(h)

            if 510 < w < 1900 and 330 < h < 1000:
                result = (w, h)
                root.destroy()
            # Размер не в диапазоне
            else:
                Wrong_label_1 = Label(
                    root,
                    text="Размер не в диапазоне!",
                    font=("Comic Sans MS", 20, "bold"),
                    fg="red",
                    bg='gold',
                    width = 20,
                    height = 1
                )
                Wrong_label_1.place(relx=0.5, y=400, anchor="center")
                Wrong_label_2 = Label(
                    root,
                    text="510 < ширина < 1900",
                    font=("Comic Sans MS", 20, "bold"),
                    fg="red",
                    bg='gold',
                    width=20,
                    height=1
                )
                Wrong_label_2.place(relx=0.5, y=450, anchor="center")
                Wrong_label_3 = Label(
                    root,
                    text="330 < высота < 1000",
                    font=("Comic Sans MS", 20, "bold"),
                    fg="red",
                    bg='gold',
                    width=20,
                    height=1
                )
                Wrong_label_3.place(relx=0.5, y=500, anchor="center")

        # Введите числа
        else:
            Empty_label = Label(
                root,
                text="Введите числа!",
                font=("Comic Sans MS", 20, "bold"),
                fg="red",
                bg='gold',
                width = 20,
                height = 1
            )
            Empty_label.place(relx=0.5, y=400, anchor="center")

    # Кнопка подтверждения
    apply_btn = Button(
        root,
        text="Применить",
        font=("Comic Sans MS", 18, "bold"),
        bg='violet',
        activebackground='light green',
        command=apply_size
    )
    apply_btn.place(relx=0.5, y=300, anchor="center")

    # Запуск работы этого окна
    root.mainloop()
    return result


# Функция секундомера
def stopwatch(width, height):
    global temp, after_id

    temp = 0
    after_id = ''

    # Создание окна с секундами
    def tick():
        global temp, after_id

        after_id = root.after(1000, tick)
        f_temp = datetime.fromtimestamp(temp).strftime('%M:%S')
        label.config(text=f_temp)
        temp += 1

    # Старт
    def start_tick():
        btnStart.place_forget()
        btnStop.place(relx=0.5, y=height - 60, anchor="center")
        tick()

    # Стоп
    def stop_tick():
        btnStop.place_forget()
        btnContinue.place(x=width // 2 - 250, y=height - 92)
        btnReset.place(x=width // 2 - 3, y=height - 92)
        root.after_cancel(after_id)

    # Продолжить
    def continue_tock():
        btnContinue.place_forget()
        btnReset.place_forget()
        btnStop.place(relx=0.5, y=height - 60, anchor="center")
        tick()

    # Сброс
    def reset_click():
        global temp

        temp = 0
        label.configure(text='00:00')
        btnContinue.place_forget()
        btnReset.place_forget()
        btnStart.place(relx=0.5, y=height - 60, anchor="center")

    # Окно секундомер
    root = Tk()
    root.title('СЕКУНДОМЕР')

    # Настройки окна
    root.geometry(f"{width}x{height}")
    root.resizable(width=False, height=False)
    root.config(bg='pink')

    # Лейбл с секундами
    label = Label(root,
                  width=6,
                  font=("Comic Sans MS", 40, "bold"),
                  text='00:00')
    label.pack()

    # Кнопка старт
    btnStart = Button(
        root,
        text='СТАРТ',
        font=("Comic Sans MS", 20, "bold italic"),
        command=start_tick,
        bg='violet',
        activebackground="light green",
        width=14,
        height=1
    )

    # Кнопка стоп
    btnStop = Button(
        root,
        text='СТОП',
        font=("Comic Sans MS", 20, "bold italic"),
        command=stop_tick,
        bg='violet',
        activebackground="firebrick1",
        width=14,
        height=1
    )

    # Кнопка продолжить
    btnContinue = Button(
        root,
        text='ПРОДОЛЖИТЬ',
        font=("Comic Sans MS", 20, "bold italic"),
        command=continue_tock,
        bg='violet',
        activebackground="light yellow",
        width=14,
        height=1
    )

    # Кнопка сброс
    btnReset = Button(
        root,
        text='СБРОС',
        font=("Comic Sans MS", 20, "bold italic"),
        command=reset_click,
        bg='violet',
        activebackground="darkred",
        width=14,
        height=1
    )

    btnStart.place(relx=0.5, y=height - 60, anchor="center")

    root.mainloop()


# Функция таймера
def timer(width, height):
    warning_label = None
    stop_flag = False

    # Стоп
    def stop():
        nonlocal stop_flag

        stop_flag = True
        btnStop.place_forget()
        btnStart.place(relx=0.5, y=height - 60, anchor="center")
        count_digit.config(text='00:00')
        second.delete(0, END)

    # Звук
    def sound():
        btnStop.place_forget()
        btnStart.place(relx=0.5, y=height - 60, anchor="center")
        root.bell()
        count_digit.config(text='00:00')
        second.delete(0, END)

    # Старт
    def start():
        nonlocal stop_flag, warning_label

        stop_flag = False

        value = second.get()

        # Проверка на положительное число
        if not value.isdigit() or int(value) <= 0:

            if warning_label is None:
                warning_label = Label(
                    root,
                    text="Введите положительное число!",
                    font=("Comic Sans MS", 20, "bold"),
                    fg="red",
                    bg="light blue"
                )
                warning_label.place(relx=0.5, y=160, anchor="center")

            return

        if warning_label is not None:
            warning_label.destroy()
            warning_label = None

        # Преобразуем в число
        duration = int(value)

        btnStart.place_forget()
        btnStop.place(relx=0.5, y=height - 60, anchor="center")

        # Цикл таймера
        while duration and not stop_flag:
            m, s = divmod(duration, 60)
            count_digit['text'] = f"{m:02d}:{s:02d}"
            root.update()
            time.sleep(1)
            duration -= 1

        # Подключаем звук
        if duration == 0 and not stop_flag:
            sound()

    # Окно таймер
    root = Tk()
    root.title('ТАЙМЕР')

    # Настройка окна
    root.geometry(f"{width}x{height}")
    root.resizable(width=False, height=False)
    root.config(bg='light blue')

    # Лейбл с секундами
    count_digit = Label(
        root,
        width=6,
        font=("Comic Sans MS", 40, "bold"),
        text='0'
    )
    count_digit.pack()

    # Ввод секунд
    second = Entry(
        root,
        font=("Comic Sans MS", 30, "bold italic"),
        width=7
    )
    second.place(relx=0.5, y=120, anchor="center")

    # Старт
    btnStart = Button(
        root,
        text='СТАРТ',
        font=("Comic Sans MS", 20, "bold italic"),
        command=start,
        bg='light goldenrod yellow',
        activebackground="light green",
        width=14,
        height=1
    )

    # Стоп
    btnStop = Button(
        root,
        text='СТОП',
        font=("Comic Sans MS", 20, "bold italic"),
        command=stop,
        bg='violet',
        activebackground="firebrick1",
        width=14,
        height=1
    )

    btnStart.place(relx=0.5, y=height - 60, anchor="center")

    root.mainloop()


# Окно меню
root = Tk()
root.title('МЕНЮ')

width = 600
height = 600

# Изображение таймера
img_timer = PhotoImage(file="1.1.png")

img_small_timer = img_timer.subsample(2, 2)

label = Label(root, image=img_small_timer)
label.place(relx=0.29, y=height - 250, anchor="center")

# Изображение секундомера
img_Stopwatch = PhotoImage(file="2.2.png")

img_small_stopwatch = img_Stopwatch.subsample(2, 2)

label = Label(root, image=img_small_stopwatch)
label.place(relx=0.7, y=height - 250, anchor="center")

# Настройка окна
root.geometry(f"{width}x{height}")
root.resizable(width=False, height=False)
root.config(bg='white')

# Лейбл с меню
count_digit = Label(
    root, width=6, font=("Arial", 40, "bold"), text='МЕНЮ'
)
count_digit.pack()


# Запуск таймера
def timer_1():
    root.destroy()
    res = setting()
    w, h = res
    timer(w, h)


# Запуск секундомера
def stopwatch_2():
    root.destroy()
    res = setting()
    w, h = res
    stopwatch(w, h)


# Кнопка 1 - таймер
btn1 = Button(
    root,
    text='1 - таймер',
    font=("Comic Sans MS", 20, "bold italic"),
    command=timer_1,
    bg='orange',
    activebackground="light blue",
    width=14,
    height=1
)

# Кнопка 2 - секундомер
btn2 = Button(
    root,
    text='2 - секундомер',
    font=("Comic Sans MS", 20, "bold italic"),
    command=stopwatch_2,
    bg='orange',
    activebackground="pink",
    width=14,
    height=1
)

btn1.place(x=width // 2 - 250, y=height - 92)
btn2.place(x=width // 2 - 3, y=height - 92)

root.mainloop()

# the json module to work with json files 
import json
import tkinter
from tkinter import *
import random

block= [
    "Социально-психологические навыки",  
    "Социально-адаптационные навыки",  
    "Правовая грамотность",  
    "Финансовая грамотность",  
    "Профессиональна-трудовая ориентаци",  
    "Навыки ЗОЖ",  
    "Социально-бытовые навыки"
]

questions = [
    ["Испытываете ли Вы трудности, чтобы заговорить с кем-нибудь", "Я со всеми соревнуюсь, стараюсь быть первым во всем"],
    ["В каких жизненных ситуациях Вы бы обратились в Многофункциональный центр (МФЦ) предоставления государственных и муниципальных услуг? (можно выбрать несколько вариантов ответа)","В каких жизненных ситуациях гражданам помогут в отделении Пенсионного фонда России (ПФР)? (можно выбрать несколько вариантов ответа)"],
    ["Как Вы оцениваете свой уровень правовой грамотности?","Куда нужно обратиться при нарушении Ваших прав?"],
    ["Какие из перечисленных ниже активов семьи являются инвестиционными? (правильные несколько вариантов ответа","В настоящий момент ставка налога на заработную плату физических лиц в РФ составляе"],
    ["Когда я думаю о необходимости работать, мне становится тревожно","Я не знаю, кем хочу работать"],
    ["Как Вы понимаете здоровый образ жизни?","Что такое личная гигиена?"],
    ["Сколько раз в день надо мыть руки?","Сколько раз в день надо очищать кожу лица?"]
]

answers_choice = [
    [
        ["Да, со всеми", "Да, если человек мне незнаком", "В зависимости от темы разговора", "Нет, если четко понимаю, о чем хочу поговорить", "Нет, как правило, не испытываю", "Нет, не испытываю никогда"],
        ["Да, это про меня", "Да, это мне свойственно очень часто", "Скорее это похоже на меня", "Скорее это не про меня", "Нет, чаще это не про меня", "Нет, это точно не про меня"]
    ],
    [
        ["Утрата документов", "Смена фамилии и имени", "Открытие свое дело", "Регистрация брака", "Смена места жительства", "Оформление ипотеки", "Оформление мер социальной поддержки", "Оплата коммунальных услуг", "Смерть близкого человека", "Во всех вышеуказанных ситуациях"],
        [ "При выходе на пенсии", "При оформлении средств материнского капитала при рождении детей", "При оформлении некоторых социальных пособий", "При утере СНИЛСа", "При поиске работы", "При оформлении электронной трудовой книжки", "При открытии собственного дела", "Во всех вышеуказанных ситуациях"]
    ],
    [
        [ "У меня хороший уровень знаний", "У меня средний уровень знаний", "У меня низкий уровень знаний"],
        [ "В полицию", "К педагогам", "К друзьям", "В суд", "Затрудняюсь ответить"]
    ],
    [
        [ "Квартира, сдаваемая в аренду", "Квартира, в которой живет семья", "Банковские депозиты", "Ценные бумаги", "Автомобиль", "Затрудняюсь ответить"],
        [ "5 %", "10 %", "13 %", "15 %", "20 %"]
    ],
    [
        [ "Да, это про меня", "Да, это мне свойственно очень часто", "Скорее это похоже на меня", "Скорее это не про меня", "Нет, чаще это не про меня", "Нет, это точно не про меня"],
        [ "Да, это про меня", "Да, это мне свойственно очень часто", "Скорее это похоже на меня", "Скорее это не про меня", "Нет, чаще это не про меня", "Нет, это точно не про меня"]
    ],
    [
        [ "Целый комплекс мер по укреплению и сохранению здоровья", "Занятия физическими упражнениями", "Отсутствие вредных привычек"],
        [ "Совокупность правил, выполнение которых способствует сохранению и укреплению здоровья", "Правила ухода за телом", "Уход за одеждой"]
    ],
    [
        [ "Утром", "По мере необходимости", "Каждый раз перед едой", "Утром и вечером"],
        [ "Утром и вечером", "Утром", "Вечером", "По мере необходимости"]
    ]
 ] 

answers = [
    [
        [5,4,3,2,1,0],    
        [5,4,3,2,1,0],
    ],    
    [
        [0,0,0,5,0,5,0,5,0,3],    
        [0,0,0,0,5,5,0,3],
    ],    
    [
        [1,3,5],    
        [0,3,5,3,5],
    ],    
    [
        [0,5,0,0,5,5],    
        [5,5,0,5,5],
    ],   
    [
        [5,4,3,2,1,0],    
        [5,4,3,2,1,0],
    ],   
    [
        [0,3,3],    
        [0,3,3],
    ],   
    [
        [5,0,5,5],    
        [0,5,5,5],
    ]    
    
    
] 

user_answer = [
    [],
    [],
    [],
    [],
    [],
    [],
    []
    ]
indexes = 0
blockIndexes = 0
rarr = []

class GradientFrame(tkinter.Canvas):
    '''A gradient frame which uses a canvas to draw the background'''
    def __init__(self, parent, color1="green", color2="red", **kwargs):
        tkinter.Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event=None):
        '''Draw the gradient'''
        self.delete("gradient")
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags=("gradient",), fill=color)
        self.lower("gradient")


#def showresult():
#    destroyQuiz()
#    i = 0
 #   for el in block:
 #       labelresulttext = Label(
  #          root,
   #         text = block[i],
    #        font = ("Times",18),
     #       background = "#ffffff",
 #       )
  #      labelresulttext.pack(pady=(5,5))
    #    gradient = Canvas(root, width=255 * 2, height=25)
   #     gradient.pack()
     #   for x in range(0, 256):
      #      r = x*2 if x < 128 else 255
       #     g = 255 if x < 128 else 255 - (x-128)*2
        #    gradient.create_rectangle(x*2, 0, x*2 + 2, 50, fill=rgb(r, g, 0), outline=rgb(r, g, 0))
       # i += 1
def showresult():
    destroyQuiz()
    i = 0
    for el in block:
        labelresulttext = Label(
            root,
            text = block[i],
            font = ("Times",18),
            background = "#ffffff",
        )
        labelresulttext.pack(pady=(5,5))
        gradient = GradientFrame(root, width=255 * 2, height=25)
        gradient.pack()
        i += 1

def rgb(r, g, b):
   return "#%s%s%s" % tuple([hex(c)[2:].rjust(2, "0")
      for c in (r, g, b)])

def destroyQuiz():
    global rarr
    global lblBlock
    global lblQuestion
    lblQuestion.destroy()
    lblBlock.destroy()
    for ri in rarr:
        ri.destroy()

ques = 1
def selected():
    global radiovar,user_answer,answers,r,rarr, blockIndexes, indexes
    global lblBlock
    global lblQuestion
    global ques
    x = radiovar.get()
    ball = answers[blockIndexes][indexes][x]
    user_answer[blockIndexes].append(ball)
    print(user_answer)
    radiovar.set(-1)
    if indexes < (len(questions[blockIndexes]) - 1):
        destroyQuiz()
        indexes += 1
        startquiz()
    elif blockIndexes < (len(block) - 1):
        destroyQuiz()
        blockIndexes += 1
        indexes = 0
        startquiz()
    else:
        showresult()
    

def startquiz():
    global lblBlock,lblQuestion, r,rarr, blockIndexes, indexes
    lblBlock = Label(
        root,
        text = block[blockIndexes],
        font = ("Times", 12),
        width = 400,
        anchor = 'w',
        wraplength = 500,
        background = "#ffffff",
    )
    lblBlock.pack(pady=(5,5))

    lblQuestion = Label(
        root,
        text = questions[blockIndexes][indexes],
        font = ("Times", 16),
        width = 500,
        justify = "center",
        wraplength = 500,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(50,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    i = 0
    for choise in answers_choice[blockIndexes][indexes]:
        r = Radiobutton(
            root,
            text = answers_choice[blockIndexes][indexes][i],
            font = ("Times", 12),
            value = i,
            variable = radiovar,
            command = selected,
            anchor = 'w',
            background = "#ffffff",
        )
        r.pack(pady=5)
        rarr.append(r)
        i +=1


def startIspressed():
    labeltext.destroy()
    lblInstruction.destroy()
    lblRules.destroy()
    btnStart.destroy()
    startquiz()



root = tkinter.Tk()
root.title("Тест на оценку нуждаемости в социальном сопровождении")
root.geometry("700x600")
root.config(background="#ffffff")
root.resizable(0,0)

labeltext = Label(
    root,
    text = "\nТест на оценку нуждаемости \nв социальном сопровождении",
    font = ("Times",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0,50))


btnStart = Button(
    root,
    text = "Начать",
    font = ("Times",24,"bold"),
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack()

lblInstruction = Label(
    root,
    text = "Прочтите правила и нажмите \"Начать\"",
    background = "#ffffff",
    font = ("Times",14),
    justify = "center",
)
lblInstruction.pack(pady=(10,100))

lblRules = Label(
    root,
    text = "В данном тесте несколько блоков: \n- Социально-психологические навыки\n- Социально-адаптационные навыки\n- Правовая грамотность\n- Финансовая грамотность\n- Профессиональна-трудовая ориентация\n- Навыки ЗОЖ \n- Социально-бытовые навыки",
    width = 100,
    font = ("Times",14),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRules.pack()

root.mainloop()
from random import choice

import requests
from vk_api import VkApi, VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from json import dumps
import datetime as dt
from docxtpl import DocxTemplate


vk_session = VkApi(token="3f8043434961a0c2f39d869734c128cf773b1f65c7e80ffebd9661210aa4534d569c97a15656edd970f2e", api_version=5.95)
longpoll = VkLongPoll(vk_session)
upload = VkUpload(vk_session)
session_api = vk_session.get_api()
question = False
upload = VkUpload(vk_session)
raspisanie = {
	'1': {'а': {'понедельник': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
		     'вторник': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
			 'среда': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
             'четверг': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
		     'пятница': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
             'суббота': ['выходной'],
             'воскресенье': ['выходной'],
                 },
            'б': {'понедельник': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
		     'вторник': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
			 'среда': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
             'четверг': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
		     'пятница': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
             'суббота': ['выходной'],
             'воскресенье': ['выходной'],
                 }
		  },
	'2': { "а":{ 'понедельник': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
		     'вторник': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
			 'среда': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
             'четверг': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
		     'пятница': ['1. чтение','2. математика','3. русский язык','4. окружающий мир'],
             'суббота': ['выходной'],
             'воскресенье': ['выходной'],
                 }
           },
	'3': { "а":{ 'понедельник': ['1. математика','2. окружающий мир','3. чтение','4. физкультура'],
		     'вторник': ['1. математика','2. окружающий мир','3. чтение','4. физкультура'],
			 'среда': ['1. математика','2. окружающий мир','3. чтение','4. физкультура'],
             'четверг': ['1. математика','2. окружающий мир','3. чтение','4. физкультура'],
		     'пятница': ['1. математика','2. окружающий мир','3. чтение','4. физкультура'],
             'суббота': ['выходной'],
             'воскресенье': ['выходной'],
                 }
           },
	'4': { "а":{ 'понедельник': ['1. английский язык','2. математика','3. музыка','4. окружающий мир', '5. русский язык'],
		     'вторник': ['1. английский язык','2. математика','3. музыка','4. окружающий мир', '5. русский язык'],
			 'среда': ['1. английский язык','2. математика','3. музыка','4. окружающий мир', '5. русский язык'],
             'четверг': ['1. английский язык','2. математика','3. музыка','4. окружающий мир', '5. русский язык'],
		     'пятница': ['1. английский язык','2. математика','3. музыка','4. окружающий мир', '5. русский язык'],
             'суббота': ['выходной'],
             'воскресенье': ['выходной'],
                 }
           },
	'5': { "а":{ 'понедельник': ['1. литература','2. физкультура','3. история','4. биология', '5. русский язык'],
		     'вторник': ['1. литература','2. физкультура','3. математика','4. биология', '5. русский язык'],
			 'среда': ['1. литература','2. физкультура','3. математика','4. биология', '5. русский язык'],
             'четверг': ['1. литература','2. физкультура','3. математика','4. биология', '5. русский язык'],
		     'пятница': ['1. литература','2. физкультура','3. математика','4. биология', '5. русский язык'],
             'суббота': ['выходной'],
             'воскресенье': ['выходной'],
                 }
           },
    '6': { "а":{ 'понедельник': ['1. обществознание','2. русский язык','3. история','4. биология', '5. музыка'],
		     'вторник': ['1. обществознание','2. русский язык','3. история','4. биология', '5. музыка'],
			 'среда': ['1. обществознание','2. русский язык','3. история','4. биология', '5. музыка'],
             'четверг': ['1. обществознание','2. русский язык','3. история','4. биология', '5. музыка'],
		     'пятница': ['1. обществознание','2. русский язык','3. история','4. биология', '5. музыка'],
             'суббота': ['выходной'],
             'воскресенье': ['выходной'],
                 }
           },
    '7': { "а":{ 'понедельник': ['1. обществознание','2. музыка','3. история','4. биология', '5. геометрия'],
		     'вторник': ['1. обществознание','2. музыка','3. история','4. биология', '5. геометрия'],
			 'среда': ['1. обществознание','2. музыка','3. история','4. биология', '5. геометрия'],
             'четверг': ['1. обществознание','2. музыка','3. история','4. биология', '5. геометрия'],
		     'пятница': ['1. обществознание','2. музыка','3. история','4. биология', '5. геометрия'],
             'суббота': ['выходной'],
             'воскресенье': ['выходной'],
                 }
           },
    '8': { "а":{ 'понедельник':  ['1. геометрия','2. русский язык','3. химия','4. биология', '5. алгебра'],
		     'вторник': ['1. геометрия','2. русский язык','3. химия','4. биология', '5. алгебра'],
			 'среда': ['1. геометрия','2. русский язык','3. химия','4. биология', '5. алгебра'],
             'четверг': ['1. геометрия','2. русский язык','3. химия','4. биология', '5. алгебра'],
		     'пятница': ['1. геометрия','2. русский язык','3. химия','4. биология', '5. алгебра'],
             'суббота': ['выходной'],
             'воскресенье': ['выходной'],
                 }
           },
    '9': { "а":{ 'понедельник':  ['1. обществознание','2. алгебра','3. химия','4. биология', '5. физкультура'],
		     'вторник': ['1. обществознание','2. алгебра','3. химия','4. биология', '5. физкультура'],
			 'среда': ['1. обществознание','2. алгебра','3. химия','4. биология', '5. физкультура'],
             'четверг': ['1. обществознание','2. алгебра','3. химия','4. биология', '5. физкультура'],
		     'пятница': ['1. обществознание','2. алгебра','3. химия','4. биология', '5. физкультура'],
             'суббота': ['выходной'],
             'воскресенье': ['выходной'],
                 }
           }
 }
day_week = ['воскресенье', 'понедельник','вторник','среда','четверг','пятница','суббота']
def get_doc(id):
	doc = open('got.docx', 'r')
	a = vk_session("doxc.getMessagesUploadServer",{"type": 'doc', "peer_id":event.user_id})
	b = requests.post(a['upload_url'], files={"file":'doc'}).json()
	print(b)
	c = vk_session("docs.save", {"file":b['file'],'title': "document"})
	print(c)
	d = 'doc{}_{}'.format(c[0]['owner_id'], c[0]['id'])
	vk_session.method("messages.send", {"user_id": id, "attachment": d, "random_id": 0, "keyboard": vkKeyboard_2})
def get_name_user(user_id):
	user = vk_session.method("users.get",{'user_ids':user_id})
	name = user[0]['first_name']
	surname = user[0]['last_name']
	return f'{name} {surname}'
def get_but(text, color):
	return {"action": {
				"type": "text",
				"payload": "{\"button\": \"" + "1" + "\"}",
				"label": f"{text}"},
			"color": f"{color}"}
def get_openlink_but(text, URl):
	return {"action": {
		"type": "open_link",
		"link": URl,
		"payload": "{\"button\": \"" + "1" + "\"}",
		"label": f"{text}"}
	}
vkKeyboard_1 = {
	"one_time" : None,
	"buttons" : [
		[get_but('Родителям', 'primary')],
    	[get_but('Ученикам', 'primary')],
		[get_openlink_but('Cайт&#8599;', 'https://3653.ru/')],
		[get_but('Помощь&#128172;', 'negative')]

	]}
vkKeyboard_2 = {
	"one_time" : False,
	"buttons" : [
		[get_but('Анкета', 'primary')],
    	[get_but('Расписание&#128342;', 'primary')],
		[get_but('Документы&#128193;', 'negative')],
		[get_but('Меню&#128203;', 'positive')],
	]}
vkKeyboard_3 = {
	"one_time" : False,
	"buttons" : [
		[get_but('Твой друг', 'primary')],
    	[get_but('Телефон доверия', 'primary')],
		[get_openlink_but('Дневник.Ру&#127890;', 'https://dnevnik.ru')],
		[get_but('Меню&#128203;', 'negative')]
	]}
vkKeyboard_4 = {
	"one_time" : False,
	"buttons" : [
		[get_but('Стоп', 'negative')]
	]}
vkKeyboard_5 = {
	"one_time" : False,
	"buttons" : [
		[get_but('Связь со специалистом&#9742;', 'positive')],
		[get_but('Меню&#128203;', 'negative')]
	]}



vkKeyboard_1 = dumps(vkKeyboard_1, ensure_ascii = False).encode('utf-8')
vkKeyboard_1 = str(vkKeyboard_1.decode('utf-8'))

vkKeyboard_2 = dumps(vkKeyboard_2, ensure_ascii = False).encode('utf-8')
vkKeyboard_2 = str(vkKeyboard_2.decode('utf-8'))

vkKeyboard_3 = dumps(vkKeyboard_3, ensure_ascii = False).encode('utf-8')
vkKeyboard_3 = str(vkKeyboard_3.decode('utf-8'))

vkKeyboard_4 = dumps(vkKeyboard_4, ensure_ascii = False).encode('utf-8')
vkKeyboard_4 = str(vkKeyboard_4.decode('utf-8'))

vkKeyboard_5 = dumps(vkKeyboard_5, ensure_ascii = False).encode('utf-8')
vkKeyboard_5 = str(vkKeyboard_5.decode('utf-8'))

specialists = ["340310013","528986727"]

def VKhear(wait_answer):
	global event
	"""
	Производит мониторинг сообщений для бота во Вконтакте.
	Когда получает новое сообщение, возвращает его.
	"""
	try:
		for event in longpoll.listen():
			if event.type == VkEventType.MESSAGE_NEW and event.to_me:
				if wait_answer:
					return event.text.lower()
				server(event.text.lower())
	except Exception as e:
		print(f"Возникла неизвестная ошибка на сервере!\nТекст ошибки: {e}")
		pass

def communication_the_client(id, text):
	sender(id, text)

def day_week(day):
	day_week = ['воскресенье', 'понедельник','вторник','среда','четверг','пятница','суббота']
	for i in range(len(day_week)):
		if day_week[i] == day:
			namber = i
	return namber
anketa = ['Фамилию Имя Отчество', 'класс зачисления', 'Дату Рождения', 'домашний адрес', 'домашний телефон', 'Фамилию Имя Отчество законного представителя', 'Телефон']

def server(cmd):
	"""
	Производит обработку полученных сообщений.
	Вызывает серверные функции, если сообщение содержит вызов серверной функции,
	иначе сообщает отправителю об получении команды, обрабатывает команду в соответствии со стандартом и возвращает её.
	"""

	dt_now = dt.datetime.now()
	if ("прив" in cmd or "здравствуй" in cmd) or ('hi' in cmd or 'hello' in cmd):
		if int(str(dt_now.time()).split(':')[0]) >= 6 and int(str(dt_now.time()).split(':')[0]) < 12:
			sender(event.user_id, choice(('Доброе утро', "Здравствуйте", "Здравствуйте, что вас интересует?")))
		elif int(str(dt_now.time()).split(':')[0]) >= 12 and int(str(dt_now.time()).split(':')[0]) < 17:
			sender(event.user_id, choice(("Добрый день", "Здравствуйте", "Здравствуйте", "Здравствуйте, что вас интересует?")))
		elif int(str(dt_now.time()).split(':')[0]) >= 17 and int(str(dt_now.time()).split(':')[0]) < 21:
				sender(event.user_id, choice(("Добрый вечер", "Здравствуйте", "Здравствуйте", "Здравствуйте, что вас интересует?")))
		elif int(str(dt_now.time()).split(':')[0]) >= 21 or int(str(dt_now.time()).split(':')[0]) < 6:
				sender(event.user_id, choice(("Доброй ночи", "Здравствуйте", "Здравствуйте", "Здравствуйте, что вас интересует?")))
	elif cmd == 'телефон доверия':
		sender(event.user_id,'Ты всегда можешь обратиться за помощью по телефону +7-800-2000-122', vkKeyboard_3)
	elif cmd == 'родителям':
		sender(event.user_id, "В этом разделе вы сможете получить ответы на самые часто задаваемые вопросы такие как: \n- отслеживание заявок на поступление в школу- направления доп образования \n- информацию о расписании \n- школьная форма\n- питание в школе \n- записать ребенка в наше образовательное учреждение", vkKeyboard_2)
	elif 'меню' in cmd:
		sender(event.user_id, choice(("Что вас ещё интересует?", "Я могу чем-нибудь ещё помочь?")) , vkKeyboard_1)
	elif cmd == 'ученикам':
		sender(event.user_id, "Здесь я тебе помогу решить некоторые вопросы, например:\n-список литературы\n-найти расписание\n-решить вопрос с поступлением\nи наконец я могу просто поболтать с тобой, если тебе скучно, обращайся)", vkKeyboard_3)
	elif cmd == 'начать':
		sender(event.user_id, "Здравствуйте, я бот Школы №36&#127979; Я отвечу на интересующие вас вопросы и в случае необходимости свяжу вас со специалистом. Пишите, я всегда готов ответить вам&#129302;", vkKeyboard_1)
	elif 'помощь' in cmd:
		sender(event.user_id, "Вы можете обратиться за помощью к специалисту", vkKeyboard_5)
	elif cmd == 'связь с клиентом' and str(event.user_id) in specialists:
		sender(event.user_id, "Что отправить?")
		wait = VKhear(True)
		print(wait)
		id = wait
		wait = VKhear(True)
		print(wait)
		text = wait
		communication_the_client(id,text)
	elif cmd == 'все специалисты' and str(event.user_id) in specialists:
		for x in specialists:
			sender(event.user_id, f"{get_name_user(x)}, id:{x}")
	elif 'связь со специалистом' in cmd:
		sender(event.user_id, "Я отправил уведомление администратору", vkKeyboard_5)
		sender(event.user_id, "Он обязательно с вами свяжется", vkKeyboard_5)
		sender(specialists[0], f"С вами хочет связаться {get_name_user(event.user_id)}, id:{event.user_id}", vkKeyboard_5)
	elif cmd == 'добавить специалиста' and str(event.user_id) in specialists:
		wait = VKhear(True)
		print(wait)
		specialist = wait
		specialists.append(str(wait))
		sender(event.user_id, "Пользователь добавлен")
		sender(specialist, "Вас добавили в специалисты чат бота")
	elif cmd == 'удалить специалиста' and str(event.user_id) in specialists:
		wait = VKhear(True)
		print(wait)
		specialist = str(wait)
		for i in range(len(specialist)):
			if specialists[i] == specialist:
				del specialists[i]
				break
		sender(event.user_id, "Пользователь удален")
		sender(specialist, "Вы больше не специалист чат бота")
	elif cmd == 'анкета':
		x = True
		context = dict()
		sender(event.user_id, "Я могу вам помочь с её заполнением", vkKeyboard_4)
		doc = DocxTemplate("shablon_ankety.docx")
		otvet = []
		for i in range(len(anketa)):
			sender(event.user_id, choice(('Назовите, пожалуйста, ','Разрешите узнать ', 'Скажите, пожалуйста,')) + anketa[i],vkKeyboard_4)
			wait = VKhear(True)
			print(wait)
			if wait == 'стоп':
				x = False
				sender(event.user_id, choice(("Что вас ещё интересует?", "Я могу чем-нибудь ещё помочь?")), vkKeyboard_1)
				break
			otvet.append(wait)
		if x:
			sender(event.user_id, choice(('Минутку', 'Анкета а разработке', 'Подождите, заполняю данные')), vkKeyboard_2)
			context['child'] = otvet[0]
			context['cllass'] = otvet[1]
			context['borndata'] = otvet[2]
			context['adress'] = otvet[3]
			context['homenum'] = otvet[4]
			context['FIO'] = otvet[5]
			context['number'] = otvet[6]
			doc.render(context)
			doc.save(f"{event.user_id}.docx")
			sender(event.user_id, "Ваша анкета готова",vkKeyboard_2)
	elif "документ" in cmd:
		sender(event.user_id, "Какие именно документы вас интересуют: согласия или заявления?", vkKeyboard_2)
		g = VKhear(True)
		print(g)
		if "согласия" in g:
			sender(event.user_id, "Согласие на что вам необходимо?",vkKeyboard_2)
			sender(event.user_id, "Фото и видео съемка, обработка персональных данных, обучение "
								  "по адаптированной основной образовательной программе", vkKeyboard_2)
			e = VKhear(True)
			print(e)
			if "фото" in e or "видео" in e:
				send(event.user_id, "doc-211759105_632243305", vkKeyboard_2)
				send(event.user_id, "doc-211759105_632243316", vkKeyboard_2)
			elif "персональн" in e:
				send(event.user_id, "doc-211759105_632243394", vkKeyboard_2)
				send(event.user_id, "doc-211759105_632243376", vkKeyboard_2)
			elif "адаптирован" in e:
				send(event.user_id, "doc-211759105_632243332", vkKeyboard_2)
				send(event.user_id, "doc-211759105_632243352", vkKeyboard_2)
			else:
				sender(event.user_id, choice(("Извините, произошла ошибка &#128528;", "Извините, я вас не понимаю &#128533;","К сожалению, не знаю такого(")), vkKeyboard_2)
		elif "заявления" in g:
			sender(event.user_id, "Заявление на что вам необходимо?", vkKeyboard_2)
			sender(event.user_id, "Прием в школу", vkKeyboard_2)
			sender(event.user_id, "Отсутствие в школе", vkKeyboard_2)
			sender(event.user_id, "Перевод в другой класс", vkKeyboard_2)
			sender(event.user_id, "Родной язык", vkKeyboard_2)
			e = VKhear(True)
			print(e)
			if "прием" in e:
				send(event.user_id, "doc-211759105_632243005", vkKeyboard_2)
				send(event.user_id, "doc-211759105_632243032", vkKeyboard_2)
				send(event.user_id, "doc-211759105_632243048", vkKeyboard_2)
			elif "отсутствие" in e:
				send(event.user_id, "doc-211759105_632243107", vkKeyboard_2)
			elif "род" in e:
				send(event.user_id, "doc-211759105_632243143", vkKeyboard_2)
			elif "перевод" in e or "другой" in e:
				send(event.user_id, "doc-211759105_632243122", vkKeyboard_2)
			else:
				sender(event.user_id,
					   choice(("Извините, произошла ошибка &#128528;", "Извините, я вас не понимаю &#128533;",
							   "К сожалению, не знаю такого(")), vkKeyboard_2)
	elif "поступление" in cmd or "поступить" in cmd:
		sender(event.user_id, choice(("Поступление в какой класс вас интересует? 1 или 10?",
									  "Хотите поступить к нам? Прекрасно! В 1 или 10 класс?")))
		g = VKhear(True)
		print(g)
		if 'первый' in g or "1" in g:
			sender(event.user_id, "Вот список необходимых документов &#128071;")
			sender(event.user_id, "1. Заявление, согласие (в формате .pdf, .jpeg, объемом не более 1 Мбайт,"
								  " не заархивированным файлом);")
			sender(event.user_id,
				   "2. Копия документа удостоверяющего личность родителя (законного представителя) ребенка;")
			sender(event.user_id,
				   "3. Копия документа о регистрации ребенка по месту жительства на закрепленной территории;")
			sender(event.user_id, "4. Документы, подтверждающие первоочередное право в приеме на обучения;")
			sender(event.user_id, "5. Разрешение о приеме на обучение (в случае, если ребенок не достиг на 01.09.2021г."
								  " возраста 6 лет и 6 месяцев), выданное Комитетом по образованию Администрации Великого Новгорода;")
			sender(event.user_id, "6. Копия свидетельства о рождении ребенка.")
		elif "10" in g or "десятый" in g:
			sender(event.user_id, "Смотрите:")
			sender(event.user_id, "У нас есть три профиля:")
			sender(event.user_id, "Технологический профиль (25 мест)")
			sender(event.user_id, "Естественнонаучный профиль (25 мест)")
			sender(event.user_id, "Гуманитарный профиль (25 мест)")
			sender(event.user_id, "Без индивидуального отбора на выбранный профиль зачисляются:")
			sender(event.user_id, "&#128213; выпускники, получившие аттестат особого образца;")
			sender(event.user_id,
				   "&#127941; победители регионального этапа чемпионата «Молодые профессионалы» (WorldSkills Russia),"
				   " олимпиады Национальной Технологической Инициативы (НТИ), всероссийской олимпиады школьников.")
			sender(event.user_id,
				   "Подробности можно посмотреть на нашем сайте: https://3653.ru/roditelyam/priem10klass/")
		else:
			sender(event.user_id, "Извините я вас не понимаю &#128577;")
	elif "образовани" in cmd:
		sender(event.user_id, "Мы можем предоставить Вам следующие направления:")
		sender(event.user_id, "&#128203; Социально-гуманитарное")
		sender(event.user_id, "&#128029; Естественнонаучное")
		sender(event.user_id, "&#128187; Техническое")
		sender(event.user_id, "&#127912; Художественное")
		sender(event.user_id, "&#9917; Физкультурно-спортивное")

	elif "админ" in cmd:
		sender(event.user_id, choice(("Ждет ваших вопросов &#129309;: https://vk.com/id528986727 ",
									  "Администратор всегда к вашим услугам &#128526;: https://vk.com/id528986727")))
	elif "айтикуб" in cmd or "itcube" in cmd or "it-cube" in cmd:
		sender(event.user_id, choice(("Подробности узнавайте у наших друзей &#128073;: https://vk.com/club211697673",
									  "Вся информация здесь &#128080;: https://vk.com/club211697673",
									  "Михаил Михайлович вам все расскажет: https://vk.com/club211697673")))
	elif "каникул" in cmd:
		send(event.user_id, "photo-211697920_457239018")
	elif "список литературы" in cmd or "литература" in cmd:
		sender(event.user_id, choice(("Какой класс интересует?", "Напиши свой класс", "Выбери класс")))
		g = VKhear(True)
		print(g)
		x = True
		while x:
			if g == "5":
				vk_session.method("messages.send", {"peer_id": event.user_id, "message": "Хорошего прочтения!&#128218;",
													"attachment": 'photo-211759105_457239030', "random_id": 0})
				x = False
			elif g == "6":
				vk_session.method("messages.send", {"peer_id": event.user_id, "message": "Хорошего прочтения!&#128218;",
													"attachment": 'photo-211759105_457239031', "random_id": 0})
				x = False
			elif g == "7":
				vk_session.method("messages.send", {"peer_id": event.user_id, "message": "Хорошего прочтения!&#128218;",
													"attachment": get_image(image), "random_id": 0})
				x = False
			elif g == "8":
				vk_session.method("messages.send", {"peer_id": event.user_id, "message": "Хорошего прочтения!&#128218;",
													"attachment": 'photo-211759105_457239028', "random_id": 0})
				x = False
			elif g == "9":
				vk_session.method("messages.send", {"peer_id": event.user_id, "message": "Хорошего прочтения!&#128218;",
													"attachment": 'photo-211759105_457239032', "random_id": 0})
				x = False
			elif g == "10":
				vk_session.method("messages.send", {"peer_id": event.user_id, "message": "Хорошего прочтения!&#128218;",
													"attachment": 'photo-211759105_457239033', "random_id": 0})
				x = False
			elif g == "11":
				vk_session.method("messages.send", {"peer_id": event.user_id, "message": "Хорошего прочтения!&#128218;",
													"attachment": 'photo-211759105_457239029', "random_id": 0})
				x = False
			else:
				sender(event.user_id, choice(("Повтори-ка", "Я не понял", "Не знаю такого","Ты какой-то непонятный, давай яснее &#128577;", "Я вас не понимаю &#128528;")))

	elif "форм" in cmd:
		sender(event.user_id, "Образцы школьной формы &#128071;")
		send(event.user_id, "photo-211697920_457239019")
		send(event.user_id, "photo-211697920_457239021")
		send(event.user_id, "photo-211697920_457239020")
	elif "столовая" in cmd or "столовую" in cmd or "столовой" in cmd or "питани" in cmd:
		sender(event.user_id, "Что конкретно вас интересует: график работы , стоимость, краткая информация?")
		g = VKhear(True)
		print(g)
		if g == "график":
			send(event.user_id, "photo-211697920_457239022")
		elif g == "стоимость":
			sender(event.user_id, "&#127859; Завтрак - 90 руб.")
			sender(event.user_id, "&#127861;Обед - 110 руб.")
			sender(event.user_id, "&#129367; Полдник - 60 руб.")
		elif g == "краткая информаци я":
			sender(event.user_id,
				   'Наша столовая находится на системе АУТСОРСИНГА! Услуги аутсорсинга оказывает компания'
				   'ООО "Комплекс Сервис". Приготовление пищи осуществляется из продуктов, закупаемых '
				   'ООО "Комплекс-сервис" на основании договора.')
		else:
			sender(event.user_id, "Извините, произошла ошибка &#128528;")
	elif "пока" in cmd or "до свидания" in cmd:
		sender(event.user_id, choice(("Всего хорошего&#128521;", "пока&#128075;", "Чао ", "Еще увидимся&#128579;", "пока-пока", "До свидания")))
	elif "спасибо" in cmd or "спс" in cmd:
		sender(event.user_id, choice(("Не за что&#128080;", "Всегда пожалуйста", "Обращайтесь", "Рад был помочь&#128522;")))
	elif "как дела" in cmd or "как ты" in cmd:
		sender(event.user_id, choice(("Лучше всех!", "Отлично! Чего и вам желаю", "Как в сказке",
									  "Ах я бедный-несчастный, так устал, мне каждый день приходится придумывать ответ"
									  " на вопрос «Как дела?»", "Затрудняюсь ответить", "Дела? ?? Нет их, не деловой я",
									  "Также, как и пять минут назад", "Задай другой вопрос пожалуйста",
									  "Как всегда, то есть хорошо")))
	elif "что тебе нравится" in cmd or "что ты любишь" in cmd:
		sender(event.user_id, choice(("Есть, спать, ну и работать тоже (наверное)", "Такие секреты не выдаю &#129296;",
									  "Ой, да много всего, давай лучше о тебе", "Честно, не знаю", "Я бот простой - "
																								  "на вопрос ответил и доволен")))
	elif "давай" in cmd:
		sender(event.user_id, "мне нравится твоя инициатива")
	elif "я люблю" in cmd or "мне нравится" in cmd:
		sender(event.user_id,
			   choice(("Классно", "Не часто встретишь встретишь человека с таким вкусом, ты крутой &#128516;",
					   "Мне тоже&#128579;", "Спасибо что поделился))", "Ого, у нас даже вкусы похожи!")))
	elif "круто" in cmd or "классн" in cmd:
		sender(event.user_id, choice(("Стараюсь для вас", "спасибо&#128073;&#128072;", "Я знаю&#128526;", "Это еще не "
																										  "самое крутое между прочим)")))
	elif "сколько тебе" in cmd:
		sender(event.user_id, choice(("Зависит от ситуации, а тебе?", "Не надо о грустном, лучше скажи сколько тебе",
									  "Я относительно молод, однако точно сказать не могу, а тебе?")))
		e = VKhear(True)
		print(e)
		sender(event.user_id, choice(("Мог бы и правду сказать)", "Ладно", "Ок, я понял&#128521;")))
	elif "скучно" in cmd or "не хочу" in cmd or "не люблю" in cmd:
		sender(event.user_id, choice(("Никогда не наклоняй голову. Держи ее высоко. Смотри миру прямо в глаза.",
									  "У тебя все получится, главное начни делать любимое дело",
									  "Твое место в мире — твоя жизнь. Иди и сделай с ней ту жизнь, которой хочешь жить."
									  )))
	elif "боюсь" in cmd:
		sender(event.user_id, choice(("Не бойтесь отказаться от хорошего, чтобы пойти за великим.",
									  "Твое место в мире — твоя жизнь. Иди и сделай с ней ту жизнь, которой хочешь жить",
									  "Однажды побоявшись что-то сделать, ты можешь сожалеть об этом в будущем")))
	elif "как" in cmd and "учить" in cmd or "урок" in cmd or "учеб" in cmd:
		sender(event.user_id, choice(("Может это сможет помочь тебе&#9994;", "Я могу дать тебе пару советов&#129300;",
									  "Я постараюсь помочь тебе ")))
		sender(event.user_id, "Вот пара советов")
		sender(event.user_id, choice(("Найдите мощную мотивацию", "Выбирайте правильное время для занятий",
									  "Создайте распорядок дня", "Перестаньте прокрастинировать",
									  "Позвольте себе увлечься учебой")))
		sender(event.user_id,
			   choice(("Наладьте контакт с учителями&#129309;", "Перестаньте гнаться за отметками&#127939;",
					   "Создайте комфортное рабочее место", "Задействуйте максимум каналов для обучения",
					   "Не переоценивайте чужое мнение")))
	elif "бот" in cmd:
		sender(event.user_id, "Я здесь")
	elif "пон" in cmd:
		sender(event.user_id, choice(("Я рад что вы поняли&#128079;", "&#9786;", "&#129303;")))
	elif "ладно" in cmd or cmd == "ок":
		sender(event.user_id, "ок")
	elif 'расписание' in cmd:
		sender(event.user_id, "Скажи, пожалуйста, номер класса и букву, например 1а")
		kl = VKhear(True)
		print(kl)
		kl1 = raspisanie[str(kl)[0]]
		kl2 = kl1[kl[1]]
		sender(event.user_id, "На какой день недели?")
		day = VKhear(True)
		print(day)
		ras = ' '.join(kl2[day])
		sender(event.user_id, ras, vkKeyboard_2)
	elif cmd == 'твой друг':
		sender(event.user_id, 'Привет, здесь мы можем поболтать&#128064;', vkKeyboard_2)
	else:
		sender(event.user_id, "Извините, произошла ошибка &#128528;")
		sender(event.user_id, "Хотите переотправлю вас на специалиста?")

	return

def sender(id, text, key=vkKeyboard_1):
	"""
	Принимает id получателя и текст сообщения.
	Производит отправку сообщения получателю во Вконтакте.
	"""
	vk_session.method("messages.send", {"user_id": id, "message": text, "random_id": 0, "keyboard": key})
	return
def send(id, doc, key):
	vk_session.method("messages.send", {"user_id": id, "attachment": doc, "random_id": 0, "keyboard": key})
	return
def main():
	while True:
		VKhear(False)

if __name__ == "__main__":
	main()





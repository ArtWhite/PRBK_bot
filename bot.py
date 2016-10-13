import telebot
import config
import random
from telebot import types

bot = telebot.TeleBot(config.token)

ark = ['«Куни короче...»', '«Ни@#я не учит до$%@&б»', '«Я тебе сейчас по мозгам врежу, до$%@&б...»', '«Кх-кх... Е$%@ее мороженное, гангстера сгубило...»', '«Бабы сдают жопами, мужики головами...»']


@bot.message_handler(commands=['start'])
def check_group(message):
	bot.send_message(message.chat.id, 'Узнать расписание - /rasp\nПример сообщения: «15ОИТ18 понедельник»\n\nРасписание звонков - /zvrasp\n\nРандомная цитата Аркаши - /ark_rand\n\nО боте - /about')

@bot.message_handler(commands=['about'])
def about(message):
	bot.send_photo(message.chat.id, photo='http://rsimru.ru/img/robot.jpg')
	bot.send_message(message.chat.id, 'Привет, я бот, который поможет узнать тебе расписание пар и звонков\n\nДля пополнения списка цитат Аркаши пишите Творцу\n\nНу и если у вас есть какие-то предложение, то тоже пишите творцу\n\nТворец: @ArtWhite')

@bot.message_handler(commands=['ark_rand'])
def rand_ark(message):
	bot.send_message(message.chat.id, ark[random.randint(0, 4)])
#bot.send_message(message.chat.id, 'В разработке\n    ¯\_(ツ)_/¯')

@bot.message_handler(commands=['zvrasp'])
def check_group(message):
	bot.send_message(message.chat.id, '1. 8:20 - 9:55 \n    Перемена 10 мин. \n\n2. 10:05 - 11:40 \n    Перемена 20 мин. \n\n3. 12:00 - 13:35 \n    Перемена 20 мин.\n\n4. 13:55 - 15:30 \n    Перемена 10 мин.\n\n5. 15:40 - 17:15 \n    Перемена 10 мин.\n\n6. 17:25 - 19:00 \n    Перемена 10 мин.')

@bot.message_handler(commands=['commands'])
def check_group(message):
	bot.send_message(message.chat.id, 'Узнать расписание - /rasp\n\nРасписание звонков - /zvrasp\n\nРандомная цитата Аркаши - /ark_rand\n\nО боте - /about\n\nКоманды - /commands')


@bot.message_handler(commands=['rasp'])
def check_group(message):
	bot.send_message(message.chat.id, 'Введите вашу группу и день недели.\n\n1 Пример сообщения: «15ОИТ18 понедельник»\n\n2 Пример сообщения: «15оит18 чт»')
	@bot.message_handler(content_types=["text"])	
	def check_rasp(message):
		while message.text != "Назад":





				# ---------- 1 КУРС ----------

				#1411


				# ---------- 2 КУРС ----------

				if message.text == '15ОИТ18 понедельник' or message.text == '15оит18 понедельник' or message.text == '15оит18 пн' or message.text == '15ОИТ18 пн':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. Основы программирования\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '3. Эл-ты вм\n    Зиманова Т.В\n    Ауд 102')
					bot.send_message(message.chat.id, '4. Рус. яз. и культура речи\n    Сергацкова О.В\n    Ауд 203')
					break;
				if message.text == '15ОИТ18 вторник' or message.text == '15оит18 вторник' or message.text == '15оит18 вт' or message.text == '15ОИТ18 вт':
					bot.send_message(message.chat.id, '1. Эл-ты вм\n    Зиманова Т.В\n    Ауд 102')
					bot.send_message(message.chat.id, '2. Основы программирования\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '3. физ-ра\n    соломинский')
					break;
				if message.text == '15ОИТ18 среда' or message.text == '15оит18 среда' or message.text == '15оит18 ср' or message.text == '15ОИТ18 ср':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. ИТ / Рус. яз\n    Антонова Е.Ю / Сергацкова О.В\n    Ауд 316 / Ауд 203')
					bot.send_message(message.chat.id, '3. Основы программирования\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '4. Ин. яз\n    Спирина Л.И\n    Ауд 205')
					break;
				if message.text == '15ОИТ18 четверг' or message.text == '15оит18 четверг' or message.text == '15оит18 чт' or message.text == '15ОИТ18 чт':
					bot.send_message(message.chat.id, '1. ИТ / _\n    Антонова Е.Ю / _\n    Ауд 316 / _')
					bot.send_message(message.chat.id, '2. Эл-ты вм\n    Зиманова Т.В\n    Ауд 102')
					bot.send_message(message.chat.id, '3. Основы программирования / ИТ\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '4. _ / Основы программирования\n    _ / Инюшкина Т.А\n    _ / Ауд 14г')
					break;
				if message.text == '15ОИТ18 пятница' or message.text == '15оит18 пятница' or message.text == '15оит18 пт' or message.text == '15ОИТ18 пт':
					bot.send_message(message.chat.id, '1. Теория алгоритмов\n    Бачуринаа Т.А\n    Ауд 102')
					bot.send_message(message.chat.id, '2. ИТ\n    Антонова Е.Ю\n    Ауд 316')
					bot.send_message(message.chat.id, '3. Основы программирования / ИТ\n    Инюшкина Т.А\n    Ауд 14г')
					break;
				if message.text == '15ОИТ18 суббота' or message.text == '15оит18 суббота' or message.text == '15оит18 сб' or message.text == '15ОИТ18 сб':
					bot.send_message(message.chat.id, '1. Теория алгоритмов\n    Бачуринаа Т.А\n    Ауд 102')
					bot.send_message(message.chat.id, '2. ИТ\n    Антонова Е.Ю\n    Ауд 316')
					bot.send_message(message.chat.id, '3. Эл-ты вм\n    Зиманова Т.В\n    Ауд 102')
					break;


				#1517k


				if message.text == '15ОИТ17к понедельник' or message.text == '15оит17к понедельник' or message.text == '15оит17к пн' or message.text == '15ОИТ17к пн':
					bot.send_message(message.chat.id, '1. История / _\n    Токмаков Л.Ю / _\n    Ауд 210 / _')
					bot.send_message(message.chat.id, '2. ИТ\n    Антонова Е.Ю\n    Ауд 316')
					bot.send_message(message.chat.id, '3. физ-ра\n    Агапов Н.И')
					bot.send_message(message.chat.id, '4. _ / Эл-ты вм\n    _ / Зиманова Т.В\n    _ / Ауд 102')
					break;
				if message.text == '15ОИТ17к вторник' or message.text == '15оит17к вторник' or message.text == '15оит17к вт' or message.text == '15ОИТ17к вт':
					bot.send_message(message.chat.id, '1. ЭТИ\n    Куяров А.Н\n    Ауд 20')
					bot.send_message(message.chat.id, '2. Теор.вероят. и мат.статистика\n    _\n    Ауд 309')
					bot.send_message(message.chat.id, '3. Осн. электротехники\n    Тришкина В.Г\n    Ауд 124')
					break;
				if message.text == '15ОИТ17к среда' or message.text == '15оит17к среда' or message.text == '15оит17к ср' or message.text == '15ОИТ17к ср':
					bot.send_message(message.chat.id, '1. _ / Теор.вероят. и мат.статистика\n    _ / _\n    _ / Ауд 309')
					bot.send_message(message.chat.id, '2. Ин. яз\n    Зуева Е.В\n    Ауд 302')
					bot.send_message(message.chat.id, '3. История\n    Токмаков Л.Ю\n    Ауд 210')
					bot.send_message(message.chat.id, '4. Рус. яз. и культура речи / _\n    Адельшина Е.В / _\n    Ауд 109 / _')
					break;
				if message.text == '15ОИТ17к четверг' or message.text == '15оит17к четверг' or message.text == '15оит17к чт' or message.text == '15ОИТ17к чт':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. Рус. яз. и культура речи\n    Адельшина Е.В\n    Ауд 109')
					bot.send_message(message.chat.id, '3. ИС в ПД / Осн. электротехники\n    Антонова Е.Ю / Тришкина В.Г\n    Ауд 316 / Ауд 124')
					bot.send_message(message.chat.id, '4. _ / Основы программирования\n    _ / Инюшкина Т.А\n    _ / Ауд 14г')
					break;
				if message.text == '15ОИТ17к пятница' or message.text == '15оит17к пятница' or message.text == '15оит17к пт' or message.text == '15ОИТ17к пт':
					bot.send_message(message.chat.id, '1. ЭТИ\n    Куяров А.Н\n    Ауд 20')
					bot.send_message(message.chat.id, '2. Эл-ты вм\n    Зиманова Т.В\n    Ауд 102')
					bot.send_message(message.chat.id, '3. ИС в ПД\n    Антонова Е.Ю\n    Ауд 316')
					break;
				if message.text == '15ОИТ17к суббота' or message.text == '15оит17к суббота' or message.text == '15оит17к сб' or message.text == '15ОИТ17к сб':
					bot.send_message(message.chat.id, '1. Осн.алг. и программир.\n    Фролова Ж.Е\n    Ауд 19')
					bot.send_message(message.chat.id, '2. Инж. графика\n    Митрофанова С.Г\n    Ауд 121')
					bot.send_message(message.chat.id, '3. ИС в ПД\n    Антонова Е.Ю\n    Ауд 316')
					break;


				#1520


				if message.text == '15ОИТ20 понедельник' or message.text == '15оит20 понедельник' or message.text == '15оит20 пн' or message.text == '15ОИТ20 пн':
					bot.send_message(message.chat.id, '1. Основы программирования\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '2. Рус. яз. и культура речи\n    Адельшина Е.В\n    Ауд 109')
					bot.send_message(message.chat.id, '3. Эл-ты вм\n    Матвеева О.Ю\n    Ауд 215')
					break;
				if message.text == '15ОИТ20 вторник' or message.text == '15оит20 вторник' or message.text == '15оит20 вт' or message.text == '15ОИТ20 вт':
					bot.send_message(message.chat.id, '1. Основы программирования\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '2. Теория алгоритмов\n    Бачуринаа Т.А\n    Ауд 7')
					bot.send_message(message.chat.id, '3. Основы программирования\n    Инюшкина Т.А\n    Ауд 14г')
					break;
				if message.text == '15ОИТ20 среда' or message.text == '15оит20 среда' or message.text == '15оит20 ср' or message.text == '15ОИТ20 ср':
					bot.send_message(message.chat.id, '1. физ-ра\n    соломинский\n    Ауд 118')
					bot.send_message(message.chat.id, '2. Основы программирования\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '3. ИТ\n    Маркова А.В | Соколовская Т.А\n    Ауд 119a | 14a')
					bot.send_message(message.chat.id, '4. физ-ра\n    Лобкова Е.К\n    Ауд 118а')
					break;
				if message.text == '15ОИТ20 четверг' or message.text == '15оит20 четверг' or message.text == '15оит20 чт' or message.text == '15ОИТ20 чт':
					bot.send_message(message.chat.id, '1. ИТ\n    Соколовская Т.А\n    14a')
					bot.send_message(message.chat.id, '2. Ин. яз\n    Прокоданова Е.Н | Спирина Л.И\n    Ауд 308 | 205')
					bot.send_message(message.chat.id, '3. Эл-ты вм\n    Матвеева О.Ю\n    Ауд 215')
					bot.send_message(message.chat.id, '4. ИТ\n    Маркова А.В\n    Ауд 119a')
					break;
				if message.text == '15ОИТ20 пятница' or message.text == '15оит20 пятница' or message.text == '15оит20 пт' or message.text == '15ОИТ20 пт':
					bot.send_message(message.chat.id, '1. Основы программирования\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '2. Рус. яз. и культура речи / ИТ\n    Адельшина Е.В / Маркова А.В | Соколовская Т.А\n    Ауд 109 / Ауд 119a | 14a')
					bot.send_message(message.chat.id, '3. Эл-ты вм\n    Матвеева О.Ю\n    Ауд 215')
					break;
				if message.text == '15ОИТ20 суббота' or message.text == '15оит20 суббота' or message.text == '15оит20 сб' or message.text == '15ОИТ20 сб':
					bot.send_message(message.chat.id, '1. ИТ\n    Маркова А.В | Соколовская Т.А\n    Ауд 119a | 14a')
					bot.send_message(message.chat.id, '2. Эл-ты вм\n    Матвеева О.Ю\n    Ауд 215')
					bot.send_message(message.chat.id, '3. Теория алгоритмов\n    Бачуринаа Т.А\n    Ауд 7')
					break;


				#1511


				if message.text == '15ОИТ11 понедельник' or message.text == '15оит11 понедельник' or message.text == '15оит11 пн' or message.text == '15ОИТ11 пн':
					bot.send_message(message.chat.id, '1. ТСИ\n    Давыдов А.И\n    Ауд 310')
					bot.send_message(message.chat.id, '2. Рус.яз и культура речи\n    Шумарова И.В\n    Ауд 204')
					bot.send_message(message.chat.id, '3. Орг-прав.обес.инф.безоп\n    Макарова А.А\n    Ауд 309')
					break;
				if message.text == '15ОИТ11 вторник' or message.text == '15оит11 вторник' or message.text == '15оит11 вт' or message.text == '15ОИТ11 вт':
					bot.send_message(message.chat.id, '1. Рус.яз и культура речи / Орг.прав.обес.инф.безопасн\n    Шумарова И.В / Макарова А.А\n    Ауд 204 / Ауд 309')
					bot.send_message(message.chat.id, '2. физ-ра\n    Агапов Н.И')
					bot.send_message(message.chat.id, '3. Информатика\n    Антонова Е.Ю\n    Ауд 316')
					break;
				if message.text == '15ОИТ11 среда' or message.text == '15оит11 среда' or message.text == '15оит11 ср' or message.text == '15ОИТ11 ср':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. Орг.прав.обес.инф.безопасн\n    Макарова А.А\n    Ауд 309 / 213')
					bot.send_message(message.chat.id, '3. Осн.информ.безопасности\n    Судовчихина А.В\n    Ауд 7')
					bot.send_message(message.chat.id, '4. Математика\n    Воробьева Е.П\n    Ауд 314')
					break;
				if message.text == '15ОИТ11 четверг' or message.text == '15оит11 четверг' or message.text == '15оит11 чт' or message.text == '15ОИТ11 чт':
					bot.send_message(message.chat.id, '1. _ / История\n    _ / Голяндина О.Н\n    _ / Ауд 210')
					bot.send_message(message.chat.id, '2. История / Математика\n    Голяндина О.Н / Воробьева Е.П\n    Ауд 210 / Ауд 314')
					bot.send_message(message.chat.id, '3. Ин. яз\n    Зуева Е.В\n    Ауд 302')
					bot.send_message(message.chat.id, '4. Информатика\n    Антонова Е.Ю\n    Ауд 316')
					break;
				if message.text == '15ОИТ11 пятница' or message.text == '15оит11 пятница' or message.text == '15оит11 пт' or message.text == '15ОИТ11 пт':
					bot.send_message(message.chat.id, '1. Информатика\n    Антонова Е.Ю\n    Ауд 316')
					bot.send_message(message.chat.id, '2. Рус. яз. и культура речи / ИТ\n    Адельшина Е.В / Маркова А.В | Соколовская Т.А\n    Ауд 109 / Ауд 119a | 14a')
					bot.send_message(message.chat.id, '3. Эл-ты вм\n    Матвеева О.Ю\n    Ауд 215')
					break;
				if message.text == '15ОИТ11 суббота' or message.text == '15оит11 суббота' or message.text == '15оит11 сб' or message.text == '15ОИТ11 сб':
					bot.send_message(message.chat.id, '1. ИТ\n    Маркова А.В | Соколовская Т.А\n    Ауд 119a | 14a')
					bot.send_message(message.chat.id, '2. Эл-ты вм\n    Матвеева О.Ю\n    Ауд 215')
					bot.send_message(message.chat.id, '3. Теория алгоритмов\n    Бачуринаа Т.А\n    Ауд 7')
					break;



				# ---------- 3 КУРС ----------

				#1411

				if message.text == '14ОИТ11 понедельник' or message.text == '14оит11 понедельник' or message.text == '14оит11 пн' or message.text == '14ОИТ11 пн':
					bot.send_message(message.chat.id, '1. Экспл.подсист.безоп.АС\n    Аверина Е.И\n    Ауд 1')
					bot.send_message(message.chat.id, '2. Орг-прав.обес.инф.безоп\n    Макарова А.А\n    Ауд 312')
					bot.send_message(message.chat.id, '3. Ин. яз\n    Зуева Е.В\n    Ауд 302')
					break;
				if message.text == '14ОИТ11 вторник' or message.text == '14оит11 вторник' or message.text == '14оит11 вт' or message.text == '14ОИТ11 вт':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. БД\n    Хемелевская Е.Б\n    Ауд 8')
					bot.send_message(message.chat.id, '3. Орг-прав.обес.инф.безоп\n    Макарова А.А\n    Ауд 205 | 103')
					bot.send_message(message.chat.id, '4. Эксплуатация КС\n    Уланов Д.С\n    Ауд 19 | 17')
					break;
				if message.text == '14ОИТ11 среда' or message.text == '14оит11 среда' or message.text == '14оит11 ср' or message.text == '14ОИТ11 ср':
					bot.send_message(message.chat.id, '1. ТСИ\n    Давыдов А.И\n    Ауд 310')
					bot.send_message(message.chat.id, '2. БЖД\n    Минтюков В.П\n    Ауд Тир')
					bot.send_message(message.chat.id, '3. Экспл.подсист.безоп.АС\n    Аверина Е.И\n    Ауд 1')
					break;
				if message.text == '14ОИТ11 четверг' or message.text == '14оит11 четверг' or message.text == '14оит11 чт' or message.text == '14ОИТ11 чт':
					bot.send_message(message.chat.id, '1. _ / Эксплуатация КС\n    _ / Уланов Д.С\n    _ / Ауд 22')
					bot.send_message(message.chat.id, '2. Эксплуатация КС\n    Уланов Д.С\n    Ауд 22')
					bot.send_message(message.chat.id, '3. БЖД\n    Минтюков В.П\n    Ауд Тир')
					bot.send_message(message.chat.id, '4. Эксплуатация КС / _\n    Уланов Д.С / _\n    Ауд 22 / _')
					break;
				if message.text == '14ОИТ11 пятница' or message.text == '14оит11 пятница' or message.text == '14оит11 пт' or message.text == '14ОИТ11 пт':
					bot.send_message(message.chat.id, '1. Экспл.подсист.безоп.АС\n    Аверина Е.И\n    Ауд 1')
					bot.send_message(message.chat.id, '2. физ-ра\n    Агапов Н.И')
					bot.send_message(message.chat.id, '3. Орг-прав.обес.инф.безоп\n    Макарова А.А\n    Ауд 124 | 121')
					break;
				if message.text == '14ОИТ11 суббота' or message.text == '14оит11 суббота' or message.text == '14оит11 сб' or message.text == '14ОИТ11 сб':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. Экспл.подсист.безоп.АС\n    Аверина Е.И\n    Ауд 1 | 5')
					bot.send_message(message.chat.id, '3. Эксплуатация КС / БЖД\n    Уланов Д.С / Минтюков В.П\n    Ауд 22 / Ауд Тир')
					bot.send_message(message.chat.id, '4. ТСИ / Эксплуатация КС\n    Давыдов А.И / Уланов Д.С\n    Ауд 310 / Ауд 22')
					break;


					#1415


				if message.text == '14ОИТ15 понедельник' or message.text == '14оит15 понедельник' or message.text == '14оит15 пн' or message.text == '14ОИТ15 пн':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. Цифр.схемотехника\n    Куяров А.Н\n    Ауд 20')
					bot.send_message(message.chat.id, '3. НТД в обл.ИТ\n    Ташкинов В.В\n    Ауд 14в | 317')
					bot.send_message(message.chat.id, '4. Ин. яз\n    Зуева Е.В\n    Ауд 302')
					break;
				if message.text == '14ОИТ15 вторник' or message.text == '14оит15 вторник' or message.text == '14оит15 вт' or message.text == '14ОИТ15 вт':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					bot.send_message(message.chat.id, '3. Дискрет.математика\n    Дорофеев Д.В\n    Ауд 104')
					bot.send_message(message.chat.id, '4. Цифр.схемотехника\n    Куяров А.Н\n    Ауд 20')
					break;
				if message.text == '14ОИТ15 среда' or message.text == '14оит15 среда' or message.text == '14оит15 ср' or message.text == '14ОИТ15 ср':
					bot.send_message(message.chat.id, '1. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					bot.send_message(message.chat.id, '2. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					bot.send_message(message.chat.id, '3. Дискрет.математика / НТД в обл.ИТ\n    Дорофеев Д.В / Ташкинов В.В\n    Ауд 104 / 304')
					break; 
				if message.text == '14ОИТ15 четверг' or message.text == '14оит15 четверг' or message.text == '14оит15 чт' or message.text == '14ОИТ15 чт':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. ЭТИ\n    Куяров А.Н\n    Ауд 20')
					bot.send_message(message.chat.id, '3. БЖД\n    Минтюков В.П\n    Ауд 122')
					bot.send_message(message.chat.id, '4. Цифр.схемотехника\n    Куяров А.Н\n    Ауд 20')
					break;
				if message.text == '14ОИТ15 пятница' or message.text == '14оит15 пятница' or message.text == '14оит15 пт' or message.text == '14ОИТ15 пт':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. Цифр.схемотехника\n    Куяров А.Н\n    Ауд 20')
					bot.send_message(message.chat.id, '3. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					bot.send_message(message.chat.id, '4. ЭТИ\n    Куяров А.Н\n    Ауд 20')
					break;
				if message.text == '14ОИТ15 суббота' or message.text == '14оит15 суббота' or message.text == '14оит15 сб' or message.text == '14ОИТ15 сб':
					bot.send_message(message.chat.id, '1. НТД в обл.ИТ\n    Ташкинов В.В\n    Ауд 14в | 317')
					bot.send_message(message.chat.id, '2. физ-ра\n    Агапов Н.И')
					bot.send_message(message.chat.id, '3. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					break;


					#1416к


				if message.text == '14ОИТ16к понедельник' or message.text == '14оит16к понедельник' or message.text == '14оит16к пн' or message.text == '14ОИТ16к пн':
					bot.send_message(message.chat.id, '1. Цифр.схемотехника\n    Богданов А.В\n    Ауд 17')
					bot.send_message(message.chat.id, '2. БЖД\n    Минтюков В.П\n    Ауд Тир')
					bot.send_message(message.chat.id, '3. Цифр.схемотехника\n    Богданов А.В\n    Ауд 17')
					break;
				if message.text == '14ОИТ16к вторник' or message.text == '14оит16к вторник' or message.text == '14оит16к вт' or message.text == '14ОИТ16к вт':
					bot.send_message(message.chat.id, '1. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					bot.send_message(message.chat.id, '2. физ-ра\n    соломинский')
					bot.send_message(message.chat.id, '3. ЭТИ\n    Куяров А.Н\n    Ауд 20')
					break;
				if message.text == '14ОИТ16к среда' or message.text == '14оит16к среда' or message.text == '14оит16к ср' or message.text == '14ОИТ16к ср':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. Цифр.схемотехника\n    Богданов А.В\n    Ауд 17')
					bot.send_message(message.chat.id, '3. НТД в обл.ИТ / Дискрет.математика\n    Ташкинов В.В / Дорофеев Д.В\n    Ауд 312 / 104')
					bot.send_message(message.chat.id, '4. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					break; 
				if message.text == '14ОИТ16к четверг' or message.text == '14оит16к четверг' or message.text == '14оит16к чт' or message.text == '14ОИТ16к чт':
					bot.send_message(message.chat.id, '1. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					bot.send_message(message.chat.id, '2. Ин. яз\n    Зуева Е.В | Синячкина Н.Ю\n    Ауд 302 | 306')
					bot.send_message(message.chat.id, '3. ЭТИ\n    Куяров А.Н\n    Ауд 20')
					break;
				if message.text == '14ОИТ16к пятница' or message.text == '14оит16к пятница' or message.text == '14оит16к пт' or message.text == '14ОИТ16к пт':
					bot.send_message(message.chat.id, '1. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					bot.send_message(message.chat.id, '2. НТД в обл.ИТ\n    Ташкинов В.В\n    Ауд 309')
					bot.send_message(message.chat.id, '3. Дискрет.математика\n    Дорофеев Д.В\n    Ауд 104')
					break;
				if message.text == '14ОИТ16к суббота' or message.text == '14оит16к суббота' or message.text == '14оит16к сб' or message.text == '14ОИТ16к сб':
					bot.send_message(message.chat.id, '1. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					bot.send_message(message.chat.id, '2. НТД в обл.ИТ\n    Ташкинов В.В\n    Ауд 309')
					bot.send_message(message.chat.id, '3. Цифр.схемотехника\n    Богданов А.В\n    Ауд 17')
					break;


					#1417к


				if message.text == '14ОИТ17к понедельник' or message.text == '14оит17к понедельник' or message.text == '14оит17к пн' or message.text == '14ОИТ17к пн':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. Цифр.схемотехника\n    Богданов А.В\n    Ауд 17')
					bot.send_message(message.chat.id, '3. БЖД\n    Минтюков В.П\n    Ауд Тир')
					bot.send_message(message.chat.id, '4. Цифр.схемотехника\n    Богданов А.В\n    Ауд 17 | 12')
					break;
				if message.text == '14ОИТ17к вторник' or message.text == '14оит17к вторник' or message.text == '14оит17к вт' or message.text == '14ОИТ17к вт':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. ЭТИ\n    Куяров А.Н\n    Ауд 20')
					bot.send_message(message.chat.id, '3. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					bot.send_message(message.chat.id, '4. физ-ра\n    соломинский')
					break;
				if message.text == '14ОИТ17к среда' or message.text == '14оит17к среда' or message.text == '14оит17к ср' or message.text == '14ОИТ17к ср':
					bot.send_message(message.chat.id, '1. Цифр.схемотехника\n    Богданов А.В\n    Ауд 17')
					bot.send_message(message.chat.id, '2. Ин. яз\n    Спирина Л.И\n    Ауд 205')
					bot.send_message(message.chat.id, '3. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					break; 
				if message.text == '14ОИТ17к четверг' or message.text == '14оит17к четверг' or message.text == '14оит17к чт' or message.text == '14ОИТ17к чт':
					bot.send_message(message.chat.id, '1. ЭТИ\n    Куяров А.Н\n    Ауд 20')
					bot.send_message(message.chat.id, '2. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					bot.send_message(message.chat.id, '3. НТД в обл.ИТ\n    Ташкинов В.В\n    Ауд 309 | 14a')
					break;
				if message.text == '14ОИТ17к пятница' or message.text == '14оит17к пятница' or message.text == '14оит17к пт' or message.text == '14ОИТ17к пт':
					bot.send_message(message.chat.id, '1. Дискрет.математика / НТД в обл.ИТ\n    Дорофеев Д.В / Ташкинов В.В\n    Ауд 104 / 309')
					bot.send_message(message.chat.id, '2. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					bot.send_message(message.chat.id, '3. Цифр.схемотехника\n    Богданов А.В\n    Ауд 5')
					break;
				if message.text == '14ОИТ17к суббота' or message.text == '14оит17к суббота' or message.text == '14оит17к сб' or message.text == '14ОИТ17к сб':
					bot.send_message(message.chat.id, '1. Дискрет.математика\n    Дорофеев Д.В\n    Ауд 104')
					bot.send_message(message.chat.id, '2. Проектирование ЦУ\n    Шмокин М.Н\n    Ауд 17')
					bot.send_message(message.chat.id, '3. НТД в обл.ИТ\n    Ташкинов В.В\n    Ауд 14a | 121')
					break;


					#1418к


				if message.text == '14ОИТ18к понедельник' or message.text == '14оит18к понедельник' or message.text == '14оит18к пн' or message.text == '14ОИТ18к пн':
					bot.send_message(message.chat.id, '1. Приклад.программирование\n    Лукьянова Г.С\n    Ауд 213')
					bot.send_message(message.chat.id, '2. Приклад.программирование\n    Лукьянова Г.С\n    Ауд 213')
					bot.send_message(message.chat.id, '3. БЖД\n    _\n    Ауд 122')
					break;
				if message.text == '14ОИТ18к вторник' or message.text == '14оит18к вторник' or message.text == '14оит18к вт' or message.text == '14ОИТ18к вт':
					bot.send_message(message.chat.id, '1. Приклад.программирование\n    Лукьянова Г.С\n    Ауд 213')
					bot.send_message(message.chat.id, '2. Приклад.программирование\n    Лукьянова Г.С\n    Ауд 213')
					bot.send_message(message.chat.id, '3. физ-ра\n    Лобкова Е.К')
					break;
				if message.text == '14ОИТ18к среда' or message.text == '14оит18к среда' or message.text == '14оит18к ср' or message.text == '14ОИТ18к ср':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. ТСИ\n    Давыдов А.И\n    Ауд 310')
					bot.send_message(message.chat.id, '3. Эл-ты математич.логики\n    _\n    Ауд 309')
					bot.send_message(message.chat.id, '4. Ин. яз\n    Прокоданова Е.Н\n    Ауд 308')
					break; 
				if message.text == '14ОИТ18к четверг' or message.text == '14оит18к четверг' or message.text == '14оит18к чт' or message.text == '14ОИТ18к чт':
					bot.send_message(message.chat.id, '1. Сист.программирование\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '2. Сист.программирование\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '3. ТСИ\n    Давыдов А.И\n    Ауд 310')
					break;
				if message.text == '14ОИТ18к пятница' or message.text == '14оит18к пятница' or message.text == '14оит18к пт' or message.text == '14ОИТ18к пт':
					bot.send_message(message.chat.id, '1. Сист.программирование\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '2. Приклад.программирование\n    Лукьянова Г.С\n    Ауд 213 | 119а')
					bot.send_message(message.chat.id, '3. Эл-ты математич.логики\n    _\n    Ауд 309')
					break;
				if message.text == '14ОИТ18к суббота' or message.text == '14оит18к суббота' or message.text == '14оит18к сб' or message.text == '14ОИТ18к сб':
					bot.send_message(message.chat.id, '1. Сист.программирование\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '2. Сист.программирование\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '3. ТСИ\n    Давыдов А.И\n    Ауд 310')
					break;
                

					#1419


				if message.text == '14ОИТ19 понедельник' or message.text == '14оит19 понедельник' or message.text == '14оит19 пн' or message.text == '14ОИТ19 пн':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '3. Бух.учет\n    Втолина М.И\n    Ауд 103')
					bot.send_message(message.chat.id, '3. Осн.философии\n    Токмакова Л.Ю\n    Ауд 210')
					bot.send_message(message.chat.id, '4. Дискрет.математика\n    Дорофеев Д.В\n    Ауд 104')
					break;
				if message.text == '14ОИТ19 вторник' or message.text == '14оит19 вторник' or message.text == '14оит19 вт' or message.text == '14ОИТ19 вт':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. Разраб.внедр.и адаптац.ПО\n    Давыдова Т.Ю\n    Ауд 310')
					bot.send_message(message.chat.id, '3. Разраб.внедр.и адаптац.ПО\n    Давыдова Т.Ю\n    Ауд 310')
					bot.send_message(message.chat.id, '4. БЖД\n    _\n    Ауд 122')
					break;
				if message.text == '14ОИТ19 среда' or message.text == '14оит19 среда' or message.text == '14оит19 ср' or message.text == '14ОИТ19 ср':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. физ-ра\n    Агапов Н.И')
					bot.send_message(message.chat.id, '3. Бух.учет\n    Втолина М.И\n    Ауд 103')
					bot.send_message(message.chat.id, '4. Разраб.внедр.и адаптац.ПО\n    Давыдова Т.Ю\n    Ауд 310')
					break; 
				if message.text == '14ОИТ19 четверг' or message.text == '14оит19 четверг' or message.text == '14оит19 чт' or message.text == '14ОИТ19 чт':
					bot.send_message(message.chat.id, '1. _')
					bot.send_message(message.chat.id, '2. Разраб.внедр.и адаптац.ПО\n    Давыдова Т.Ю\n    Ауд 310')
					bot.send_message(message.chat.id, '3. Разраб.внедр.и адаптац.ПО\n    Давыдова Т.Ю\n    Ауд 310')
					bot.send_message(message.chat.id, '4. Осн.философии\n    Токмакова Л.Ю\n    Ауд 210')
					break;
				if message.text == '14ОИТ19 пятница' or message.text == '14оит19 пятница' or message.text == '14оит19 пт' or message.text == '14ОИТ19 пт':
					bot.send_message(message.chat.id, '1. Сист.программирование\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '2. Приклад.программирование\n    Лукьянова Г.С\n    Ауд 213 | 119а')
					bot.send_message(message.chat.id, '3. Эл-ты математич.логики\n    _\n    Ауд 309')
					break;
				if message.text == '14ОИТ19 суббота' or message.text == '14оит19 суббота' or message.text == '14оит19 сб' or message.text == '14ОИТ19 сб':
					bot.send_message(message.chat.id, '1. Сист.программирование\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '2. Сист.программирование\n    Инюшкина Т.А\n    Ауд 14г')
					bot.send_message(message.chat.id, '3. ТСИ\n    Давыдов А.И\n    Ауд 310')
					break;

				else:
					bot.send_message(message.chat.id, 'Попробуйте снова')
					break;



				
			



if __name__ == '__main__':
	bot.polling(none_stop=True)
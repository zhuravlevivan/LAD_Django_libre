from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from django.template.response import TemplateResponse

from .models import LibreAuthors

menu = [
	{'title': 'Books', 'url_name': 'books'},
	{'title': 'About', 'url_name': 'about'},
	{'title': 'Add Note', 'url_name': 'add_note'},
	{'title': 'Help', 'url_name': 'help'},
	{'title': 'Sign In', 'url_name': 'sign'},
]

book_db = [
	{'id': 1, 'title': '«Властелин колец»', 'author': 'Джон Р. Р. Толкин', 'country': 'Великобритания', 'content': '''
	«Властели́н коле́ц» (англ. The Lord of the Rings) — роман-эпопея английского писателя Дж. Р. Р. Толкина, одно из самых известных произведений жанра фэнтези. «Властелин колец» был написан как единая книга, но из-за объёма при первом издании его разделили на три части — «Братство Кольца», «Две крепости» и «Возвращение короля». В виде трилогии он публикуется и по сей день, хотя часто в едином томе. Роман считается первым произведением жанра эпическое фэнтези, а также его классикой.
	'''},
	{'id': 2, 'title': '«Гордость и предубеждение»', 'author': 'Джейн Остин', 'country': 'Великобритания', 'content': '''
	«Го́рдость и предубежде́ние» (англ. Pride and Prejudice) — роман Джейн Остин, опубликованный в 1813 году.'''},
	{'id': 3, 'title': '«Тёмные начала»', 'author': 'Филип Пулман', 'country': 'Великобритания', 'content': '''
	«Тёмные начала» (англ. His Dark Materials) — фантастическая трилогия Филипа Пулмана. Включает романы «Северное сияние», «Чудесный нож» и «Янтарный телескоп». В списке 200 лучших книг по версии BBC трилогия занимает третье место.'''},
	{'id': 4, 'title': '«Автостопом по галактике»', 'author': 'Дуглас Адамс', 'country': 'Великобритания', 'content': '''
	«Автосто́пом по гала́ктике» (англ. The Hitchhiker’s Guide to the Galaxy; дословно «Путеводитель по Галактике для автостопщиков», «Путеводитель для путешествующих по Галактике автостопом», 1979) — юмористический фантастический роман английского писателя Дугласа Адамса. Первая книга одноимённой серии.'''},
	{'id': 5, 'title': '«Гарри Поттер и Кубок огня»', 'author': 'Джоан Роулинг', 'country': 'Великобритания', 'content': '''
	Га́рри По́ттер и Ку́бок огня́ (англ. Harry Potter and the Goblet of Fire) — четвёртая книга о приключениях Гарри Поттера, написанная английской писательницей Джоан Роулинг. В Англии опубликована в 2000 году. По сюжету Гарри Поттер против своей воли вовлекается в участие в Турнире Трёх Волшебников, и ему предстоит не только сразиться с более опытными участниками, но и разгадать загадку того, как он вообще попал на турнир вопреки правилам. Книга получила премию «Хьюго» в 2001 году[1]. В 2005 году вышел одноимённый фильм, режиссёр — Майк Ньюэлл.'''},
	{'id': 6, 'title': '«Убить пересмешника»', 'author': 'Харпер Ли', 'country': 'США', 'content': '''
	«Уби́ть пересме́шника» (англ. To Kill a Mockingbird) — роман-бестселлер[2][3] американской писательницы Харпер Ли, опубликованный в 1960 году, за который в 1961 году она получила Пулитцеровскую премию. Её успех стал вехой в борьбе за права чернокожих.'''},
	{'id': 7, 'title': '«Винни Пух»', 'author': 'Алан Александр Милн', 'country': 'Великобритания', 'content': ''''''},
	{'id': 8, 'title': '«1984»', 'author': 'Джордж Оруэлл', 'country': 'Великобритания', 'content': ''''''},
	{'id': 9, 'title': '«Лев, колдунья и платяной шкаф»', 'author': 'Клайв Стэйплз Льюис', 'country': 'Великобритания', 'content': ''''''},
	{'id': 10, 'title': '«Джейн Эйр»', 'author': 'Шарлотта Бронте', 'country': 'Великобритания', 'content': ''''''},
	{'id': 11, 'title': '«Уловка-22»', 'author': 'Джозеф Хеллер', 'country': 'США', 'content': ''''''},
	{'id': 12, 'title': '«Грозовой перевал»', 'author': 'Эмили Бронте', 'country': 'Великобритания', 'content': ''''''},
	{'id': 13, 'title': '«Пение птиц»', 'author': 'Себастьян Фолкс', 'country': 'Великобритания', 'content': ''''''},
	{'id': 14, 'title': '«Ребекка»', 'author': 'Дафна Дюморье', 'country': 'Великобритания', 'content': ''''''},
	{'id': 15, 'title': '«Над пропастью во ржи»', 'author': 'Джером Сэлинджер', 'country': 'США', 'content': ''''''},

]


def index(request):
	# books_db = LibreAuthors.objects.all()
	data = {'menu': menu, 'books': book_db, }
	return render(request, "libre_authors/index.html", context=data)


def authors(request, book_authors='Not Set'):  # http://127.0.0.1:8000/authors/?a=Shultz&book=Python
	a = request.GET.get('a', book_authors)
	book = request.GET.get('book', 'No Book')
	output = '<h3>Author Name: {0}<br>Book: {1}</h3>'.format(a, book)
	return HttpResponse(output)


def books(request):
	books_db = LibreAuthors.objects.filter(is_published=1)
	data = {'menu': menu, 'books': book_db, }
	return render(request, "libre_authors/books.html", context=data)


# return TemplateResponse(request, 'libre_authors/books.html')


def show_book(request, book_id):
	book = get_object_or_404(LibreAuthors, pk=book_id)

	data = {
		'title': book.title,
		'menu': menu,
		'book': book,

	}

	# return HttpResponse(f'Show Book with ID = {book_slug}')
	return render(request, 'libre_authors/book.html', data)


def about(request):
	data = {'menu': menu, }
	return TemplateResponse(request, 'libre_authors/about.html', context=data)


def add_note(request):
	return HttpResponse('Add note page')


def help_page(request):
	return HttpResponse('Help page')


def sign_in(request):
	return HttpResponse('Sign in page')


def page_not_found(request, exception):
	return HttpResponseNotFound('<h1>Страница не найдена</h1>')

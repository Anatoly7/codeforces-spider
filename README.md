# codeforces-spider
Public scrapy spider for codeforces parsing
Проверка списка хэндлов на участие в раундах codeforces

1. Нужен python 3.4 и выше
2. Нужен фреймворк scrapy
3. Перейти в папку проекта
4. Внутри этой папки(через консоль) запустите команду

scrapy crawl cfspider
	
5. Все данные, связанные с парсингом хранятся в tutorial/info
	
to_check.txt - список хэндлов, которые нужно проверить на участие в раунде

s_url.txt - ссылка формата "https://codeforces.com/contest/9999" на проверяемый контест

result.txt - набор хэндлов, которые участвовали в раунде официально
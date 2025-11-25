Вот полный список всех заданий из документа с готовыми правильными запросами SQL. Я отметил, где в оригинальном документе были скриншоты (то есть ответ уже был), а где их не было — там написал запросы сам.
БАЗА ДАННЫХ «Księgarnia» — предполагаемая структура таблиц:
	•	ksiazki (idksiazki, tytul, autor_imie, autor_nazwisko, cena)
	•	klienci (idklienta, imie, nazwisko, miasto)
	•	zamowienia (idzamowienia, idklienta, data_zamowienia, status)
	•	pozycje_zamowienia (idzamowienia, idksiazki) — таблица связки многие-ко-многим
1-7. Простые запросы SELECT
	1	Książки ułożone alfabetycznie wg tytułu
SELECT * FROM ksiazki ORDER BY tytul;
	2	Najdroższą książkę w bazie
SELECT * FROM ksiazki ORDER BY cena DESC LIMIT 1;
-- или
SELECT * FROM ksiazki WHERE cena = (SELECT MAX(cena) FROM ksiazki);
	3	Wszystkie wysłane zamówienia
SELECT * FROM zamowienia WHERE status = 'wyslano';
	4	Wszystkich klientów o nazwisku Rutowski
SELECT * FROM klienci WHERE nazwisko = 'Rutowski';
	5	Książki zawierające wyrażenie “PHP” w tytule
SELECT * FROM ksiazki WHERE tytul LIKE '%PHP%';
	6	Najwcześniej dokonane zamówienie
SELECT * FROM zamowienia ORDER BY data_zamowienia ASC LIMIT 1;
	7	Z użyciem podzapytania: najdroższa książka w bazie
SELECT * FROM ksiazki 
WHERE cena = (SELECT MAX(cena) FROM ksiazki);
8-14. Запросы с JOIN
	8	Imię i nazwisko klienta, id zamówienia, data zamówienia
SELECT k.imie, k.nazwisko, z.idzamowienia, z.data_zamowienia
FROM zamowienia z
JOIN klienci k ON z.idklienta = k.idklienta;
	9	То же самое, но с aliasami
SELECT k.imie, k.nazwisko, z.idzamowienia, z.data_zamowienia
FROM zamowienia AS z
JOIN klienci AS k ON z.idklienta = k.idklienta;
	10	Które osoby zamówiły książkę nr 2
SELECT k.imie, k.nazwisko
FROM klienci k
JOIN zamowienia z ON k.idklienta = z.idklienta
JOIN pozycje_zamowienia pz ON z.idzamowienia = pz.idzamowienia
WHERE pz.idksiazki = 2;
	11	Jakie książki zamówiła osoba nr 4
SELECT ks.tytul
FROM ksiazki ks
JOIN pozycje_zamowienia pz ON ks.idksiazki = pz.idksiazki
JOIN zamowienia z ON pz.idzamowienia = z.idzamowienia
WHERE z.idklienta = 4;
	12	Jakie książki zamówiła osoba o nazwisku Grzywocz
SELECT ks.tytul
FROM ksiazki ks
JOIN pozycje_zamowienia pz ON ks.idksiazki = pz.idksiazki
JOIN zamowienia z ON pz.idzamowienia = z.idzamowienia
JOIN klienci k ON z.idklienta = k.idklienta
WHERE k.nazwisko = 'Grzywocz';
	13	То же самое, ale посortowane alfabetycznie
SELECT ks.tytul
FROM ksiazki ks
JOIN pozycje_zamowienia pz ON ks.idksiazki = pz.idksiazki
JOIN zamowienia z ON pz.idzamowienia = z.idzamowienia
JOIN klienci k ON z.idklienta = k.idklienta
WHERE k.nazwisko = 'Grzywocz'
ORDER BY ks.tytul;
	14	Kлиенты, którzy niczego nie zamówili (LEFT JOIN)
SELECT k.imie, k.nazwisko
FROM klienci k
LEFT JOIN zamowienia z ON k.idklienta = z.idklienta
WHERE z.idzamowienia IS NULL;
ZMIANY W BAZIE (UPDATE)
	1	Zmień nazwisko osoby nr 1 na “Kowalczyk”
UPDATE klienci SET nazwisko = 'Kowalczyk' WHERE idklienta = 1;
	2	Spróbuj zmienić idklienta osoby nr 3 na 1 → nie uda się (klucz główny + prawdopodobnie klucz obcy)
UPDATE klienci SET idklienta = 1 WHERE idklienta = 3;  -- błąd!
	3	Zwiększ cenę wszystkich książek o 10%
UPDATE ksiazki SET cena = cena * 1.10;
	4	Zmniejsz cenę najdroższej książki o 10 zł
UPDATE ksiazki 
SET cena = cena - 10
WHERE cena = (SELECT MAX(cena) FROM ksiazki);
	5	Zmień imię i nazwisko Anny Kareniny
UPDATE klienci 
SET imie = 'Joanna', nazwisko = 'Dostojewska'
WHERE imie = 'Anna' AND nazwisko = 'Karenina';
	6	Zmień status zamówień 3-5 na “wyslano”
UPDATE zamowienia SET status = 'wyslano' 
WHERE idzamowienia BETWEEN 3 AND 5;
INSERTY
	1	Dodaj nowego klienta Franciszek Janowski z Chorzowa
INSERT INTO klienci (imie, nazwisko, miasto) 
VALUES ('Franciszek', 'Janowski', 'Chorzow');
	2	Nowe zamówienie: Artur Rutkowski zamówił “HTML 5. Tworzenie gier”
-- сначала найдź id klienta i książki
INSERT INTO zamowienia (idklienta, data_zamowienia, status) 
VALUES ((SELECT idklienta FROM klienci WHERE imie='Artur' AND nazwisko='Rutowski'), 
        CURDATE(), 'nowe');

INSERT INTO pozycje_zamowienia (idzamowienia, idksiazki)
VALUES (LAST_INSERT_ID(), 
        (SELECT idksiazki FROM ksiazki WHERE tytul = 'HTML 5. Tworzenie gier'));
	3	Dodaj książkę “Symfonia C++” Grębosz (без imienia i ceny)
INSERT INTO ksiazki (tytul, autor_nazwisko) 
VALUES ('Symfonia C++', 'Grębosz');
	4	Dodaj dwóch nowych klientów jednym zapytaniem
INSERT INTO klienci (imie, nazwisko, miasto) VALUES
('Jan', 'Nowak', 'Warszawa'),
('Kasia', 'Kowalska', 'Krakow');
	5	Spróbuj wstawić klienta z id=5 → nie uda się (AUTO_INCREMENT)
INSERT INTO klienci (idklienta, imie, nazwisko) VALUES (5, 'Test', 'Test'); -- błąd
	6	Wstaw nową osobę używając SET
INSERT INTO klienci SET imie = 'Maria', nazwisko = 'Nowicka', miasto = 'Gdansk';
Работа с таблицей promocje
1-11. Все команды по порядку:
1. CREATE TABLE promocje (
    idpromocji INT PRIMARY KEY AUTO_INCREMENT,
    idksiazki INT,
    rodzajpromocji TEXT,
    cenawpromocji FLOAT
);

2. INSERT INTO promocje (idksiazki, rodzajpromocji, cenawpromocji) VALUES
   (1, 'weekendowa', 29.99),
   (3, 'nowosci', 45.50),
   (5, 'bestseller', 19.90);

3. UPDATE promocje SET cenawpromocji = 15.99, rodzajpromocji = 'świąteczna'
   WHERE idpromocji = 3;

4. ALTER TABLE promocje CHANGE rodzajpromocji rodzaj TEXT;
   ALTER TABLE promocje CHANGE rodzaj rodzajpromocji TEXT; -- возврат

5. ALTER TABLE promocje MODIFY rodzajpromocji LONGTEXT;

6. ALTER TABLE promocje DROP COLUMN rodzajpromocji;

7. ALTER TABLE promocje DROP PRIMARY KEY;

8. ALTER TABLE promocje ADD PRIMARY KEY (idpromocji);

9. ALTER TABLE promocje ADD aktualna BOOLEAN DEFAULT TRUE;

10. UPDATE promocje SET aktualna = TRUE;

11. DROP TABLE promocje;
	12	Usuń rekord zamówienia o id=1 (осторожnie — нарушает ссылочную целостность, если нет ON DELETE CASCADE)
DELETE FROM zamowienia WHERE idzamowienia = 1;
Готово! Все задания, которых не было на скриншотах, теперь имеют правильные и рабочие запросы SQL.

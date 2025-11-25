Zadania SQL – Księgarnia
Pełne rozwiązania wszystkich zadań z dokumentu (w formacie Markdown)
Struktura bazy (dla orientacji)
	•	ksiazki (idksiazki, tytul, autor_imie, autor_nazwisko, cena)
	•	klienci (idklienta PK AUTO_INCREMENT, imie, nazwisko, miasto)
	•	zamowienia (idzamowienia PK AUTO_INCREMENT, idklienta, data_zamowienia, status)
	•	pozycje_zamowienia (idzamowienia, idksiazki) – tabela łącząca

1–7. Proste zapytania SELECT
Nr
Zadanie
Zapytanie SQL
1
Książki alfabetycznie wg tytułu
SELECT * FROM ksiazki ORDER BY tytul;
2
Najdroższa książka
SELECT * FROM ksiazki ORDER BY cena DESC LIMIT 1;
3
Wszystkie wysłane zamówienia
SELECT * FROM zamowienia WHERE status = 'wyslano';
4
Klienci o nazwisku Rutowski
SELECT * FROM klienci WHERE nazwisko = 'Rutowski';
5
Książki z „PHP” w tytule
SELECT * FROM ksiazki WHERE tytul LIKE '%PHP%';
6
Najwcześniejsze zamówienie
SELECT * FROM zamowienia ORDER BY data_zamowienia ASC LIMIT 1;
7
Najdroższa książka – z podzapytaniem
SELECT * FROM ksiazki WHERE cena = (SELECT MAX(cena) FROM ksiazki);
8–14. Zapytania z JOIN
Nr
Zadanie
Zapytanie SQL
8
Imię, nazw039;isko klienta + id i data zamówienia
sql
SELECT k.imie, k.nazwisko, z.idzamowienia, z.data_zamowienia
FROM zamowienia z
JOIN klienci k ON z.idklienta = k.idklienta;
9
Jak wyżej, ale z aliasami
sql
SELECT k.imie, k.nazwisko, z.idzamowienia, z.data_zamowienia
FROM zamowienia AS z
JOIN klienci AS k ON z.idklienta = k.idklienta;
10
Kto zamówił książkę nr 2
sql
SELECT k.imie, k.nazwisko
FROM klienci k
JOIN zamowienia z ON k.idklienta = z.idklienta
JOIN pozycje_zamowienia pz ON z.idzamowienia = pz.idzamowienia
WHERE pz.idksiazki = 2;
11
Jakie książki zamówiła osoba nr 4
sql
SELECT ks.tytul
FROM ksiazki ks
JOIN pozycje_zamowienia pz ON ks.idksiazki = pz.idksiazki
JOIN zamowienia z ON pz.idzamowienia = z.idzamowienia
WHERE z.idklienta = 4;
12
Jakie książki zamówiła osoba o nazwisku Grzywocz
sql
SELECT ks.tytul
FROM ksiazki ks
JOIN pozycje_zamowienia pz ON ks.idksiazki = pz.idksiazki
JOIN zamowienia z ON pz.idzamowienia = z.idzamowienia
JOIN klienci k ON z.idklienta = k.idklienta
WHERE k.nazwisko = 'Grzywocz';
13
Jak wyżej + posortowane alfabetycznie
(to samo zapytanie co w 12) ORDER BY ks.tytul;
14
Klienci, którzy nic nie zamówili (LEFT JOIN)
sql
SELECT k.imie, k.nazwisko
FROM klienci k
LEFT JOIN zamowienia z ON k.idklienta = z.idklienta
WHERE z.idzamowienia IS NULL;
UPDATE – zmiany w bazie
Nr
Zadanie
Zapytanie SQL
1
Zmień nazwisko osoby nr 1 na Kowalczyk
UPDATE klienci SET nazwisko = 'Kowalczyk' WHERE idklienta = 1;
2
Spróbuj zmienić idklienta osoby nr 3 na 1 → błąd (klucz główny/obcy)
UPDATE klienci SET idklienta = 1 WHERE idklienta = 3;
3
Zwiększ cenę wszystkich książek o 10%
UPDATE ksiazki SET cena = cena * 1.10;
4
Zmniejsz cenę najdroższej książki o 10 zł
sql
UPDATE ksiazki
SET cena = cena - 10
WHERE cena = (SELECT MAX(cena) FROM ksiazki);
5
Anna Karenina → Joanna Dostojewska
UPDATE klienci SET imie = 'Joanna', nazwisko = 'Dostojewska' WHERE imie = 'Anna' AND nazwisko = 'Karenina';
6
Status zamówień 3–5 na „wyslano”
UPDATE zamowienia SET status = 'wyslano' WHERE idzamowienia BETWEEN 3 AND 5;
INSERT – wstawianie danych
Nr
Zadanie
Zapytanie SQL
1
Nowy klient: Franciszek Janowski, Chorzów
INSERT INTO klienci (imie, nazwisko, miasto) VALUES ('Franciszek', 'Janowski', 'Chorzow');
2
Artur Rutkowski zamówił „HTML 5. Tworzenie gier”
sql
INSERT INTO zamowienia (idklienta, data_zamowienia, status)
VALUES ((SELECT idklienta FROM klienci WHERE imie='Artur' AND nazwisko='Rutowski'), CURDATE(), 'nowe');

INSERT INTO pozycje_zamowienia (idzamowienia, idksiazki)
VALUES (LAST_INSERT_ID(), (SELECT idksiazki FROM ksiazki WHERE tytul LIKE 'HTML 5. Tworzenie gier%'));
3
Książka „Symfonia C++” autor Grębosz (bez imienia i ceny)
INSERT INTO ksiazki (tytul, autor_nazwisko) VALUES ('Symfonia C++', 'Grębosz');
4
Dwóch klientów jednym zapytaniem
INSERT INTO klienci (imie, nazwisko, miasto) VALUES ('Jan','Nowak','Warszawa'), ('Kasia','Kowalska','Krakow');
5
Wstaw klienta z ręcznym id=5 → błąd (AUTO_INCREMENT)
INSERT INTO klienci (idklienta, imie, nazwisko) VALUES (5,'Test','Test');
6
Wstaw osobę używając składni SET
INSERT INTO klienci SET imie='Maria', nazwisko='Nowicka', miasto='Gdansk';
Tabela „promocje” – wszystkie operacje DDL/DML
-- 1. Utworzenie tabeli
CREATE TABLE promocje (
    idpromocji INT PRIMARY KEY AUTO_INCREMENT,
    idksiazki INT,
    rodzajpromocji TEXT,
    cenawpromocji FLOAT
);

-- 2. Trzy rekordy jednym INSERTem
INSERT INTO promocje (idksiazki, rodzajpromocji, cenawpromocji) VALUES
(1, 'weekendowa', 29.99),
(3, 'nowosci', 45.50),
(5, 'bestseller', 19.90);

-- 3. Zmiana trzeciej promocji
UPDATE promocje 
SET cenawpromocji = 15.99, rodzajpromocji = 'świąteczna'
WHERE idpromocji = 3;

-- 4. Zmiana nazwy kolumny i powrót
ALTER TABLE promocje CHANGE rodzajpromocji rodzaj TEXT;
ALTER TABLE promocje CHANGE rodzaj rodzajpromocji TEXT;

-- 5. Zmiana typu na LONGTEXT
ALTER TABLE promocje MODIFY rodzajpromocji LONGTEXT;

-- 6. Usunięcie kolumny
ALTER TABLE promocje DROP COLUMN rodzajpromocji;

-- 7. Usunięcie klucza głównego
ALTER TABLE promocje DROP PRIMARY KEY;

-- 8. Ponowne dodanie klucza głównego
ALTER TABLE promocje ADD PRIMARY KEY (idpromocji);

-- 9. Nowa kolumna boolean
ALTER TABLE promocje ADD aktualna BOOLEAN DEFAULT TRUE;

-- 10. Ustawienie TRUE we wszystkich rekordach
UPDATE promocje SET aktualna = TRUE;

-- 11. Usunięcie całej tabeli
DROP TABLE promocje;
Ostatnie polecenie
-- 12. Usuń zamówienie o id=1 (uwaga na klucze obce!)
DELETE FROM zamowienia WHERE idzamowienia = 1;
Gotowe! Wszystkie zadania (takie, które miały tylko zdjęcia, jak i te bez odpowiedzi) są teraz uzupełnione czytelnymi, działającymi zapytaniami SQL w formacie Markdown.

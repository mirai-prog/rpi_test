1 SELECT * FROM ksiazki ORDER BY tytul;
2 SELECT * FROM ksiazki ORDER BY cena DESC LIMIT 1;
3 SELECT * FROM zamowienia WHERE status = ‘wyslano’;
4 SELECT * FROM klienci WHERE nazwisko = ‘Rutowski’;
5 SELECT * FROM ksiazki WHERE tytul LIKE ‘%PHP%’;
6 SELECT * FROM zamowienia ORDER BY data_zamowienia ASC LIMIT 1;
7 SELECT * FROM ksiazki WHERE cena = (SELECT MAX(cena) FROM ksiazki);
8 SELECT k.imie, k.nazwisko, z.idzamowienia, z.data_zamowienia FROM zamowienia z JOIN klienci k ON z.idklienta = k.idklienta;
9 SELECT k.imie, k.nazwisko, z.idzamowienia, z.data_zamowienia FROM zamowienia AS z JOIN klienci AS k ON z.idklienta = k.idklienta;
10 SELECT k.imie, k.nazwisko FROM klienci k JOIN zamowienia z ON k.idklienta = z.idklienta JOIN pozycje_zamowienia pz ON z.idzamowienia = pz.idzamowienia WHERE pz.idksiazki = 2;
11 SELECT ks.tytul FROM ksiazki ks JOIN pozycje_zamowienia pz ON ks.idksiazki = pz.idksiazki JOIN zamowienia z ON pz.idzamowienia = z.idzamowienia WHERE z.idklienta = 4;
12 SELECT ks.tytul FROM ksiazki ks JOIN pozycje_zamowienia pz ON ks.idksiazki = pz.idksiazki JOIN zamowienia z ON pz.idzamowienia = z.idzamowienia JOIN klienci k ON z.idklienta = k.idklienta WHERE k.nazwisko = ‘Grzywocz’;
13 SELECT ks.tytul FROM ksiazki ks JOIN pozycje_zamowienia pz ON ks.idksiazki = pz.idksiazki JOIN zamowienia z ON pz.idzamowienia = z.idzamowienia JOIN klienci k ON z.idklienta = k.idklienta WHERE k.nazwisko = ‘Grzywocz’ ORDER BY ks.tytul;
14 SELECT k.imie, k.nazwisko FROM klienci k LEFT JOIN zamowienia z ON k.idklienta = z.idklienta WHERE z.idzamowienia IS NULL;
UPDATE 1 UPDATE klienci SET nazwisko = ‘Kowalczyk’ WHERE idklienta = 1;
UPDATE 2 UPDATE klienci SET idklienta = 1 WHERE idklienta = 3; – błąd
UPDATE 3 UPDATE ksiazki SET cena = cena * 1.10;
UPDATE 4 UPDATE ksiazki SET cena = cena - 10 WHERE cena = (SELECT MAX(cena) FROM ksiazki);
UPDATE 5 UPDATE klienci SET imie = ‘Joanna’, nazwisko = ‘Dostojewska’ WHERE imie = ‘Anna’ AND nazwisko = ‘Karenina’;
UPDATE 6 UPDATE zamowienia SET status = ‘wyslano’ WHERE idzamowienia BETWEEN 3 AND 5;
INSERT 1 INSERT INTO klienci (imie, nazwisko, miasto) VALUES (‘Franciszek’, ‘Janowski’, ‘Chorzow’);
INSERT 2 INSERT INTO zamowienia (idklienta, data_zamowienia, status) VALUES ((SELECT idklienta FROM klienci WHERE imie=‘Artur’ AND nazwisko=‘Rutowski’), CURDATE(), ‘nowe’); INSERT INTO pozycje_zamowienia (idzamowienia, idksiazki) VALUES (LAST_INSERT_ID(), (SELECT idksiazki FROM ksiazki WHERE tytul = ‘HTML 5. Tworzenie gier’));
INSERT 3 INSERT INTO ksiazki (tytul, autor_nazwisko) VALUES (‘Symfonia C++’, ‘Grębosz’);
INSERT 4 INSERT INTO klienci (imie, nazwisko, miasto) VALUES (‘Jan’,‘Nowak’,‘Warszawa’), (‘Kasia’,‘Kowalska’,‘Krakow’);
INSERT 5 INSERT INTO klienci (idklienta, imie, nazwisko) VALUES (5,‘Test’,‘Test’); – błąd
INSERT 6 INSERT INTO klienci SET imie=‘Maria’, nazwisko=‘Nowicka’, miasto=‘Gdansk’;
PROMOCJE 1 CREATE TABLE promocje (idpromocji INT PRIMARY KEY AUTO_INCREMENT, idksiazki INT, rodzajpromocji TEXT, cenawpromocji FLOAT);
PROMOCJE 2 INSERT INTO promocje (idksiazki, rodzajpromocji, cenawpromocji) VALUES (1,‘weekendowa’,29.99), (3,‘nowosci’,45.50), (5,‘bestseller’,19.90);
PROMOCJE 3 UPDATE promocje SET cenawpromocji = 15.99, rodzajpromocji = ‘świąteczna’ WHERE idpromocji = 3;
PROMOCJE 4 ALTER TABLE promocje CHANGE rodzajpromocji rodzaj TEXT; ALTER TABLE promocje CHANGE rodzaj rodzajpromocji TEXT;
PROMOCJE 5 ALTER TABLE promocje MODIFY rodzajpromocji LONGTEXT;
PROMOCJE 6 ALTER TABLE promocje DROP COLUMN rodzajpromocji;
PROMOCJE 7 ALTER TABLE promocje DROP PRIMARY KEY;
PROMOCJE 8 ALTER TABLE promocje ADD PRIMARY KEY (idpromocji);
PROMOCJE 9 ALTER TABLE promocje ADD aktualna BOOLEAN DEFAULT TRUE;
PROMOCJE 10 UPDATE promocje SET aktualna = TRUE;
PROMOCJE 11 DROP TABLE promocje;
PROMOCJE 12 DELETE FROM zamowienia WHERE idzamowienia = 1;

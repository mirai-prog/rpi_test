<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <title>Ważenie samochodów ciężarowych</title>
    <link rel="stylesheet" href="styl.css">
    <meta http-equiv="refresh" content="10">
</head>
<body>
    <header>
        <h1>Ważenie pojazdów we Wrocławiu</h1>
    </header>
    <header>
        <img src="obraz1.png" alt="waga">
    </header>

    <aside>
        <h2>Lokalizacje wag</h2>
        <ol>
            <?php
            $db = mysqli_connect('localhost', 'root', '', 'wazenietirow');
            // Skrypt 1
            $q2 = "SELECT ulica FROM lokalizacje;";
            $res2 = mysqli_query($db, $q2);
            while($row = mysqli_fetch_array($res2)) {
                echo "<li>ulica " . $row['ulica'] . "</li>";
            }
            ?>
        </ol>
        <h2>Kontakt</h2>
        <a href="mailto:wazenie@wroclaw.pl">napisz</a>
    </aside>

    <main>
        <h2>Alerty</h2>
        <table>
            <tr>
                <th>rejestracja</th>
                <th>ulica</th>
                <th>waga</th>
                <th>dzień</th>
                <th>czas</th>
            </tr>
            <?php
            // Skrypt 3 (wykonuje się przed 2, aby nowa dana była w tabeli)
            $q3 = "INSERT INTO wagi (lokalizacje_id, waga, rejestracja, dzien, czas) VALUES (5, FLOOR(1 + RAND() * 10), 'DW12345', CURDATE(), CURTIME());";
            mysqli_query($db, $q3);

            // Skrypt 2
            $q4 = "SELECT wagi.rejestracja, lokalizacje.ulica, wagi.waga, wagi.dzien, wagi.czas FROM wagi JOIN lokalizacje ON wagi.lokalizacje_id = lokalizacje.id WHERE wagi.waga > 5;";
            $res4 = mysqli_query($db, $q4);
            while($row = mysqli_fetch_array($res4)) {
                echo "<tr>
                        <td>{$row['rejestracja']}</td>
                        <td>{$row['ulica']}</td>
                        <td>{$row['waga']}</td>
                        <td>{$row['dzien']}</td>
                        <td>{$row['czas']}</td>
                      </tr>";
            }
            mysqli_close($db);
            ?>
        </table>
    </main>

    <section>
        <img src="obraz2.jpg" alt="tir">
    </section>

    <footer>
        <p>Stronę wykonał: [Twój_PESEL]</p>
    </footer>
</body>
</html>

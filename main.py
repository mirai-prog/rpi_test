function zadania() {
  let wybor = parseInt(prompt("Wybierz zadanie (1-8):"));

  switch (wybor) {
    case 1:
      // 1. 10 kolejnych liczb całkowitych od 1
      for (let i = 1; i <= 10; i++) console.log(i);
      break;

    case 2:
      // 2. 10 kolejnych liczb całkowitych od 10 malejąco
      for (let i = 10; i >= 1; i--) console.log(i);
      break;

    case 3:
      // 3. Suma kolejnych 10 liczb od 1
      let suma = 0;
      for (let i = 1; i <= 10; i++) suma += i;
      console.log("Suma =", suma);
      break;

    case 4:
      // 4. 10 liczb parzystych od 2
      for (let i = 2; i <= 20; i += 2) console.log(i);
      break;

    case 5:
      // 5. Suma 100 elementów ciągu arytmetycznego (a1=5, d=10)
      let sumaCiagu = 0;
      let a = 5;
      for (let i = 0; i < 100; i++) sumaCiagu += a + i * 10;
      console.log("Suma ciągu =", sumaCiagu);
      break;

    case 6:
      // 6. Silnia liczby
      let n = parseInt(prompt("Podaj liczbę:"));
      let silnia = 1;
      for (let i = 1; i <= n; i++) silnia *= i;
      console.log(n + "! =", silnia);
      break;

    case 7:
      // 7. Ciąg n liczb, każda kolejna to kwadrat poprzedniej
      let ile = parseInt(prompt("Podaj ilość elementów:"));
      let pierwsza = parseInt(prompt("Podaj pierwszą liczbę:"));
      let liczba = pierwsza;
      for (let i = 0; i < ile; i++) {
        console.log(liczba);
        liczba = liczba ** 2;
      }
      break;

    case 8:
      // 8. Suma i średnia 10 losowych liczb z przedziału 50-100
      let sumaLos = 0;
      for (let i = 0; i < 10; i++) {
        let los = Math.floor(Math.random() * 51) + 50;
        console.log(los);
        sumaLos += los;
      }
      let srednia = sumaLos / 10;
      console.log("Suma =", sumaLos);
      console.log("Średnia =", srednia);
      break;

    default:
      console.log("Nie ma takiego zadania!");
  }
}

zadania();
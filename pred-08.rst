=============
Predavanja 08
=============


Značaj praćenja metrika u kontekstu cloud computing-a
=====================================================

- ako nešto *ne merimo*, kako ćemo to *optimizovati* (data/metric driven workflow)?
- interesantne stvari za monitoring/praćenje:

  - utrošak računarskih/mrežnih resursa
  - odziv sistema, u normalnim okolnostima
  - odziv sistema, u vanrednim okolnostima (flash-sale, D/DOS napadi, memory/disk swapping, ...)
  - vremenski lag za elastični scale in/out
  - operativni troškovi, ako koristimo elastični scale in/out (a koliko će onda da nas košta D/DOS napad?)
  - maksimalni stepen opterećenja koje naš sistem može da izdrži

- jako je bitno pratiti ne samo sirove metrike - veći i njihov *istoriski kontekst*, tj. istoriju promena


Upotreba Django razvojnog okvira za brz razvoj modernih web aplikacija [nastavak]
=================================================================================

- razvoj jednostavne home page stranice koja će *dodatno* da ispiše:

  - visit counter, iz baze podataka

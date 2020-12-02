=============
Predavanja 02
=============


Prednosti i mane cloud computing-a
==================================

- mi ne moramo da brinemo o infrastrukturi

  - ali možda je bolje rečeno, da **nema koristi** da brinemo o infrastrukturi (mi se ništa tu ne pitamo)
  - otkaz jednog ključnog servisa cloud service providera može dovesti do kaskadnih grešaka koje sruše sve njegove servise

- u odnosu na iznajmljivanje dedicated servera (npr. Telekom, SBB, Hetzner):

  - **CENA**, obavezno uvek sračunajte TCO
  - mi uvek moramo da platimo ceo mesec za dedicated server, čak iako ga koristimo samo mali deo vremena (npr. "noćni režim" poseta)
  - overprovision vs underprovision, šta je gore po nas?

    - popularnost naših servisa/sajtova se menja tokom godine (npr. kolokvijumi, praznici, specijalne akcije, godišnji odmori)
    - popularnost naših servisa/sajtova se menja tokom nedelje (npr. više/manje popularni vikendom)
    - popularnost naših servisa/sajtova se menja tokom dana (npr. više/manje popularni danju/noću)


Šta je to virtuelizacija i motivacija za upotrebu?
==================================================

- virtuelizacija/apstrakcija hardvera
- pravimo računar u računaru (u računaru, u računaru, ...)
- izolacija računarskih resursa: host - vm guest
- isprobavanje loše napisanih (ili potencijalno malicioznih programa) na bezbedan način - bez uticaja na host računar
- rad sa legacy projektima, koji koriste matore verzije alata, biblioteka ili programskih jezika
- šta se dešava u vm guest, je *uglavnom* sakriveno (crna kutija) za vm host: prednost i/ili mana?

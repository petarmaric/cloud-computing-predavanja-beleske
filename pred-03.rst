=============
Predavanja 03
=============


Šta je to virtuelizacija i motivacija za upotrebu? [nastavak]
=============================================================

- **NASTAVAK**, krenuli smo da se igramo sa virtualbox i kreiranjem VM-a
- na predavanjima je većinom ručni rad, sa Jelenom na vežbama je automatizacija

Motivacija sa strane operations-a, tj. service/server provider-a
----------------------------------------------------------------

- možemo našem kupcu servera/servisa da iznajmimo ceo fizički server

  - pojedinačna cena je veća, konkurentnost?
  - jedan fizički server se može iznajmiti samo jednom kupcu (u jednom trenutku)
  - za svakog kupca nam treba dodatni fizički prostor u data centru - kao i struja, hlađenje, ...

- možemo našem kupcu servera/servisa da iznajmimo jedan deo fizičkog servera - kao tzv. shared hosting (npr. putem SSH)

  - jedan fizički server se može iznajmiti ka više kupaca
  - pojedinačna cena jeste manja (ljudi su voljni da plate manje za manji VPS), ali zbirno (na nivou servera) zarada može biti značajno veća
  - deljenje resursa (ali i bezbednost), "nevaljali" korisnik može drugima da napravi problem
  - još veći profit, ako se odlučimo za overselling (jednu "istu" stvar možemo prodati do 20, pa i 50 puta). Užasnimo se nad time što radi DreamHost npr: ``ssh petarmaric.com wc -l /etc/passwd``
  - efikasno pakovanje korisnika na fizički server - preteraj sa brojem korisnika, pa ako se neko želi prebaci ga na manje opterećen server
  - svi korisnici *obično* moraju da dele istu verziju softvera (zarad manjeg utroška RAM-a i diska): PHP, Apache, nginx, Python, Ruby

- možemo našem kupcu servera/servisa da iznajmimo jedan deo fizičkog servera - kao tzv. VPS (virtual private server)

  - jedan fizički server se može iznajmiti ka više kupaca
  - pojedinačna cena jeste manja (ljudi su voljni da plate manje za manji VPS), ali zbirno (na nivou servera) zarada može biti značajno veća
  - efikasno pakovanje korisnika/VPS-ova na fizički server (da ne bude neiskorišćenih "rupa" koje se ne mogu iskoristiti)
  - problem automatizacije, šta se dešava kada korisnik želi za sebe više RAM-a (a da ga nema na VM hostu)
  - za svakog kupca moram "vrteti" po svaki put sve komponente operativnog sistema (npr. kernel) što "baca" RAM
  - obično iznajmljujemo VPS kupcu na mesečnom nivou

- možemo našem kupcu servera/servisa da iznajmimo jedan deo fizičkog servera - kao cloud instancu

  - mala razlika u odnosu na VPS, sa strane service providera
  - najbitnije je što sada naši korisnici imaju API za pristup, traženje i upravljanje računarskim resursima (npr. cloud instancama)
  - **automatizacija svega**, koja mora da postoji i bude jako dobra po prirodi problema
  - zvuči "cool" što smo cloud-enabled
  - obično možemo da tražimo veću cenu u odnosu na VPS, zato što smo "cool"
  - obično iznajmljujemo cloud instancu kupcu na minut ili sat

- možemo našem kupcu servera/servisa da iznajmimo jedan deo fizičkog servera - kao "serverless" container

  - *UVEK* postoji server/CPU na kome se izvršava kod, samo je pitanje da li to interesuje našeg krajnjeg kupca
  - zvuči "cool" što smo cloud-native
  - obično možemo da tražimo *JOŠ* veću cenu u odnosu na ranije, jer je ovo premium usluga
  - monogo je efikasnije pakovanje korisnika i njihovih "kontejnera", pošto kontejner sadrži samo lib/app a ostatak operativnog sistema dele svi korisnici
  - visoka efikasnost utroška diska na serveru, pošto Docker organizuje (i kešira) svoje container/image u tzv. slojeve - tako da se slojevi mogu deliti između svih korisnika na tom serveru
  - proći kroz https://aws.amazon.com/fargate/pricing/ i objasniti specifičnosti

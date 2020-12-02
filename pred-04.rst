=============
Predavanja 04
=============


Šta je to virtuelizacija i motivacija za upotrebu? [nastavak]
=============================================================

- **NASTAVAK**, diskusija o materijalu sa prethodnih predavanja

Motivacija sa strane operations-a, tj. service/server provider-a [nastavak]
---------------------------------------------------------------------------

- ... rekapitulacija i diskusija materijala sa prethodnih predavanja ...

- FaaS (Function As A Service), kao alternativni "serverless"

  - sve prednosti i mane kako kod "serverless" container-a
  - event-driven "serverless" funkcija
  - uopšte (skoro da) ne moramo da razmišljamo o horizontalnom skaliranju (automatski scale-out i scale-in-to-zero)
  - neverovatno isplativa stvar za slabije popularne servise
  - sada možemo da merimo (i naplaćujemo) vreme izvršavanja i za ispod sekunde (obično 100ms)
  - proći kroz https://aws.amazon.com/lambda/pricing/ i objasniti specifičnosti

- primer upotrebe/cena FaaS, na bazi use-case sajta sa dostavu hrane u Novom Sadu (``materijali/pred-04`` dir)

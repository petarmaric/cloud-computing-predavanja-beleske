=============
Predavanja 10
=============


Uvod u Continuous Deployment, na cloud + serverless computing
=============================================================

Ciljevi
-------

- deployment na cloud
- automatizovana (ili automatska?) procedura za deployment na cloud
- "serverless" infrastruktura, uvek postoje serveri - ali mi ne želimo da brinemo o njima
- elastična infrastruktura, sposobna da raste (i skuplja) svoj kapacitet (i *cenu*) - u zavisnosti od opterećenja celog sistema
- bezbednost, izolacija osetljivih delova infrastrukture od interneta - kao i ostalih klijenata na našem cloud provideru


Kako sve ovo postići?
---------------------

deployment na cloud

  Nekoliko opcija za compute servis:

  - virtuelne mašine, kroz Virtual Private Server (VPS) ili cloud instancu - npr. AWS EC2
  - "serverless" container, kroz *managed* Docker image/container - npr. AWS Fargate
  - "serverless" Functions As A Service (FaaS) - npr. AWS Lambda

  Kako odabrati najpogodniji servis?

  - cena
  - brzina kojom može elastično da raste (i skuplja) svoj kapacitet
  - stepen automatizacije koji se može postići
  - stepen/vreme očekivanog održavanja
  - zrelost servisa, tj. količina (ne)poznatih bagova i njihovih workaround-ova

  Spektar cloudiness-a: virtuelne mašine << "serverless" container << "serverless" Functions As A Service

  Ne postoji idealno cloud-native, tj. cloud-bazirano, tj. generalno rešenje za ove probleme - sve je stvar kompromisa!
  Mi ćemo analizirati sve opcije, ali ćemo raditi na primeru "serverless" container-a (via Docker) - Goldilocks rešenje

  Ali šta je ostalim delovima infrastrukture, kao što je baza podataka - gde možda još (mnogo) više opcija?


automatizovana (ili automatska?) procedura za deployment na cloud

  Nekoliko opcija za podizanje cloud infrastrukture:

  - ručno, npr. kroz AWS konzolu - hahahaha, good luck with that :)
  - API bazirano, npr. kroz AWS API - manje će da boli, ali opet sve moramo ručno da zadajemo i automatizujemo (npr. infra rollback u slučaju greške?)
  - Infrastructure As Code (IaC) rešenja, npr. AWS CDK - vertikalna kriva učenja, mnogo problema sa alatom (ali se na kraju isplati)

  Kako odabrati najpogodniju deployment proceduru?

  - brzina kojom možemo da izvršimo novi deployment, tj. mutiramo infrastrukturu
  - brzina kojom možemo da promenimo (i testiramo) nove/ažurirane deployment procedure
  - održavanje konzistentnosti infrastrukture između dva deployment-a (npr. mutirati minimum infrastrukture koji mora)
  - stepen automatizacije koji se može postići
  - stepen/vreme očekivanog održavanja
  - zrelost servisa, tj. količina (ne)poznatih bagova i njihovih workaround-ova

  Spektar cloudiness-a: ručno << API bazirano << Infrastructure As Code

  Ne postoji idealno cloud-native, tj. cloud-bazirano, tj. generalno rešenje za ove probleme - sve je stvar kompromisa!
  Mi ćemo analizirati sve opcije, ali ćemo raditi na primeru Infrastructure As Code rešenja (via AWS CDK)


"serverless" infrastruktura, uvek postoje serveri - ali mi ne želimo da brinemo o njima

  Uglavnom ne moramo da brinemo o ovome, ako se držimo viših nivoa u okviru našeg spektra cloudiness-a, kao što su:

  - AWS CDK, za automatizovani deployment
  - AWS Fargate, za "serverless" compute engine
  - AWS Aurora Serverless, za "serverless" bazu podataka


elastična infrastruktura, sposobna da raste (i skuplja) svoj kapacitet (i *cenu*) - u zavisnosti od opterećenja celog sistema

  Uglavnom ne moramo da brinemo o ovome, ako se držimo (već spomenutih) viših nivoa u okviru našeg spektra cloudiness-a

  Potencijalni problemi:

  - cena (TCO = CAPEX + OPEX), može biti *nepremostiv* problem (osim ako smo Netflix)
  - brzina kojom može elastično da raste (i skuplja) svoj kapacitet
  - stepen automatizacije mehanizama za skaliranje koji se može postići
  - stepen/vreme očekivanog održavanja
  - zrelost servisa, tj. količina (ne)poznatih bagova i njihovih workaround-ova

  Svi navedeni problemi su u pozitivnoj/negativnoj korelaciji sa našom pozicijom u okviru spektra cloudiness-a.


bezbednost, izolacija osetljivih delova infrastrukture od interneta - kao i ostalih klijenata na našem cloud provideru

  Uglavnom ne moramo da brinemo o ovome, ako koristimo postojeće alate za izolaciju resursa - kao što je AWS Virtual Private Cloud (VPC)

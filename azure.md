# Azure guide and usage

## Accesso
### comando per connettersi alla VM su Azure da SSH:
```ssh -p 5007 disi@lab-cb9a98e8-b0e8-43d6-be67-c149d1c83eab.westeurope.cloudapp.azure.com```

### Credenziali per SSH

**username**: disi

**psw**: Trends2024

## Configurazione

per installare il la UI(non c'è l'ho fatta a farla andare)
1. installa i tool. FATTO
```
sudo apt install xrdp
sudo apt install xfce4
sudo reboot
```
2. *"Poi da remmina ci si connette senza problemi in grafica: basta specificare host:port nel campo server."* NON funziona

## Scaricare dataset e modello

1. **Prompt2Guard:** ```git clone https://github.com/laitifranz/Prompt2Guard.git```
2. **CDDB:** 
   1. **Nostro GitHub:** ```git clone https://github.com/IlPoiana/TrendsCV-CDD.git```
   2. **link Gdrive:** ```https://drive.google.com/drive/folders/10Yw5jYIWY1l8pn3yTnkbAD5OlTiNqc34?usp=drive_link```
   3. Esegui ```python3 setup.py``` o ```python setup.py``` per scaricare il dataset (.tar) sulla VM(scarica python se serve)
   4. Estrai il tar con ```sudo tar xopf CDDB.tar``` 
   5. Spostalo sulla home ```sudo mv /home/disi/TrendsCV-CDD/CDDBdataset/ /home/disi/```
   6. cambia la visibilità della directory per poterci accedere ```sudo chmod -R +rwx CDDB```

## Useful Links

**Microsoft guide to Azure SSH:** https://learn.microsoft.com/it-it/azure/lab-services/connect-virtual-machine#connect-to-a-linux-lab-vm-using-ssh

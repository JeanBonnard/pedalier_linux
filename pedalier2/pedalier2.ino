// les constantes ne changeront jamais. On les utilise pour initialiser les pin-Numbers
const int bouton1 = 5;     // pin-Number du bouton
const int bouton2 = 4;
const int bouton3 = 14;

int EtatBouton1 = LOW;   // variables pour lire l'état du bouton, initialisé ici à 0
int EtatBouton2 = LOW;
int EtatBouton3 = LOW;

int EtatPrecedentBouton1 = LOW;    //variable pour stocker l'état precedent du bouton, initialiser aussi à 0 car au démarrage aucun bouton n'est appuyer.
int EtatPrecedentBouton2 = LOW;
int EtatPrecedentBouton3 = LOW;

// fonction de démarrage
void setup() {
// Démarrage du bus série
Serial.begin(9600);
//Serial.begin(115200);               // vitesse
pinMode(bouton1,INPUT);
pinMode(bouton2, INPUT);
pinMode(bouton3, INPUT);
}


void loop() {
// lire l'état des bouton
delay(100);
EtatBouton1 = digitalRead(bouton1); // on lit l'état du bouton 1 ,2 et 3
EtatBouton2 = digitalRead(bouton2);
EtatBouton3 = digitalRead(bouton3);

// regarder si le bouton viens d'être appuyé ou relacher.

if (EtatBouton1 != EtatPrecedentBouton1)
{
    if(EtatPrecedentBouton1 == LOW){Serial.println("bouton1");}
    else{Serial.println("bouton+++");}
}

if (EtatBouton2 != EtatPrecedentBouton2)
{
    if(EtatPrecedentBouton2 == LOW){Serial.println("bouton2");}
    else{Serial.println("bouton+++");}
}

if (EtatBouton3 != EtatPrecedentBouton3)
{
    if(EtatPrecedentBouton3 == LOW){Serial.println("bouton3");}
    else{Serial.println("bouton+++");}
}

EtatPrecedentBouton1 = EtatBouton1;
EtatPrecedentBouton2 =    EtatBouton2;
EtatPrecedentBouton3 = EtatBouton3;
}

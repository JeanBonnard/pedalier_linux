// les constantes ne changeront jamais. On les utilise pour initialiser les pin-Numbers
const int bouton1 = 5;     // pin-Number du bouton
const int bouton2 = 4;
const int bouton3 = 14;

int buttonState1 = LOW;   // variables pour lire l'état du bouton, initialisé ici à 0
int buttonState2 = LOW;
int buttonState3 = LOW;

boolean etat_bouton1 = false;
boolean etat_bouton2 = false;
boolean etat_bouton3 = false;
  
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
  buttonState1 = digitalRead(bouton1);
  buttonState2 = digitalRead(bouton2);
  buttonState3 = digitalRead(bouton3);

  // regarder si le bouton est appuyé.
  // si il l'est,  buttonState est HIGH:
  if (buttonState1 != etat_bouton1 && etat_bouton1 == false) {
    Serial.println("bouton1");
  }
  if (buttonState2 != etat_bouton2 && etat_bouton2 == false) {
    Serial.println("bouton2");
  }
  if (buttonState3 != etat_bouton3 && etat_bouton3 == false) {
    Serial.println("bouton3");
  }
  etat_bouton1 = buttonState1;
  etat_bouton2 = buttonState2;
  etat_bouton3 = buttonState3;
}

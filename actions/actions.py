
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import requests

# Action : Obtenir des Informations sur une carriere
class ActionObtenirInformationsCarriere(Action):
    def name(self) -> Text:
        return "action_obtenir_informations_carriere"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        carriere = tracker.get_slot("carriere")

        # Logique pour obtenir des informations sur la carrière
        # Vous pouvez utiliser des API externes, une base de données, etc.
        #x = requests.get('http://127.0.0.1:8000/api/carriere')

        # Seach by name api/all/?name=
        #query =f"http://127.0.0.1:8000/api/all"
        query_2 = "http://127.0.0.1:8000/api/all/?name="+carriere.lower()
        #parametres = {"name": carriere}
        #print(query_2)
        x = requests.get(query_2)
        #print(x.json())
        if (x.status_code !=  404):
            description_carriere = x.json()[0]['description']
            response = f"{carriere} c'est quoi ?:\n{description_carriere}"
        else:
            response =  " Desolé , je n'ai pas encore appris à répondre à cette question ;)"

        dispatcher.utter_message(response)

        return []


class ActionExplorerOptionsEtudes(Action):
    def name(self) -> Text:
        return "action_explorer_options_etudes"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        domaine = tracker.get_slot("domaine_etude")
        # Logique pour explorer les options d'études
        # Vous pouvez utiliser des bases de données, des API, etc.
        query = "http://127.0.0.1:8000/api/cursus/?name=" + domaine.lower()

        x = requests.get(query)
        # Check if isset any error
        if (x.status_code == 404):
            response = " Informations pas encore disponible ;) - EduBot Mali"
        else:
            # print(x.status_code == 404)
            # description_carriere = 'TEst'
            description_carriere = x.json()[0]['description']
            response = f"Voici quelques options d'études disponibles en {domaine} :\n{description_carriere} "

        dispatcher.utter_message(response)

        return []


class ActionConseilOrientationAcademique(Action):
    def name(self) -> Text:
        return "action_conseil_orientation_academique"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        diplome = tracker.get_slot("diplome")
        query = "http://127.0.0.1:8000/api/diplomes/?name=" + diplome.lower()

        x = requests.get(query)
        # Check if isset any error
        if(x.status_code == 404):
            response = " Informations pas encore disponible ;) - EduBot Mali"
        else:
            #print(x.status_code == 404)
            #description_carriere = 'TEst'
            description_carriere = x.json()[0]['description']

            response = f"Voici les Possibilités d'emploi avec un(e) {diplome} :\n{description_carriere} "
        dispatcher.utter_message(response)

        return []


class ActionEtablissementAcademique(Action):
    def name(self) -> Text:
        return "action_etablissement"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        etablissement = tracker.get_slot("etablissement")
        query = "http://127.0.0.1:8000/api/etablissement/?name=" + etablissement.lower()

        x = requests.get(query)
        # Check if isset any error
        if(x.status_code == 404):
            response = " Informations pas encore disponible ;) - EduBot Mali"
        else:
            #print(x.status_code == 404)
            #description_carriere = 'Test'
            description_carriere = x.json()[0]['description']

            response = f"Voici les informations sur {etablissement} :\n{description_carriere} "
        dispatcher.utter_message(response)

        return []

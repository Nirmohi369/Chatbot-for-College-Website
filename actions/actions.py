# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions



from typing import Any, Text, Dict, List,Union

from rasa_sdk import Action,Tracker
from rasa_sdk.executor import CollectingDispatcher


Fees = {
    "8" : "35,600",
    "7" : "38,000",
    "6" : "35,500",
    "5" : "34,000",
    "4" : "39,000",
    "3" : "35,500",
    "2" : "34,000",
    "1" : "39,000"
}
Subjects = {
    "8" : "Android, AI, BIG Data Analytics",
    "7" : "MCWC, DMBI, INS, CD",
    "6" : "SE, TOC, AJAVA, DOT NET, WT",
    "5" : "ADA, JAVA, SP, MPI",
    "4" : "CN, C++, OS, COA, NM",
    "3" : "DBMS, DS, DE, Maths3",
    "2" : "EG",
    "1" : "C"
}

class ActionKnowFees(Action):

    def name(self) -> Text:
        return "action_know_fees"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        fee = Fees.get(semester)

        if fee is None:
            output = "Could not find fees of {}".format(semester)
        else:
            output = "Fees of {} semester is {}".format(semester,fee)

        dispatcher.utter_message(output)

        return []

class ActionKnowSubjects(Action):

    def name(self) -> Text:
        return "action_know_subjects"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        semester = tracker.get_slot("semester")
        sub = Subjects.get(semester)

        if sub is None:
            output = "Could not find subjects of {}".format(semester)
        else:
            output = "Subjects of {} semester are {}".format(semester,sub)
        
        dispatcher.utter_message(text=output)

        return []
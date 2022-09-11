from pythonds.basic.queue import Queue
import random



class Patient:
    """
    A class to simulate patients in a clinic
    """
    def __init__(self, time):
        """
        The current patient is intialized with the arrival time given to the method and his age (which is a random number between 20 and 60)
        :param time: the time this patient got into the queue in seconds
        """
        self.arrivalTime = time
        self.age = random.randrange(20, 61)

    def getAge(self):
        """
        Gets the Age of the patient
        :return: Integer between 20 and 60
        """
        return self.age

    def getArrivalTime(self):
        """
        Gets the Arrival Time of the Patient
        :return: integer between 0 and the Max simulation time passed to the main function
        """
        return self.arrivalTime

    def waitTime(self, currentSec):
        """
        Computes the amount time this patient waited in the queue before entering
        :param currentSec: the time this patient got out of the queue in seconds
        :return: integer more than or equal zero
        """
        return currentSec - self.arrivalTime
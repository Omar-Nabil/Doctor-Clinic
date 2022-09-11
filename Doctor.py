from Patient import *


class Doctor:
    """
    A class to simulate a doctor treating patients in a clinic
    """

    def __init__(self, rate):

        """
        The doctor is initialized with the rate of treating patients, and NO current patients
        :param rate: the rate of treating patients
        """

        self.patientRate = rate
        self.timeRemaining = 0
        self.currentPatient = None

    def enterNextPatient(self, patient):
        """
        This Method simulates the entering of the patients to the doctor
        :param patient: the next patient according to the queue (object of class Patient)
        :return: No return value
        """

        self.currentPatient = patient

        # Time taken to treat each patient = Age/5  or  Age/10  (* 60 to get it in seconds)
        self.timeRemaining = round(patient.getAge()/self.patientRate) * 60

    def busy(self):
        """
        Method to check whether the doctor is free or not
        :return: boolean value (True if busy, False if not)
        """
        return self.currentPatient is not None

    def tick(self):
        """
        This method simulates the clock in the clinic, one call for this method means that 1 second has passed
        :return: No return value
        """
        if self.currentPatient is not None:
            self.timeRemaining -= 1
            if self.timeRemaining == 0:
                self.currentPatient = None
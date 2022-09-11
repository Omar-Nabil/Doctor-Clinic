from Doctor import *

########################################################################################################################
# Write a Python program that simulates a doctor's clinic from 12 pm to 4pm. On any average day,
# about 10 patients arrive to the clinic at any given hour. The patients ages typically are in between 20 and 60.
# Each Age from 20 to 60 is equally likely. The clinic deals with the patients by a first-come first-served manner.
# Patient time with the doctor is calculated by the following formula: patient time with doctor = (Age/5) minutes.
# The output of the simulation are the average waiting time of the patients and the number of remaining patients at 4pm.
# If patient time with doctor changes to (Age/10) minutes,
# what are the average waiting time of the patients and the number of remaining patients at 4pm?
########################################################################################################################


def printResult(times, remaining):
    """
    Prints the result in the desired format
    """
    averageWaitTime = sum(times)/len(times)/60
    print("Average Waiting Time : ", "{:.2f}".format(averageWaitTime), " mins \t , Untreated Patients : ", remaining)



###########################################################################################
# According to the Problem we get an average of 10 patients per hour :                    #
# 10 P/ hr = 10 P/ 60 min = 10 P / 3600 sec = 1 P / 360 sec                               #
# so the probability of a new patient coming to the clinic in the next second is 1 to 360 #
# Which is applied by the following function :                                            #
###########################################################################################
def newPatientArrived():
    """
    Function to check if a patient arrived in the current second or not
    :return: an integer from 1 to 360
    """
    return random.randrange(1, 361) == 150


def simulate(totalSimulationTime, rate):
    """
    Function to simulate the work of a clinic in a specific period of time
    :param totalSimulationTime: The amount of time you need to simulate the working of the clinic in hours
    :param rate: The rate of treating patients
    :return: No return value
    """

    # Convert to seconds
    totalSimulationTime *= 3600

    # Prepare
    clinicDoctor = Doctor(rate)
    patientQueue = Queue()
    waitingTimes = []

    # Iterate over each second
    for currentSec in range(totalSimulationTime):

        # Check if a patient arrived in this second
        if newPatientArrived():
            # YES? :
            # Add him to the queue
            newPatient = Patient(currentSec)
            patientQueue.enqueue(newPatient)

        # Check if the doctor is free and there are patients in the queue :
        if (not clinicDoctor.busy()) and (not patientQueue.isEmpty()):
            # YES? :
            # Enter the following patient to the doctor
            nextPatient = patientQueue.dequeue()
            clinicDoctor.enterNextPatient(nextPatient)

            # Save the amount of time this patient waited in the list "waitingTimes"
            waitingTimes.append(nextPatient.waitTime(currentSec))

        # 1 second passed in the clinic
        clinicDoctor.tick()

    # Print the results
    averageWaitTime = sum(waitingTimes) / len(waitingTimes) / 60
    print("Average Waiting Time : ", "{:.2f}".format(averageWaitTime), " mins \t , Untreated Patients : ", patientQueue.size())
    return averageWaitTime

########################
# We can then simulate with both rates (Age/5 and Age/10) and compare the results :

# Age / 5 :
print("Incase of (Age/5) : ")
s= 0
for i in range(500):
    simulate(4, 5)
    s += simulate(4,5)
print("avrege of all runs",s/500)
def patientQueue(queue):
    queue = Queue()
    a=queue.size()
    for i in range(a+1):
        x=queue.dequeue()
        y=x.getage()/5
        sum=0
        sum += y
    print("the waitingtime",sum)




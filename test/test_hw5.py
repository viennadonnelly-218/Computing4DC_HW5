import pytest

from computing4dc_hw5 import hw5


def test_patient_default_covid_risk():
    # initialise a patient with no symptoms
    dobby = hw5.Patient(name="Dobby", symptoms=["long nose", "big ears"])    
    # a default patient with no symptoms should have a 0.05 probability of having covid
    assert dobby.has_covid() == pytest.approx(0.05)

def test_patient_symptoms():
    # now lets add some symptomps
    dobby = hw5.Patient(name="Dobby", symptoms=["happy"])
    dobby.symptoms += ["fever", "cough"]
    assert dobby.has_covid() == pytest.approx(0.25)  # +0.1 for each symptom

def test_patient_covid_test():
    # add a positive test!
    dobby = hw5.Patient(name="Dobby", symptoms=["happy"])
    dobby.add_test("covid", True)
    assert dobby.has_covid() == pytest.approx(0.99)

def test_patient_covid_test_negative():
    # now add an all-clear
    dobby = hw5.Patient(name="Dobby", symptoms=["happy"])
    dobby.add_test("covid", False)
    assert dobby.has_covid() == pytest.approx(0.01)

def test_patient_non_covid_test():
    # add a non-covid test
    dobby = hw5.Patient(name="Dobby", symptoms=["happy"])
    dobby.add_test("flu", True)
    assert dobby.has_covid() == pytest.approx(0.05)  # should not affect covid probability

package com.example.demo.service;

import com.example.demo.entity.Patient;
import com.example.demo.repository.PatientRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class PatientServiceImpl implements PatientService {

    @Autowired
    private PatientRepository patientRepository;

    @Override
    public Patient savePatient(Patient patient) {
        return patientRepository.save(patient);
    }

    @Override
    public List<Patient> getAllPatients() {
        return patientRepository.findAll();
    }

    @Override
    public Patient getPatientById(Long id) {
        return patientRepository.findById(id).orElse(null);
    }

    @Override
    public Patient updatePatient(Long id, Patient patient) {
        Patient existingPatient = patientRepository.findById(id).orElse(null);

        if (existingPatient != null) {
            existingPatient.setFirstName(patient.getFirstName());
            existingPatient.setLastName(patient.getLastName());
            existingPatient.setAge(patient.getAge());
            existingPatient.setGender(patient.getGender());
            existingPatient.setBloodGroup(patient.getBloodGroup());
            existingPatient.setPhone(patient.getPhone());
            existingPatient.setEmail(patient.getEmail());
            existingPatient.setAddress(patient.getAddress());
            existingPatient.setDisease(patient.getDisease());

            return patientRepository.save(existingPatient);
        }

        return null;
    }

    @Override
    public void deletePatient(Long id) {
        patientRepository.deleteById(id);
    }
}
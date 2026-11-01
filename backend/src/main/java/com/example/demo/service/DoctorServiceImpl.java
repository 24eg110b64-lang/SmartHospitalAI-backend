package com.example.demo.service;

import com.example.demo.entity.Doctor;
import com.example.demo.repository.DoctorRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class DoctorServiceImpl implements DoctorService {

    @Autowired
    private DoctorRepository doctorRepository;

    @Override
    public Doctor saveDoctor(Doctor doctor) {
        return doctorRepository.save(doctor);
    }

    @Override
    public List<Doctor> getAllDoctors() {
        return doctorRepository.findAll();
    }

    @Override
    public Doctor getDoctorById(Long id) {
        return doctorRepository.findById(id).orElse(null);
    }

    @Override
    public Doctor updateDoctor(Long id, Doctor doctor) {

        Doctor existingDoctor = doctorRepository.findById(id).orElse(null);

        if (existingDoctor != null) {
            existingDoctor.setDoctorName(doctor.getDoctorName());
            existingDoctor.setSpecialization(doctor.getSpecialization());
            existingDoctor.setExperience(doctor.getExperience());
            existingDoctor.setQualification(doctor.getQualification());
            existingDoctor.setPhone(doctor.getPhone());
            existingDoctor.setEmail(doctor.getEmail());
            existingDoctor.setAvailability(doctor.getAvailability());
            existingDoctor.setConsultationFee(doctor.getConsultationFee());

            return doctorRepository.save(existingDoctor);
        }

        return null;
    }

    @Override
    public void deleteDoctor(Long id) {
        doctorRepository.deleteById(id);
    }
}

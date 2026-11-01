package com.example.demo.service;

import com.example.demo.entity.Appointment;

import java.util.List;

public interface AppointmentService {

    Appointment saveAppointment(Appointment appointment);

    List<Appointment> getAllAppointments();

    Appointment getAppointmentById(Long id);

    Appointment updateAppointment(Long id, Appointment appointment);

    void deleteAppointment(Long id);
}
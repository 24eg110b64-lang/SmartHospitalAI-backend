package com.example.demo.controller;

import com.example.demo.entity.User;
import com.example.demo.repository.UserRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("/auth")
@CrossOrigin("*")
public class UserController {

    @Autowired
    private UserRepository userRepository;

    @PostMapping("/login")
    public Object login(@RequestBody User loginUser) {

        Optional<User> user =
                userRepository.findByUsername(loginUser.getUsername());

        if (user.isPresent() &&
            user.get().getPassword().equals(loginUser.getPassword())) {

            return user.get();
        }

        return "Invalid username or password";
    }
}
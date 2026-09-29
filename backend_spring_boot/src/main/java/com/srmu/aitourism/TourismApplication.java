package com.srmu.aitourism;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

/**
 * AI-Based Tourism Recommendation and Itinerary Planner
 * Shri Ramswaroop Memorial University (SRMU), Lucknow
 * Department of Computer Science & Information Systems
 */
@SpringBootApplication
public class TourismApplication {
    public static void main(String[] args) {
        SpringApplication.run(TourismApplication.class, args);
        System.out.println(">>> Spring Boot Tourism RAG Application Started Successfully <<<");
    }
}

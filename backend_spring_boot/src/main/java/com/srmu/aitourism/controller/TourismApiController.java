package com.srmu.aitourism.controller;

import com.srmu.aitourism.entity.Attraction;
import com.srmu.aitourism.repository.AttractionRepository;
import com.srmu.aitourism.service.TourismRagService;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.*;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "*")
public class TourismApiController {

    private final AttractionRepository attractionRepository;
    private final TourismRagService ragService;

    public TourismApiController(AttractionRepository attractionRepository, TourismRagService ragService) {
        this.attractionRepository = attractionRepository;
        this.ragService = ragService;
    }

    @GetMapping("/destinations")
    public ResponseEntity<Map<String, Object>> getDestinations() {
        List<Map<String, Object>> circuits = List.of(
            Map.of("id", "LKO", "name", "Lucknow", "region", "Awadh Heritage Circuit"),
            Map.of("id", "VNS", "name", "Varanasi", "region", "Ganga Spiritual Circuit"),
            Map.of("id", "AGR", "name", "Agra", "region", "Braj-Mughal Heritage Circuit"),
            Map.of("id", "AYD", "name", "Ayodhya", "region", "Ramayana Circuit"),
            Map.of("id", "PRY", "name", "Prayagraj", "region", "Triveni Sangam Circuit"),
            Map.of("id", "MTH", "name", "Mathura & Vrindavan", "region", "Krishna Janmabhoomi Circuit")
        );
        return ResponseEntity.ok(Map.of("destinations", circuits, "total", circuits.size()));
    }

    @GetMapping("/attractions")
    public ResponseEntity<List<Attraction>> getAttractions(
            @RequestParam(required = false) String city,
            @RequestParam(required = false) String category,
            @RequestParam(defaultValue = "false") boolean wheelchairOnly) {

        if (city != null && wheelchairOnly) {
            return ResponseEntity.ok(attractionRepository.findByCityIgnoreCaseAndWheelchairAccessibleTrue(city));
        } else if (city != null) {
            return ResponseEntity.ok(attractionRepository.findByCityIgnoreCase(city));
        }
        return ResponseEntity.ok(attractionRepository.findAll());
    }

    @PostMapping("/chat")
    public ResponseEntity<Map<String, Object>> chatWithGroundedAssistant(@RequestBody Map<String, String> request) {
        String query = request.getOrDefault("query", "");
        String city = request.getOrDefault("city", "");
        Map<String, Object> result = ragService.askTourismAssistant(query, city);
        return ResponseEntity.ok(result);
    }
}

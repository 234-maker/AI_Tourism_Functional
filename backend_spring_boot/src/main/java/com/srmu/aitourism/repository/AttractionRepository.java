package com.srmu.aitourism.repository;

import com.srmu.aitourism.entity.Attraction;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AttractionRepository extends JpaRepository<Attraction, String> {
    List<Attraction> findByCityIgnoreCase(String city);
    List<Attraction> findByCityIgnoreCaseAndCategoryIgnoreCase(String city, String category);
    List<Attraction> findByCityIgnoreCaseAndWheelchairAccessibleTrue(String city);
    List<Attraction> findByCityIgnoreCaseAndSeniorFriendlyTrue(String city);
}

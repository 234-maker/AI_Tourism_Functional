package com.srmu.aitourism.entity;

import jakarta.persistence.*;
import lombok.*;

@Entity
@Table(name = "attractions")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Attraction {

    @Id
    @Column(length = 20)
    private String id;

    @Column(nullable = false)
    private String name;

    @Column(nullable = false)
    private String city;

    @Column(nullable = false)
    private String state;

    @Column(nullable = false, length = 50)
    private String category;

    @Column(columnDefinition = "TEXT")
    private String description;

    @Column(name = "open_time", length = 10)
    private String openTime;

    @Column(name = "close_time", length = 10)
    private String closeTime;

    @Column(name = "fee_adult_inr")
    private Double feeAdultInr;

    @Column(name = "fee_foreigner_inr")
    private Double feeForeignerInr;

    @Column(name = "indicative_duration_hours")
    private Double indicativeDurationHours;

    @Column(name = "wheelchair_accessible")
    private Boolean wheelchairAccessible;

    @Column(name = "senior_friendly")
    private Boolean seniorFriendly;

    @Column(name = "walking_intensity", length = 20)
    private String walkingIntensity;

    private Double latitude;
    private Double longitude;

    @Column(name = "source_name")
    private String sourceName;

    @Column(name = "source_url", columnDefinition = "TEXT")
    private String sourceUrl;
}

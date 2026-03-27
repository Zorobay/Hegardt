package se.hegardt.dto

import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.Location

@Serdeable
class LocationDto {
    Long id
    String city
    String country
    String region
    String notes
    Double latitude
    Double longitude

    static LocationDto from(Location location) {
        if (!location) return new LocationDto()
        new LocationDto(
            id: location.id,
            city: location.city,
            country: location.country,
            region: location.region,
            notes: location.notes,
            latitude: location.latitude,
            longitude: location.longitude,
        )
    }
}

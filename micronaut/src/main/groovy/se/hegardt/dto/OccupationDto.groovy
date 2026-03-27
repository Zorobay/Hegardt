package se.hegardt.dto

import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.Occupation

@Serdeable
class OccupationDto {

    Long id
    String notes
    LocationDto location
    PartialDateDto date

    static OccupationDto from(Occupation occupation) {
        if (!occupation) return new OccupationDto()
        return new OccupationDto(
            id: occupation.id,
            notes: occupation.notes,
            location: LocationDto.from(occupation.location),
            date: PartialDateDto.from(occupation.date)
        )
    }
}

package se.hegardt.dto

import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.LifeEvent

@Serdeable
class LifeEventDto {
    Long id
    String notes
    PartialDateDto date
    LocationDto location

    static LifeEventDto from(LifeEvent event) {
        if (!event) return new LifeEventDto()
        new LifeEventDto(
            id: event.id,
            notes: event.notes,
            date: PartialDateDto.from(event.date),
            location: LocationDto.from(event.location)
        )
    }
}

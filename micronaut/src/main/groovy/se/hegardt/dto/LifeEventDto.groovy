package se.hegardt.dto

import groovy.transform.CompileStatic
import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.LifeEvent

@Serdeable
@CompileStatic
class LifeEventDto {
    Long id
    String notes
    PartialDateDto date
    LocationDto location

    static LifeEventDto from(LifeEvent event) {
        if (!event) return new LifeEventDto()
        return new LifeEventDto(
            id: event.id,
            notes: event.notes,
            date: PartialDateDto.from(event.date),
            location: LocationDto.from(event.location)
        )
    }
}

package se.hegardt.dto

import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.Marriage

@Serdeable
class MarriageDto {

    Long id
    String notes
    PersonSummaryDto spouse1
    PersonSummaryDto spouse2
    PartialDateDto date
    LocationDto location

    static MarriageDto from(Marriage marriage) {
        if (!marriage) return new MarriageDto()
        return new MarriageDto(
            id: marriage.id,
            notes: marriage.notes,
            spouse1: PersonSummaryDto.from(marriage.spouse1),
            spouse2: PersonSummaryDto.from(marriage.spouse2),
            date: PartialDateDto.from(marriage.date),
            location: LocationDto.from(marriage.location)
        )
    }
}

package se.hegardt.dto

import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.Person

@Serdeable
class PersonDto extends PersonSummaryDto {
    String notes
    Integer pdfPage

    List<Integer> childrenIds = []
    int fatherId
    int motherId

    static PersonDto from(Person person) {
        new PersonDto(
            id: person.id,
            firstName: person.firstName,
            lastName: person.lastName,
            middleNames: person.middleNames,
            notes: person.notes,
            sex: person.sex?.name(),
            pdfPage: person.pdfPage,
            birth: LifeEventDto.from(person.birth),
            death: LifeEventDto.from(person.death),
            burial: LifeEventDto.from(person.burial),
        )
    }
}

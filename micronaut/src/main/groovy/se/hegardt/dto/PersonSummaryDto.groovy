package se.hegardt.dto

import groovy.transform.CompileStatic
import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.Person

@Serdeable
@CompileStatic
class PersonSummaryDto {
    Long id
    String firstName
    String lastName
    String middleNames
    String sex
    LifeEventDto birth
    LifeEventDto death
    LifeEventDto burial

    String notes
    Integer pdfPage

    static PersonSummaryDto from(Person person) {
        if (!person) return null
        return new PersonSummaryDto(
            id: person.id,
            firstName: person.firstName,
            lastName: person.lastName,
            middleNames: person.middleNames,
            sex: person.sex?.name(),
            birth: LifeEventDto.from(person.birth),
            death: LifeEventDto.from(person.death),
            burial: LifeEventDto.from(person.burial),
            notes: person.notes,
            pdfPage: person.pdfPage
        )
    }
}

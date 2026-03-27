package se.hegardt.dto

import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.Occupation
import se.hegardt.domain.Person

@Serdeable
class PersonDto {
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

    Set<Occupation> occupations = []
    Set<MarriageDto> marriages = []
    Set<PersonSummaryDto> children = []
    Set<PersonSummaryDto> siblings = []
    PersonSummaryDto father
    PersonSummaryDto mother

    static PersonDto from(Person person) {
        new PersonDto(
            id: person.id,
            firstName: person.firstName,
            lastName: person.lastName,
            middleNames: person.middleNames,
            sex: person.sex?.name(),
            birth: LifeEventDto.from(person.birth),
            death: LifeEventDto.from(person.death),
            burial: LifeEventDto.from(person.burial),
            notes: person.notes,
            pdfPage: person.pdfPage,
            father: PersonSummaryDto.from(person.father),
            mother: PersonSummaryDto.from(person.mother)
        )
    }
}

package se.hegardt.dto

import groovy.transform.CompileStatic
import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.Occupation
import se.hegardt.domain.Person

@Serdeable
@CompileStatic
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

    PersonSummaryDto father
    PersonSummaryDto mother

    // Fetched by PersonsService
    Set<MarriageDto> marriages = []
    Set<PersonSummaryDto> children = []
    Set<PersonSummaryDto> siblings = []

    Set<OccupationDto> occupations = []
    Set<PdfReferenceDto> pdfReferences = []

    static PersonDto from(Person person) {
        return new PersonDto(
            id: person.id,
            firstName: person.firstName,
            lastName: person.lastName,
            middleNames: person.middleNames,
            sex: person.sex?.name(),
            birth: LifeEventDto.from(person.birth),
            death: LifeEventDto.from(person.death),
            burial: LifeEventDto.from(person.burial),
            notes: person.notes,
            father: PersonSummaryDto.from(person.father),
            mother: PersonSummaryDto.from(person.mother),
            occupations: person.occupations.collect(OccupationDto.&from).toSet(),
            pdfReferences: person.pdfReferences.collect(PdfReferenceDto.&from).toSet()
        )
    }
}

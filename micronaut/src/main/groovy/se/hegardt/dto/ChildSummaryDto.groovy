package se.hegardt.dto

import groovy.transform.CompileStatic
import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.Person

@Serdeable
@CompileStatic
class ChildSummaryDto extends PersonSummaryDto {

    PersonMinimalDto father
    PersonMinimalDto mother

    static ChildSummaryDto from(Person person) {
        if (!person) return null
        return new ChildSummaryDto(
            id: person.id,
            firstName: person.firstName,
            lastName: person.lastName,
            middleNames: person.middleNames,
            sex: person.sex?.name(),
            birth: LifeEventDto.from(person.birth),
            death: LifeEventDto.from(person.death),
            burial: LifeEventDto.from(person.burial),
            father: PersonMinimalDto.from(person.father),
            mother: PersonMinimalDto.from(person.mother),
            notes: person.notes,
        )
    }
}

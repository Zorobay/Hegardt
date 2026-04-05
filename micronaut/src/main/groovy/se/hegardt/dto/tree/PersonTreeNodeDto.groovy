package se.hegardt.dto.tree

import groovy.transform.CompileStatic
import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.Person
import se.hegardt.dto.LifeEventDto

@Serdeable
@CompileStatic
class PersonTreeNodeDto {
    Long id
    String firstName
    String lastName
    String middleNames
    String sex
    LifeEventDto birth
    LifeEventDto death
    LifeEventDto burial

    PersonTreeNodeDto father
    PersonTreeNodeDto mother

    static PersonTreeNodeDto from(Person person) {
        if (!person) return null
        return new PersonTreeNodeDto(
            id: person.id,
            firstName: person.firstName,
            lastName: person.lastName,
            middleNames: person.middleNames,
            sex: person.sex?.name(),
            birth: LifeEventDto.from(person.birth),
            death: LifeEventDto.from(person.death),
            burial: LifeEventDto.from(person.burial),
            father: from(person.father),
            mother: from(person.mother)
        )
    }
}

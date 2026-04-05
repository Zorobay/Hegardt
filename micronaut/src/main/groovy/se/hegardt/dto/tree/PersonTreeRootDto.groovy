package se.hegardt.dto.tree

import groovy.transform.CompileStatic
import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.Person
import se.hegardt.dto.LifeEventDto
import se.hegardt.dto.PersonSummaryDto

@CompileStatic
@Serdeable
class PersonTreeRootDto {
    Long id
    String firstName
    String lastName
    String middleNames
    String sex
    LifeEventDto birth
    LifeEventDto death
    LifeEventDto burial

    Set<PersonSummaryDto> children = []
    PersonTreeNodeDto father
    PersonTreeNodeDto mother

    static PersonTreeRootDto from(Person person, List<Person> children) {
        if (!person) return null
        return new PersonTreeRootDto(
            id: person.id,
            firstName: person.firstName,
            lastName: person.lastName,
            middleNames: person.middleNames,
            sex: person.sex?.name(),
            birth: LifeEventDto.from(person.birth),
            death: LifeEventDto.from(person.death),
            burial: LifeEventDto.from(person.burial),
            children: children.collect { Person child -> PersonSummaryDto.from(child) }.toSet(),
            father: PersonTreeNodeDto.from(person.father),
            mother: PersonTreeNodeDto.from(person.mother)
        )
    }
}

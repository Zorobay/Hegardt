package se.hegardt.dto

import groovy.transform.CompileStatic
import io.micronaut.serde.annotation.Serdeable
import se.hegardt.domain.Person

@Serdeable
@CompileStatic
class PersonMinimalDto {

    Long id
    String firstName
    String lastName
    String middleNames
    String sex

    static PersonMinimalDto from(Person person) {
        if (!person) return null
        return new PersonMinimalDto(
            id: person.id,
            firstName: person.firstName,
            lastName: person.lastName,
            middleNames: person.middleNames,
            sex: person.sex?.name(),
        )
    }
}

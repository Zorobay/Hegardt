package se.hegardt.service

import io.micronaut.transaction.annotation.Transactional
import se.hegardt.domain.Person
import se.hegardt.dto.PersonDto
import se.hegardt.dto.tree.PersonTreeRootDto

interface IPersonsService {
    List<Person> findAll()

    Optional<Person> getById(Long id)

    @Transactional(readOnly = true)
    Optional<PersonDto> getCompleteById(Long id)

    @Transactional(readOnly = true)
    Optional<PersonTreeRootDto> getTreeRootById(Long id)

    Collection<Person> findByName(String name)

    Person update(Person person)
}

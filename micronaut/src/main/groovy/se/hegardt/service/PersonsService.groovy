package se.hegardt.service

import groovy.transform.CompileStatic
import io.micronaut.transaction.annotation.Transactional
import jakarta.inject.Singleton
import se.hegardt.domain.Marriage
import se.hegardt.domain.Person
import se.hegardt.dto.MarriageDto
import se.hegardt.dto.PersonDto
import se.hegardt.dto.PersonSummaryDto
import se.hegardt.helper.StringHelper
import se.hegardt.repository.MarriageRepository
import se.hegardt.repository.PersonsRepository

@Singleton
@CompileStatic
class PersonsService {
    private final PersonsRepository repository
    private final MarriageRepository marriageRepository

    PersonsService(PersonsRepository repository, MarriageRepository marriageRepository) {
        this.repository = repository
        this.marriageRepository = marriageRepository
    }

    List<Person> findAll() {
        return repository.findAll().toList()
    }

    Optional<Person> getById(Long id) {
        return repository.findById(id)
    }

    @Transactional(readOnly = true)
    Optional<PersonDto> getCompleteById(Long id) {
        Optional<Person> person = repository.findById(id)
        if (person.present) {
            PersonDto personDto = PersonDto.from(person.get())
            // TODO get occupations
            personDto.children = repository.findChildren(personDto.id)
                .collect { Person child -> PersonSummaryDto.from(child) }
                .toSet()

            personDto.siblings = findSiblings(personDto)
            personDto.marriages = marriageRepository.findAllByPersonId(id)
                .collect { Marriage marriage -> MarriageDto.from(marriage) }
                .toSet()

            return Optional.of(personDto)
        }
        return Optional.empty()
    }

    Collection<Person> findByName(String name) {
        if (!name?.trim()) return []

        List<String> tokens = name
            .trim()
            .split(/\s+/)
            .collect { String str -> StringHelper.normalize(str) } as List<String>
        return repository.findByNameTokens(tokens).toSet()
    }

    Person save(Person person) {
        return repository.save(person)
    }

    Person merge(Person person) {
        return repository.merge(person)
    }

    Person update(Person person) {
        return repository.update(person)
    }

    void delete(Long id) {
        repository.deleteById(id)
    }

    private Set<PersonSummaryDto> findSiblings(PersonDto person) {
        Set<Person> siblings = []
        if (person.mother) {
            siblings.addAll(repository.findChildren(person.mother.id))
        }
        if (person.father) {
            siblings.addAll(repository.findChildren(person.father.id))
        }
        siblings.removeAll { Person sibling -> sibling.id == person.id }
        return siblings.collect { Person sibling -> PersonSummaryDto.from(sibling) }.toSet()
    }
}

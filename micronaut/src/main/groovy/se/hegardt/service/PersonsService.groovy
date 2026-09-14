package se.hegardt.service

import groovy.transform.CompileStatic
import io.micronaut.transaction.annotation.Transactional
import jakarta.inject.Singleton
import se.hegardt.domain.Marriage
import se.hegardt.domain.PdfReference
import se.hegardt.domain.Person
import se.hegardt.dto.MarriageDto
import se.hegardt.dto.PdfReferenceDto
import se.hegardt.dto.PersonDto
import se.hegardt.dto.PersonSummaryDto
import se.hegardt.dto.tree.PersonTreeRootDto
import se.hegardt.helper.StringHelper
import se.hegardt.repository.MarriageRepository
import se.hegardt.repository.PdfReferenceRespository
import se.hegardt.repository.PersonsRepository

@Singleton
@CompileStatic
class PersonsService implements IPersonsService {
    private final PersonsRepository personRepo
    private final PdfReferenceRespository pdfReferenceRespo
    private final MarriageRepository marriageRepo

    PersonsService(PersonsRepository personsRepository,
                   PdfReferenceRespository pdfReferenceRespository,
                   MarriageRepository marriageRepository) {
        this.personRepo = personsRepository
        this.pdfReferenceRespo = pdfReferenceRespository
        this.marriageRepo = marriageRepository
    }

    List<Person> findAll() {
        return personRepo.findAll().toList()
    }

    Optional<Person> getById(Long id) {
        return personRepo.findById(id)
    }

    @Transactional(readOnly = true)
    Optional<PersonDto> getCompleteById(Long id) {
        Optional<Person> person = personRepo.findById(id)
        if (person.present) {
            PersonDto personDto = PersonDto.from(person.get())
            // TODO get occupations
            personDto.children = personRepo.findChildren(personDto.id)
                .collect { Person child -> PersonSummaryDto.from(child) }
                .toSet()

            personDto.siblings = findSiblings(personDto)
            personDto.marriages = marriageRepo.findAllByPersonId(id)
                .collect { Marriage marriage -> MarriageDto.from(marriage) }
                .toSet()
            personDto.pdfReference = pdfReferenceRespo.findByPersonId(id)
                .map { PdfReference ref -> PdfReferenceDto.from(ref) }
                .orElse(null)

            return Optional.of(personDto)
        }
        return Optional.empty()
    }

    @Transactional(readOnly = true)
    Optional<PersonTreeRootDto> getTreeRootById(Long id) {
        Optional<Person> optional = personRepo.findById(id)
        if (optional.present) {
            Person person = optional.get()
            List<Person> children = personRepo.findChildren(person.id)
            PersonTreeRootDto treeRootDto = PersonTreeRootDto.from(person, children)
            return Optional.of(treeRootDto)
        }
        return Optional.empty()
    }

    Collection<Person> findByName(String name) {
        if (!name?.trim()) return []

        List<String> tokens = name
            .trim()
            .split(/\s+/)
            .collect { String str -> StringHelper.normalize(str) } as List<String>
        return personRepo.findByNameTokens(tokens).toSet()
    }

    Person update(Person person) {
        return personRepo.update(person)
    }

    private Set<PersonSummaryDto> findSiblings(PersonDto person) {
        Set<Person> siblings = []
        if (person.mother) {
            siblings.addAll(personRepo.findChildren(person.mother.id))
        }
        if (person.father) {
            siblings.addAll(personRepo.findChildren(person.father.id))
        }
        siblings.removeAll { Person sibling -> sibling.id == person.id }
        return siblings.collect { Person sibling -> PersonSummaryDto.from(sibling) }.toSet()
    }
}

package se.hegardt.service

import io.micronaut.test.extensions.spock.annotation.MicronautTest
import jakarta.inject.Inject
import se.hegardt.domain.Marriage
import se.hegardt.domain.Person
import se.hegardt.dto.PersonDto
import se.hegardt.dto.tree.PersonTreeRootDto
import se.hegardt.repository.MarriageRepository
import se.hegardt.repository.PersonsRepository
import spock.lang.Specification

@MicronautTest
class PersonsServiceSpec extends Specification {

    @Inject
    PersonsRepository personsRepository

    @Inject
    PersonsService personService

    @Inject
    MarriageRepository marriageRepository

    private Person grandpa = null
    private Person grandma = null
    private Person father = null
    private Person uncle = null
    private Person aunt = null
    private Person mother = null
    private Person son = null
    private Person daughter = null
    private Person baby = null

    def setup() {
        grandpa = personsRepository.save(new Person(id: 119, firstName: 'Grandpa', lastName: 'Family'))
        grandma = personsRepository.save(new Person(id: 120, firstName: 'Grandma', lastName: 'Family'))
        uncle = personsRepository.save(new Person(id: 121, firstName: 'Uncle', lastName: 'Family'))
        aunt = personsRepository.save(new Person(id: 122, firstName: 'Aunt', lastName: 'Family'))
        father = personsRepository.save(new Person(id: 123, firstName: 'Father', lastName: 'Family'))
        mother = personsRepository.save(new Person(id: 124, firstName: 'Mother', lastName: 'Family'))
        son = personsRepository.save(new Person(id: 125, firstName: 'Son', lastName: 'Family'))
        daughter = personsRepository.save(new Person(id: 126, firstName: 'Daughter', lastName: 'Family'))
        baby = personsRepository.save(new Person(id: 127, firstName: 'Baby', lastName: 'Family'))

        father.father = grandpa
        father.mother = grandma
        uncle.father = grandpa
        uncle.mother = grandma
        aunt.father = grandpa
        aunt.mother = grandma
        son.father = father
        son.mother = mother
        daughter.father = father
        daughter.mother = mother
        baby.father = father
        baby.mother = mother
        personsRepository.saveAll([son, daughter, baby])

        marriageRepository.save(new Marriage(id: 1, spouse1: father, spouse2: mother))
        marriageRepository.save(new Marriage(id: 2, spouse1: grandpa, spouse2: grandma))
    }

    def 'findAll'() {
        when:
            List<Person> res = personService.findAll()
        then:
            res.size() == 9
            res.any { it.id == 119 && it.firstName == 'Grandpa' }
            res.any { it.id == 120 && it.firstName == 'Grandma' }
            res.any { it.id == 121 && it.firstName == 'Uncle' }
            res.any { it.id == 122 && it.firstName == 'Aunt' }
            res.any { it.id == 123 && it.firstName == 'Father' }
            res.any { it.id == 124 && it.firstName == 'Mother' }
            res.any { it.id == 125 && it.firstName == 'Son' }
            res.any { it.id == 126 && it.firstName == 'Daughter' }
            res.any { it.id == 127 && it.firstName == 'Baby' }
    }

    def 'getById'() {
        given:
            Optional<Person> res = personService.getById(id)
        expect:
            if (expectedId) {
                assert res.present
                Person person = res.get()
                assert person.id == expectedId
                assert person?.firstName == firstName
            } else {
                assert !res.present
            }
        where:
            id  | expectedId | firstName
            123 | 123        | 'Father'
            124 | 124        | 'Mother'
            125 | 125        | 'Son'
            126 | 126        | 'Daughter'
            127 | 127        | 'Baby'
            128 | null       | null
    }

    def 'getCompleteById: existing id'() {
        when:
            Optional<PersonDto> res = personService.getCompleteById(father.id)
        then:
            res.present
            PersonDto person = res.get()
            person.id == father.id
            person.firstName == 'Father'
            person.father.id == grandpa.id
            person.father.firstName == 'Grandpa'
            person.mother.id == grandma.id
            person.mother.firstName == 'Grandma'
            person.children.size() == 3
            person.children.every { it.id in [125L, 126L, 127L] }
            person.children.every { it.firstName in ['Son', 'Daughter', 'Baby'] }
            person.siblings.size() == 2
            person.siblings.every { it.id in [121L, 122L] }
            person.siblings.every { it.firstName in ['Aunt', 'Uncle'] }
            person.marriages.size() == 1
            person.marriages.first().spouse1.id == father.id
            person.marriages.first().spouse2.id == mother.id
    }

    def 'getCompleteById: non-existing id'() {
        when:
            Optional<PersonDto> res = personService.getCompleteById(300)
        then:
            !res.present
    }

    def 'getTreeRootById'() {
        when:
            Optional<PersonTreeRootDto> res = personService.getTreeRootById(father.id)
        then:
            res.present
            PersonTreeRootDto root = res.get()
            root.id == father.id
            root.children.size() == 3
            root.father.id == grandpa.id
            root.mother.id == grandma.id
    }

    def 'findByName'() {
        when:
            List<PersonDto> res = personService.findByName(name) as List<PersonDto>
        then:
            res.size() == expectedSize
            res.toSet().every { it.id in expectedIds }
        where:
            name           | expectedSize | expectedIds
            'Family'       | 9            | [119L, 120L, 121L, 122L, 123L, 124L, 125L, 126L, 127L]
            'Son'          | 1            | [125L]
            'Grand'        | 2            | [119L, 120L]
            'Grand family' | 2            | [119L, 120L]
            'Farmily'      | 0            | []
    }
}
